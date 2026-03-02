from input_processing import convert_pattern_type




#to print summary of all
def print_summary_all(pattern_objs):
    print(f"These are the summaries of all the patterns")
    for obj in pattern_objs:
        print_output(obj)
    return

# to search for a pattern name
def print_result_search(pattern_objs, search_term):
    print (f"This is the result of a search for {search_term} pattern:\n")
    for obj in pattern_objs:
        if obj.name == search_term:
            print_output(obj)
    return

# to search for a pattern type
def print_result_type(pattern_objs, p_type):
    matching_objs = []
    '''
    if type(p_type) is str:
        pattern_type = convert_pattern_type(p_type)
        print(f"new_pattern type after conversion is {pattern_type}")
    else:
        print(f"p_type is {p_type} of type {type(p_type)}")
    #print_result_type(pattern_objs, pattern_type)
    '''
    print(f"This is the result of a search for {p_type} type patterns:\n")
    counter = 0
    for obj in pattern_objs:

        #print (f"obj, search {obj.pattern_type}, {pattern_type}")
        if  p_type in obj.pattern_type:
           #print_output(obj)
           matching_objs.append(obj)
           counter+=1
        else: 
            continue
    #print(f"There are {counter} patterns that match")
    return matching_objs





# print the details of one pattern obj
def print_output(pattern_obj):
    print (pattern_obj.attribute_summary())
    print (pattern_obj.images())
    print()
    return