import os
from pattern_classes import Pattern, Library, KnittingPattern,CraftType
from print_outputs import print_result_search, print_result_type


#------------------- Page calls from main -----------------------------------------------------

# if the page isn't requested or the search returns no result produce a blank page with an appropriate message
def make_blank_page(template_dir, output_dir, library, output_files, blank_type):
    
    page_type_lookup = {
        "blank_search_no_result": "single",
        "blank_type_search_no_result": "multi",
        "blank_all_no_result": "all",
        "blank_search_no_request": "single",
        "blank_type_search_no_request": "multi",
        "blank_all_no_request": "all",
          }
    if "no_request" in blank_type:
        blank_reason = "no_request"
    else:
        blank_reason = "no_result"

    page_type = page_type_lookup[blank_type]
    make_html_file(template_dir, output_dir, library, library.obj_list, page_type, output_files, blank_reason)
    return

# make a home page
def make_home_page(template_dir, output_dir, library, output_files):
    page_type = "home"
    success = make_html_file(template_dir, output_dir, library, library.obj_list, page_type, output_files)
    if success:
        print(f"HTML home page successfully made\n")
    return
    
# make an image grid of all patterns in the library
def make_all_images_page(template_dir, output_dir, library, output_files):
    page_type = "all"
    success = make_html_file(template_dir, output_dir, library, library.obj_list, page_type, output_files)
    if success:
        print(f"HTML all images page successfully made\n")
    return

# make a page for the results of a pattern name search 
def make_search_page(template_dir, output_dir, library, search_term, output_files):   
    page_type = "single"
    found_objs = print_result_search(library.obj_list, search_term)
    if found_objs:
        success = make_html_file(template_dir, output_dir, library, found_objs, page_type, output_files)
        if success:
            print (f"HTML search page successfully made\n")
    else:
        print (f"No match found")
        make_blank_page(template_dir, output_dir, library, output_files, "blank_search_no_result")
    return

# make a page for the results of a pattern type search
def make_type_page(template_dir, output_directory, library, search_term, output_files):
    page_type = "multi"
    found_objs = print_result_type(library.obj_list, search_term)
    if found_objs:
        success = make_html_file(template_dir, output_directory, library, found_objs, page_type, output_files)
        if success:
            print (f"HTML type search page successfully made\n")
    else:
        print (f"No match found")
        make_blank_page(template_dir, output_directory, library, output_files, "blank_type_search_no_result")
    return

# make a page for summary information about the library
def make_summary_page(template_dir, output_directory, library, output_files):
    page_type = "text"
    success = make_html_file(template_dir, output_directory, library, library.obj_list, page_type, output_files)
    if success:
        print(f"HTML information page successfully made\n")
    return
    
#------------------------ create HTML page from the component templates ------------------------------------------

def make_html_file(template_dir, output_dir, library, found_objs, page_type, output_files, blank=""):
    
    if not os.path.isdir(template_dir):
        raise Exception ("template directory given is not a directory")
    if not os.path.isdir(output_dir):
        raise Exception ("template directory given is not a directory")
    if not library:
        raise Exception ("no library")
    if not found_objs:
        raise Exception ("no object found in search")
    if not type(found_objs) is list:
        raise Exception ("found object must be a list")
    if not type(output_files) is dict:
        raise Exception ("output files should be a dictionary")

    #need to check the inputs are valid - not empty, is a directory, etc 
    
    # create an html file by concatenating the parts
    full_html = []

    #---------------- head --------------------------

    head = make_head_html(template_dir)
    if head:
        full_html.append(head)
    else:
        raise Exception ("Head template not read")
    
    # --------------- header ------------------------
    
    header_strings = {
        "text": "Library Information",
        "single": "Pattern Search",
        "multi": "Pattern Type Search",
        "home": "Home",
        "all": "Library Image Grid"
         }
    header_text = header_strings[page_type]
    header = make_header_html(template_dir, header_text)
    if header:
        full_html.append(header)
    else:
        raise Exception ("failed to add header")
    
    #---------------- nav bar -------------------------
    nav = make_nav_html(template_dir)
    if nav:
        full_html.append(nav)
    else:
        raise Exception ("failed to add navigation")

    #---------------- main body ----------------------------

    # switch to the correct type of page  single, multi, text, home, blank

    if blank != "":
        match (blank):
            case "no_request":
                message = "No page of this type requested"
            case "no_result":
                message = "No search results"
            case _:
                message = ""
        blank_body = make_blank_body(template_dir, message)        
        if blank_body:
            full_html.append(blank_body)
        else:
            raise Exception ("failed to add text page")
        
    else:
        match (page_type):

            case "text":
                text_body = make_text_body_html(template_dir, library)
                if text_body:
                    full_html.append(text_body)
                else:
                    raise Exception ("failed to add text page")
                    

            case "single":
                
                single_body = make_single_body_html(template_dir, found_objs)
                if single_body:
                    full_html.append(single_body)
                else:
                    raise Exception ("failed to add single page")
                

            case "multi":
                multi_body = make_multi_body_html(template_dir, found_objs)
                if multi_body:
                    full_html.append(multi_body)
                else:
                    raise Exception ("failed to add multi pattern page")
                

            case "home":
                home_body = make_home_body_html(template_dir)
                if home_body:
                    full_html.append(home_body)
                else:
                    raise Exception ("failed to add home page")
                
            case "all":
                all_body = make_multi_body_html(template_dir,found_objs)
                if all_body:
                    full_html.append(all_body)
                else:
                    raise Exception ("failed to add all images page")
                
            
            case _:
                raise Exception ("page type not recognised")
            
    
    #--------------------- footer --------------------------------------

    footer = make_footer_html(template_dir, library)
    if footer:
        full_html.append(footer)
    else:
        raise Exception ("failed to add footer")   
    
    #--------------------- tail ------------------------------------------

    tail = make_tail_html(template_dir)
    if tail:
        full_html.append(tail)

    #--------------- join all the components into one string -----------------
    full_html_string = "\n".join(full_html)

    # to put background on homepage only need to make the body of the home page selectable
    if page_type == "home":
        full_html_string = full_html_string.replace('<body','<body class="home-page">')

    
    html_file_name = output_files[page_type]
    output_path = os.path.join(output_dir, html_file_name)
    result = write_html_file(output_path,full_html_string)

    if result == "Successful":
        #print(f"html file successfully written to {html_file_name}")
        return "Success"
    else:
        raise Exception ("html not written successfully")

#---------------------------- File I/O --------------------------------------------------

def read_template_html(file_path):
    
    try:
        with open(file_path,"r") as f:
            content = f.read()
    except Exception as e:
        raise Exception (f"{file_path} cannot be read, error {e}")
    return content
    

def write_html_file(dest_path, html_content):
    try: 
        with open(dest_path, 'w') as file:
            file.write(html_content)
            return "Successful"
    except Exception as e:
        raise Exception ("writing to the file failed")
    
#----------------------- Replace placeholders in the sections with appropriate information ----------------------

def make_head_html(template_dir):
    head_path = os.path.join(template_dir,"head.html")
    head = read_template_html(head_path)
    return head

def make_header_html(template_dir, header_text):
    header_path = os.path.join(template_dir,"header.html")
    header = read_template_html(header_path)
    if header:
        header = header.replace("{{header_info}}", header_text)
    return header

def make_nav_html(template_dir):
    nav_path = os.path.join(template_dir,"navigation.html")
    nav = read_template_html(nav_path)
    return nav

def make_single_body_html(template_dir, found_objs):
    #outer template
    single_body_path = os.path.join(template_dir,"single_pattern_body.html")
    outer_body = read_template_html(single_body_path)
    #inner template for each image
    inner_body_path = os.path.join(template_dir,"pattern_only.html")
    inner_body = read_template_html(inner_body_path)

          
    final_body = f'<div class="num-results"><p>There are {len(found_objs)} results</p></div>'
    for obj in found_objs:
        single_body = outer_body.replace("{{Pattern_Name}}",obj.name)
        # for each pattern there can be multiple images
        image_strings = obj.make_image_strings()
        image_tag = '{{image_path}}'    
        all_image_string = ''
        html_strings = []
        for image_string in image_strings:
            single_image_html = inner_body.replace(image_tag,image_string)
            single_image_html = single_image_html.replace("{{text}}","")
            single_image_html = single_image_html.replace("{{pattern_link}}","")
            html_strings.append(single_image_html)
        all_image_string = "\n".join(html_strings)
        all_images_tag = '{{images}}' # into single_pattern_body
        single_body = single_body.replace(all_images_tag,all_image_string)

        # list of properties
        main_text = ""
        prop_list = obj.list_of_properties()
        for prop in prop_list:
            main_text += f'<p>{prop}</p>'
        single_body = single_body.replace("{{main_text}}",main_text)
        link_string = obj.make_dropbox_links_html()
        single_body = single_body.replace("{{dropbox_pattern_link}}",link_string)
        final_body += single_body
    
    return final_body

def make_multi_body_html(template_dir, found_objs):
    
    #outer template
    outer_body_path = os.path.join(template_dir,"multi_pattern_body.html")
    outer_body = read_template_html(outer_body_path)
    #inner template per pattern
    inner_body_path = os.path.join(template_dir,"pattern_only.html")
    inner_body = read_template_html(inner_body_path)
    
    # repeat the inner template and then insert into the outer template
    multi_body = ""
    patterns = []
    for obj in found_objs:
        obj_string = inner_body
        image_strings = obj.make_image_strings()
        #for each pattern just display the first image
        obj_string = obj_string.replace("{{image_path}}",image_strings[0])
        obj_string = obj_string.replace("{{text}}",obj.name)
        # eventually this link open a pattern details page for that pattern, not implemented yet
        link_string = f'<a href="#">Pattern Details</a>'
        obj_string = obj_string.replace("{{pattern_link}}",link_string)
        patterns.append(obj_string)

    pattern_string = "\n".join(patterns)
    multi_body = outer_body.replace("{{patterns}}", pattern_string)
    summary_string = f"There were {len(found_objs)} matches"
    multi_body = multi_body.replace("{{result_summary}}", summary_string)
    return multi_body

def make_text_body_html(template_dir,library):
    text_body_path = os.path.join(template_dir,"text_body.html")
    text_body = read_template_html(text_body_path)
    
    key_list_html = ""
    for key in library.keys:
        key_list_html += f'<li>{key} </li>'
    text_body = text_body.replace('{{key_list}}', key_list_html)
    
    info_string =  library.info_string()
    text_body = text_body.replace('{{main_text}}', info_string)

    type_list_html = ""
    for t in library.types:
        type_list_html += f'<li>{t} </li>'
    text_body = text_body.replace('{{type_list}}', type_list_html)
    return text_body

def make_home_body_html(template_dir):
    home_body_path = os.path.join(template_dir,"home_body.html")
    home_body = read_template_html(home_body_path)
    return home_body


def make_footer_html(template_dir, library):
    footer_path = os.path.join(template_dir,"footer.html")
    footer = read_template_html(footer_path)
    library_name = library.name
    footer = footer.replace ("{{csv_name}}",library_name)
    return footer

def make_tail_html(template_dir):
    tail_path = os.path.join(template_dir,"tail.html")
    tail = read_template_html(tail_path)
    return tail

def make_blank_body(template_dir, message):
    blank_body_path = os.path.join(template_dir,"blank_body.html")
    blank_body = read_template_html(blank_body_path)
    blank_body = blank_body.replace("{{reason}}", message)
    return blank_body









