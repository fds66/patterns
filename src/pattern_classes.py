from enum import Enum


class CraftType(Enum):
    KNIT = "knitting pattern"
    SEW = "sewing pattern"


class PatternType(Enum):
    JUMPER = ""



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
        self.attachments = attributes[keys[6]]
        self.attachment_regex = attributes[keys[9]]
        self.attachment_batch = attributes[keys[10]]
        

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
    
    def images(self):
        
        return f'There are {self.num_attach} attachments stored in {self.attachment_batch}\nThe attachments are {self.attachment_regex}'
        

