import unicodedata

from pattern_classes import PatternType,Pattern,KnittingPattern,CraftType
from input_processing import read_csv_file,extract_keys, make_pattern_dictionarys,create_dictionarys_from_csv, convert_pattern_type



def separate_patterns(keys,dictionarys):
    print(f"separating {len(dictionarys)} dictionaries\n\n")
    #takes in a list of dictionarys and creates a knitting pattern object for each one
    pattern_obj_list = []
    for dictionary in dictionarys:
        #print (dictionary)
        name = dictionary[keys[0]]
        #print (name)
        pattern_obj = make_knitting_pattern_obj(name,keys,dictionary)

        # correct the pattern type to the enum 
        #print(f"original pattern type is {pattern_obj.pattern_type}")
        #some have multiple pattern_types so need to parse
       # ptypes = []
       # att_string = pattern_obj.pattern_type
       # att_string = unicodedata.normalize('NFKD',att_string)
       # ptypes = att_string.split(",")
       # print (f"pattern types for {pattern_obj} are {ptypes}")
       # adjusted_types = []
       # for ptype in ptypes:
           # new_pattern_type = convert_pattern_type(pattern_obj.pattern_type)
           # adjusted_types.append(new_pattern_type)
       # if adjusted_types:

           # pattern_obj.pattern_type = adjusted_types
        #print (f"corrected pattern type is {pattern_obj.pattern_type}")
        pattern_obj_list.append(pattern_obj)
       

    return pattern_obj_list


   

def make_knitting_pattern_obj(name,keys,dict):
    #print(f"making objects")
    knit_obj = KnittingPattern(name,keys,dict)
    return knit_obj
