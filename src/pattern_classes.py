from enum import Enum
import os



class CraftType(Enum):
    KNIT = "knitting"
    SEW = "sewing"


class PatternType(Enum):
    NECK = "Shawl/Scarf/Cowl"
    SOCKS = "Socks"
    HATS = "Hats"
    BOOK = "Book"
    CHILD = "Baby/Child"
    JUMPER = "Cardigan/Jumper"
    CHARTS = "Charts" 
    DOG = "Dog"
    GLOVES = "Gloves/Mitts"
    HOUSEHOLD = "Household/Decorations"
    TOYS = "Toys"
    MULTI = "Multi"
    DRESS = "Dress"
    GEN = "General instructions or notes"
    LEGGINGS = "Leggings"
    




class Pattern:
    # name is text, keys is a list, attributes is a dictionary with key,value pairs
    def __init__(self,name,keys,attributes):
        self.name = name
        self.attributes = attributes
        self.keys = keys


    def __repr__(self):
        return f"Pattern object({self.name})"
    





class KnittingPattern(Pattern):
    def __init__(self,name,keys,attributes):
        super().__init__(name,keys,attributes)
        self.designer = attributes[keys[2]]
        
        self.pattern_type = attributes[keys[3]]
        self.date_added = attributes[keys[4]]
        self.notes = attributes[keys[5]]
        self.num_attach = attributes[keys[7]]
        
        self.attachments = attributes[keys[9]]
        self.attachment_batch = attributes[keys[10]]
        self.dropbox_link = attributes[keys[18]]
        

    '''
attributes:

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




    def attribute_summary(self):

        return f'{self.name} by {self.designer} has a type {self.pattern_type}, '
    
    def list_of_properties(self):
         # This produces a set of properties that will be printed out
         prop_list = []
         prop_list.append(f"Designer: {self.designer}")
         pattern_type = self.pattern_type
         pattern_type = pattern_type.replace(",",", ")
         prop_list.append(pattern_type)
         prop_list.append(self.notes)
         prop_list.append(f'number of attachments: {self.num_attach}')
         #prop_list.append(f'{self.make_dropbox_links_html()}')
         
         return prop_list
    
    def images(self):
        
        return f'There are {self.num_attach} attachments stored in {self.attachment_batch}\nThe attachments are {self.attachments}'
    
    def make_image_strings(self):
        #print(f"method raw is {self.attachments}")
        raw_strings = self.attachments.split(",")
        #print(f"method raw after splitting {raw_strings}")
        modified_strings = []
        for raw_string in raw_strings:
            # remove all spaces and removed symbols so filenames match
            raw_string = raw_string.strip()
            raw_string = raw_string.replace(" ","")
            raw_string = raw_string.replace('"','')
            raw_string = raw_string.replace("'",'')
            raw_string = raw_string.replace("&",'')
            modified_strings.append(raw_string)
            
        batch = self.make_batch_folder_name()
        num_attach = int(self.num_attach)
        image_strings=[]

                
        for i in range(num_attach):

            image_strings.append(f'<img src = "image/{os.path.join(batch,modified_strings[i])}">')
        #print (f"method return image strings {image_strings}")   
        return image_strings
        
    def make_batch_folder_name(self):
        batch_folder_name = self.attachment_batch
        batch_folder_name = batch_folder_name.replace(":","_")
        return batch_folder_name
    
    def make_dropbox_links_html(self):
        dropbox_link_string = self.dropbox_link
        print (dropbox_link_string)
        link_strings = dropbox_link_string.split()
        print (link_strings)
        return_string = ""
        counter = 1
        for link_string in link_strings:
            
            link_string_html = f'<a href="{link_string}">Pattern Link {counter}</a>\n'
            counter += 1
            return_string += link_string_html
            
        return return_string







class Library:
     # name is text, keys is a list, attributes is a dictionary with key,value pairs
    def __init__(self,input_filepath,keys,craft_type, obj_list, name):
        
        self.input_filepath = input_filepath
        self.keys = keys
        self.craft_type = craft_type
        self.number = len(obj_list)
        self.obj_list = obj_list
        self.name = name


    def __repr__(self):
        return f"Library from ({self.input_filepath} contains {self.number} {self.craft_type.value} patterns)"
    
    def info_string(self):
        return f"Library from {self.input_filepath} contains {self.number} {self.craft_type} patterns"
    
    def csv_string(self):
        return f'{self.input_filepath}'