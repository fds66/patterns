import argparse
from enum import Enum

from input_processing import read_csv_file,extract_keys,make_pattern_dictionarys,create_dictionarys_from_csv, convert_pattern_type
from pattern_classes import PatternType,Pattern,KnittingPattern,CraftType
from make_pattern_obj import separate_patterns,make_knitting_pattern_obj
from print_outputs import print_summary_all, print_result_search, print_result_type

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
    #############################################################
    # simple print outputs
    
    #to print summary of all
    if args.all is True:
        print_summary_all(pattern_objs)

    
    # to search for a pattern name
    if args.Search_name:
        search_term = args.Search_name
        print_result_search(pattern_objs, search_term)

    # to search for a pattern type
    #print (f"access the enum value by .value {PatternType.GLOVES.value}")
    
    
    if args.Search_ptype:
        pattern_type = args.Search_ptype
        matching_objs = print_result_type(pattern_objs, pattern_type)
        print(f"There were {len(matching_objs)} matches ")
        if matching_objs:
            for obj in matching_objs:
                print(obj.name)







    return














main()