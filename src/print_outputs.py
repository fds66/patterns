

#to print summary of all
def print_summary_all(pattern_objs):
    print(f"These are the summaries of all the patterns")
    for obj in pattern_objs:
        print_output(obj)
    return

# to search for a pattern name
def print_result_search(pattern_objs, search_term):
    found_objs = []
    print (f"This is the result of a search for {search_term} pattern:\n")
    for obj in pattern_objs:
        if search_term.lower() in obj.name.lower():
            found_objs.append(obj)
            print_output(obj)
    return found_objs 
         

# to search for a pattern type
def print_result_type(pattern_objs, p_type):
    
    print(f"This is the result of a search for {p_type} type patterns:\n")
    matching_objs = []   
    counter = 0
    for obj in pattern_objs:
        if  p_type in obj.pattern_type:
           print(obj.name)
           matching_objs.append(obj)
           counter+=1
        else: 
            continue
    
    return matching_objs

# to print the details of one pattern obj
def print_output(pattern_obj):
    print (pattern_obj.attribute_summary())
    print (pattern_obj.images())
    print()
    return