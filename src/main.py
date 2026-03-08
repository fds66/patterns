import argparse
from enum import Enum

from input_processing import read_csv_file,extract_keys,make_pattern_dictionarys,create_dictionarys_from_csv, convert_pattern_type
from pattern_classes import PatternType,Pattern,KnittingPattern,CraftType,Library
from make_pattern_obj import separate_patterns,make_knitting_pattern_obj
from print_outputs import print_summary_all, print_result_search, print_result_type
from make_html import make_search_page, make_type_page, make_all_images_page, make_blank_page, make_home_page, make_summary_page

def main():

    

    # Process commandline arguments so they are available

    parser = argparse.ArgumentParser(description="Pattern library search and summarise")
    #Required
    parser.add_argument("craft_type", type = str,  help = "knit or sew")
    parser.add_argument("csv_filepath", type=str,  help="relative filepath to the csv file from the root")
    #Optional
    parser.add_argument("-s","--Search_name", type = str, help = "the name of the pattern you are searching for")
    parser.add_argument("-t","--Search_ptype", type = str, help = "the category of pattern you are searching for")
    parser.add_argument("-a","--all", action='store_true',help = "output summaries of all patterns")
    args = parser.parse_args()

   
# Now we can access `args.csv_filepath` and craft_type
    

    craft_type = args.craft_type
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
    print (filepath)
    
    # now we can parse the csv and create the list of keys and the list of pattern dictionarys, one dictionary for each pattern

    keys,dictionarys = create_dictionarys_from_csv(filepath)
    # to get list of keys use this section
    '''
    i=0
    for key in keys:
        print(f"{i} {key},")
        i+=1
    '''

    # convert the pattern dictionarys into pattern objects

    knitting_objs = separate_patterns(keys,dictionarys)
    #will add in the sewing option later
    #if KNIT pattern_objs = knitting_objs, if SEW pattern_objs = sewing_obs

    pattern_objs = knitting_objs


    # create library
    library_name = "Knitting Patterns"
    library = Library(filepath, keys, craft_type, pattern_objs, library_name)


    #############################################################
    # simple print outputs and html static pages
    # setup the file paths
    template_dir = "/home/fds66/workspace/fds66/patterns/static/templates/page_components"
    output_dir = "/home/fds66/workspace/fds66/patterns/static/templates/test_outputs"
    output_files={
        "text": "info.html",
        "single": "pattern_search.html",
        "multi": "type_search.html",
        "home": "index.html",
        "all": "all.html"
         }
    
    
    # create home page

    make_home_page(template_dir, output_dir, library, output_files)



    #to print summary of all
    if args.all is True:
        print_summary_all(pattern_objs)

    make_summary_page(template_dir, output_dir, library, output_files)   

    

    # to search for a pattern name
    if args.Search_name:
        search_term = args.Search_name
        print(f"searching for {search_term}\n")
        make_search_page(template_dir, output_dir, library, search_term, output_files)
    #otherwise make a blank page
    else:
        make_blank_page(template_dir, output_dir, library, output_files, "blank_search")

      

    # to search for a pattern type
    #print (f"access the enum value by .value {PatternType.GLOVES.value}")
    
    
    if args.Search_ptype:
        pattern_type = args.Search_ptype
        matching_objs = print_result_type(pattern_objs, pattern_type)
        print(f"There were {len(matching_objs)} matches ")
        if matching_objs:
            for obj in matching_objs:
                print(obj.name)
        make_type_page(template_dir, output_dir, library, pattern_type, output_files)
    #otherwise make a blank page
    else:
        make_blank_page(template_dir, output_dir, library, output_files, "blank_type_search")


    ############testing html generation#################
    # print all in a grid to test the image strings

    make_all_images_page(template_dir, output_dir, library, output_files)

    #make_blank_page(template_dir, output_dir, library, output_files, "blank_search")

    

    return














main()