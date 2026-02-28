import sys
import csv
from pattern_classes import PatternType,Pattern,KnittingPattern





def create_dictionary_from_csv(filepath):
    if filepath:
        
        parsed_lists = read_csv_file(filepath)
                    #parsed_lists = parse_csv(lines)
        #print(parsed_lists[0])
        #print()
        #print(parsed_lists[1])
        keys = extract_keys(parsed_lists)
        for key in keys:
            print(f'{key},')
            #continue
        
        #for list in parsed_lists:
            #print (list[0])
        dictionarys = make_pattern_dictionarys(keys,parsed_lists)
        #print (dictionarys[0])
        
            
        #print(dictionary_line_1)



def read_csv_file(filepath):
    # Basic pattern for reading a text file line by line

    

    with open(filepath, "r", encoding="utf-8") as csvfile:
        try:
            #print(csv.Dialect)
            lines = list(csv.reader(csvfile,dialect = 'excel'))
                    
           # print(lines[0])
           # print(lines[1])
            print(f"lines has length {len(lines)}")
            #string = string.replace(" ","_")
            new_line = []
            results = []
            for line in lines: 
                    for item in line:
                
                                  # loop over each line in the file
                       # remove spaces and newline ?
                       # correct those fields with newlines in them
                    #print(line)
                        new_item = item.replace("\n"," ")
                        new_line.append(new_item)
                    #print(line)               
                    results.append(line)

            # now `results` is a list of processed lines
            return results
        except Exception as e:
            print(f"Error: read operation failed with error {e}")

'''
def parse_csv(lines):
    parsed_lists = []
    for line in lines:
        this_list = line.split(",")
        parsed_lists.append(this_list)
    return parsed_lists
'''
def extract_keys(parsed_lists):
    raw=parsed_lists[0]
    keys=[]
    # colummn headings are in the first row of the spreadsheet
    # process key to get rid of space etc
    i=0
    for item in raw:
        i +=1
        item = f'"{item.replace(" ","_")}"'
        keys.append(item)
        #print(i,item)
    
    return keys

def make_pattern_dictionarys(keys,parsed_lists):
    dictionarys = []
    this_pattern_dictionary = {}
    print(f"length of keys {len(keys)}")
    print(f"length of parsed_lists {len(parsed_lists)}")
    # for each pattern (first list in parsed_lists is the key list)
    i=0
    j=0
    
    for i  in range(1,len(parsed_lists)):
        #for each key
        for j in range (len(keys)):
            
            this_row = parsed_lists[i]
            
            this_pattern_dictionary[keys[j]] = this_row[j]
            if i<3:
                print(keys[j],this_row[j])

    return dictionarys
        

