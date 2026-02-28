from input_processing import read_csv_file,extract_keys,make_pattern_dictionarys,create_dictionary_from_csv
from pattern_classes import PatternType,Pattern,KnittingPattern


def main():




    # knitting pattern keys
    '''
    "Name",
    "Designer",
    "Rollup_designer",
    "Type",
    "Date_added",
    "Notes",
    "Attachments",
    "Number_of_Attachments",
    "Image.png?",
    "Attachment_filenames_regex",
    "Batch_attachment_archive_in_dropbox",
    "RecordId",
    "Status",
    "Projects",
    "Projects_from_rollup",
    "Paper_folder",
    "Project_completed_need_to_record",
    "Checked_file_into_subcategory",
    "Dropbox_link",
    "Projects_3",
    "Last_modified",
    "Google_sheet_sync",
    "Unsaved_changes",
    
    '''
    required_keys = [
    "Name",
    "Designer",
    "Type",
    "Date_added",
    "Notes",
    "Attachments",
    "Number_of_Attachments",
    "Attachment_filenames_regex",
    "Batch_attachment_archive_in_dropbox",
    "RecordId",
    "Status",
    "Projects",
    "Paper_folder",
    "Project_completed_need_to_record",
    "Checked_file_into_subcategory",
    "Dropbox_link",
    "Last_modified",
    "Google_sheet_sync",
    "Unsaved_changes",
    ]
    

    filepath = "./test_knitting_patterns_table__patterns_input.csv"

    dictionarys = create_dictionary_from_csv(filepath)






















main()