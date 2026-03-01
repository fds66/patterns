

from pattern_classes import PatternType,Pattern,KnittingPattern,CraftType
from input_processing import read_csv_file,extract_keys,make_pattern_dictionarys,create_dictionarys_from_csv



def separate_patterns(keys,dictionarys):
    print(f"separating {len(dictionarys)} dictionaries\n\n")
    #takes in a list of dictionarys and creates a knitting pattern object for each one
    pattern_obj_list = []
    for dictionary in dictionarys:
        #print (dictionary)
        name = dictionary[keys[0]]
        #print (name)
        pattern_obj = make_knitting_pattern_obj(name,keys,dictionary)
        pattern_obj_list.append(pattern_obj)

    return pattern_obj_list


   

def make_knitting_pattern_obj(name,keys,dict):
    #print(f"making objects")
    knit_obj = KnittingPattern(name,keys,dict)
    return knit_obj
