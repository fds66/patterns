import argparse
import os
import sys


from input_processing import create_dictionarys_from_csv
from pattern_classes import CraftType,Library
from make_pattern_obj import separate_patterns
from print_outputs import print_summary_all
from make_html import make_search_page, make_type_page, make_all_images_page, make_blank_page, make_home_page, make_summary_page

def main():

    
    
    # setup the file paths and parameters -----------------------------------------------------------
    template_dir = "/home/fds66/workspace/fds66/patterns/static/templates/page_components"
    output_dir = "/home/fds66/workspace/fds66/patterns/docs" # for final use and github
    #output_dir = "static/templates/test_outputs" # for testing and working on css
    
    
    output_files={
        "text": "info.html",
        "single": "pattern_search.html",
        "multi": "type_search.html",
        "home": "index.html",
        "all": "all.html"
         }
    image_dir = "image/"
    library_name = "Knitting Patterns"

    #copy style sheet to chosen output directory
    stylesheet_path = "static/templates/test_outputs/global_style.css"

    # check paths

    if not os.path.isdir(output_dir):
        raise Exception ("output directory path given is not a directory")
    if not os.path.exists(stylesheet_path):
        raise Exception ("stylesheet does not exist")
    
    #read current stylesheet
    try:
        with open(stylesheet_path,"r") as f:
            content = f.read()
    except Exception as e:
        raise Exception (f"{stylesheet_path} cannot be read, error {e}")
    
    #write contents into output directory
    copy_stylesheet_path = os.path.join(output_dir,"global_style.css")
    try: 
        with open(copy_stylesheet_path, 'w') as file:
            file.write(content)
            
    except Exception as e:
        raise Exception ("writing to the file failed")

    # Process commandline arguments so they are available ----------------------------------------------------

    parser = argparse.ArgumentParser(description="Pattern library search and summarise")
    #Required
    parser.add_argument("craft_type", type = str,  help = "knit or sew")
    parser.add_argument("csv_filepath", type=str,  help="relative filepath to the csv file from the root")
    #Optional
    parser.add_argument("-s","--search_name", type = str, help = "the name of the pattern you are searching for")
    parser.add_argument("-t","--search_ptype", type = str, help = "the category of pattern you are searching for")
    parser.add_argument("-a","--all", action='store_true',help = "output summaries of all patterns")
    args = parser.parse_args()

    
    # Now we can access csv_filepath and craft_type ----------------------------
    
    craft_type = args.craft_type

    # This converts the craft type into an Enum, not sure if I will eventually use this, not used currently
    match(craft_type):

        case "knit":
            craft = CraftType.KNIT
        case "sew":
            craft = CraftType.SEW
        case _:
            raise Exception ("first argument should be either knit or sew")
        
    
    filepath = args.csv_filepath
    if not filepath:
        raise Exception ("No csv filepath given")
    if not os.path.isfile(filepath):
        raise Exception ("csv filepath does not exist")
    #print (filepath)
    
    # now we can parse the csv and create the list of keys and the list of pattern dictionarys, one dictionary for each pattern ----------------------------

    keys,dictionarys = create_dictionarys_from_csv(filepath)
    
    # convert the pattern dictionarys into pattern objects, knitting objects already implemented, sewing objects not yet implemented -----------------------

    
    sewing_objs = None # not implemented yet
    match (craft_type):
        case "knit":
            knitting_objs = separate_patterns(keys,dictionarys, image_dir)
            pattern_objs = knitting_objs
        case "sew":
            pattern_objs = sewing_objs
            raise Exception (" Not implemented sewing patterns yet")
        case _:
            raise Exception ("Unknown craft_type")

    # create library --------------------------------------------------------------
    
    library = Library(filepath, keys, craft_type, pattern_objs, library_name)

    # simple print outputs and html static pages ----------------------------
    
    # create home page  and library information summary page -----------------------

    make_home_page(template_dir, output_dir, library, output_files)
    make_summary_page(template_dir, output_dir, library, output_files) 

    # If the command line switch -a --all is used an image grid of all pattern is created along with a text output
    
    if args.all:
        print_summary_all(pattern_objs)
        make_all_images_page(template_dir, output_dir, library, output_files)
        
    else:
        make_blank_page(template_dir, output_dir, library, output_files, "blank_all_no_request")  

    # if the command line switch -s --search_name is used a pattern name search is carried out and the resulting pattern shown on a page and a text output

    if args.search_name:
        search_term = args.search_name
        print(f"searching for {search_term}\n")
        make_search_page(template_dir, output_dir, library, search_term, output_files)

    #otherwise make a blank page
    else:
        make_blank_page(template_dir, output_dir, library, output_files, "blank_search_no_request")

      

    # if the command line switch -t --search_ptype is used a pattern type search is carried out and the resulting patterns shown on a page and a text output
        
    if args.search_ptype:
        pattern_type = args.search_ptype
        print(f"searching for {search_term}\n")
        make_type_page(template_dir, output_dir, library, pattern_type, output_files)

    #otherwise make a blank page
    else:
        make_blank_page(template_dir, output_dir, library, output_files, "blank_type_search_no_request")


    return














main()