
from pattern_classes import KnittingPattern




def separate_patterns(keys,dictionarys,image_dir):
    #takes in a list of dictionarys and keys and creates a knitting pattern object for each one
    pattern_obj_list = []
    for dictionary in dictionarys:
        name = dictionary[keys[0]]
        pattern_obj = KnittingPattern(name,keys,dictionary, image_dir)
        pattern_obj_list.append(pattern_obj)
    return pattern_obj_list


