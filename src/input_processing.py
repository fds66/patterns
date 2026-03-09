
import csv
from pattern_classes import PatternType





def create_dictionarys_from_csv(filepath):
    if filepath:
        # get the parsed lists from the csv file
        parsed_lists = read_csv_file(filepath)
        # create a set of keys from the headings, the first line of the csv
        keys = extract_keys(parsed_lists)
        #create a dictionary for each pattern in the csv which corresponds to one row
        dictionarys = make_pattern_dictionarys(keys,parsed_lists)
        return keys,dictionarys
    else:
        raise Exception ("no filepath to read csv")
       
def read_csv_file(filepath):
    #open the csv file and read line by line

    with open(filepath, "r", encoding="utf-8") as csvfile:
        try:
            # typecast them into a list instead of reader objects
            lines = list(csv.reader(csvfile,dialect = 'excel'))
            # store the lines in a list to use them later
            new_line = []
            results = []
            for line in lines: 
                    # loop over each item in the line (they were separated by , in the csv and parsed by csv.reader)
                    for item in line:
                        # correct those fields with newlines in them, just replace them with a space in case the newlines cause problems later
                        new_item = item.replace("\n"," ")
                        new_line.append(new_item)
                    # add the list of all the items in that row to the list of all the rows               
                    results.append(line)

            # now `results` is a list of processed lines
            return results
        except Exception as e:
            print(f"Error: read operation failed with error {e}")


def extract_keys(parsed_lists):
    #extract the headings in row 1 to create a list of keys
    raw = parsed_lists[0]
    keys = []
    # process key to get rid of space etc (need to inspect the heading in case there are symbols in there that might cause problems)
    i=0
    for item in raw:
        i +=1
        item = f'{item.replace(" ","_")}'
        keys.append(item)
    return keys

def make_pattern_dictionarys(keys,parsed_lists):
    # use the key list we created to make a dictionary for each row, (each pattern)
    dictionarys = []
    this_pattern_dictionary = {}
    
    # for each pattern (first list in parsed_lists is the key list)
        
    for i  in range(1,len(parsed_lists)):
        #for each key
        this_row = parsed_lists[i]
        this_pattern_dictionary = {}
        for j in range (len(keys)):
            this_pattern_dictionary[keys[j]] = this_row[j]
        dictionarys.append(this_pattern_dictionary)

    # return a list of all the dictionarys
    return dictionarys

# convert the command line argument into an Enum pattern type in PatternType
def convert_pattern_type(ptype_string):
    
    for t in PatternType:
        this_type = t.value
        if ptype_string in this_type:
            print(f"Success, found {ptype_string} in {this_type}")
            return t
    else:
        raise Exception ("pattern type not found")
            
        
    
        

  

