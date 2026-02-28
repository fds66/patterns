import argparse
from enum import Enum

from input_processing import read_csv_file,extract_keys,make_pattern_dictionarys,create_dictionarys_from_csv
from pattern_classes import PatternType,Pattern,KnittingPattern,CraftType
from make_pattern_obj import separate_patterns,make_knitting_pattern_obj

def main():




    # knitting pattern keys
    '''
    0 Name,
    1 Designer,
    2 Rollup_designer,
    3 Type,
    4 Date_added,
    5 Notes,
    6 Attachments,
    7 Number_of_Attachments,
    8 Image.png?,
    9 Attachment_filenames_regex,
    10 Batch_attachment_archive_in_dropbox,
    11 RecordId,
    12 Status,
    13 Projects,
    14 Projects_from_rollup,
    15 Paper_folder,
    16 Project_completed_need_to_record,
    17 Checked_file_into_subcategory,
    18 Dropbox_link,
    19 Projects_3,
    20 Last_modified,
    21 Google_sheet_sync,
    22 Unsaved_changes,
    
    '''

    parser = argparse.ArgumentParser(description="Pattern library search and summarise")
    parser.add_argument("csv_filepath", type=str, help="relative filepath to the csv file")
    #parser.add_argument("craft_type"), type = CraftType, help = "KNIT or SEW"
    parser.add_argument("-s","--Search_name", type = str, help = "the name of the pattern you are searching for")
    parser.add_argument("-a","--all", action='store_true',help = "output summaries of all patterns")
    args = parser.parse_args()

    '''
    # Add an optional argument with choices
    parser.add_argument('--color', choices=['red', 'green', 'blue'], help='choose a color')

    # Parse the arguments
    args = parser.parse_args()

    # Use the optional argument
    if args.color:
    print(f"You chose the color: {args.color}")

    compulsory
    parser.add_argument('--use-lang', required=True, help="Output language")
    
    '''


# Now we can access `args.user_prompt`
    filepath = args.csv_filepath
    if not filepath:
        raise Exception ("No csv filepath given")
    print (filepath)
   

    #filepath = "./test_knitting_patterns_table__patterns_input.csv"

    keys,dictionarys = create_dictionarys_from_csv(filepath)
    # to get list of keys use this section
    '''
    i=0
    for key in keys:
        print(f"{i} {key},")
        i+=1
    '''
    knitting_objs = separate_patterns(keys,dictionarys)



    #############################################################
    #Outputs
    
    #to print summary of all
    if args.all is True:
        print(f"These are the summaries of all the patterns")
        for obj in knitting_objs:
            print (obj.attribute_summary())
            print (obj.images())
            print()

    

    if args.Search_name:
        search_term = args.Search_name
        print (f"This is the result of a search for {search_term} pattern:\n")
        for obj in knitting_objs:
            if obj.name == search_term:
                print (obj.attribute_summary())
                print (obj.images())
                print()
























main()