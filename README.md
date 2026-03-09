Patterns is designed to work with a csv input file created from a database of patterns with fields containing various attributes of the patterns, images and pattern links. A pattern object is created for each of the records in the library and the first line (column heading) is used to define the attributes of the pattern forming a set of keys. A library object is created that contains general information about the pattern collection and a list of all the pattern objects. The parent Pattern class contains generic information and methods suitable for all pattern libraries. Child pattern classes are then defined containing more specific attributes and methods for particular data structures. This approach keeps all the data associated with a pattern or a library together simplifying the transfer of parameters into function calls and preventing duplication of code. It is very simple to add another child pattern class to adapt to different field structures.

This program has a command line interface with both mandatory and optional arguments. The output is in the form of a set of static webpages displaying various outputs chosen by the optional input parameters and a summary page showing the information about the library.

## **Usage**

### Mandatory arguments:

- `<craft_type>`: Finds a pattern with a matching pattern name
- `<csv_filepath>`: Finds pattern with matching pattern type <craft_type>

### Optional Commands Available:

- `-s <search_term>`: Finds a pattern with a matching pattern name
- `-t <search_term>`: Finds pattern with matching pattern type
- `-a`: Generates a grid of all pattern in the library

### **Examples:**

```
python3 ./src/main.py knit ./inputs/input.csv # mandatory arguments

python3 ./src/main.py knit ./inputs/input.csv -s "pattern_search_term" -t "type_search_term” -a # all optional arguments

```

### Other parameters

Within [main.py](http://main.py) a number of parameters are set up including a template directory, an output directory, a dictionary of html filenames for the outputs and a library name.

## Settings details and resulting outputs

The mandatory program arguments are the craft type and the input csv filepath. The craft type is used as a tag to make sure the correct pattern objects are created and that the key list is translated into the correct information for output. A new table structure can be incorporated by creating a new Pattern type object with inherited methods from the parent and  and more specific attributes and method suited to that particular data structure within the child Pattern type object 

The collection information page is always available and contains a list of both the keys and pattern type to assist in setting up the program with data from a new table with a different structure. The program was designed to extract the key list and pattern types from the data itself and so adapts to different data structures.

A pattern name search is executed when the command line switch -s is used and a search term given. This displays the resulting pattern with images, information about the pattern and a pattern link to a locally stored pattern library.

The pattern data this is designed to work with has a pattern type attribute. A type search can be executed using the switch -t and a search term and this will find all the patterns that include a pattern type specified. The resulting matches are displayed as a grid of  patterns, each with an image and pattern name. 

The final optional output , -a, creates a grid containing all the patterns in the collection with an image and a pattern name.

## Output details

The output html files are arranged in the doc directory to enable hosting by github. There is a shared stylesheet. The location of the output files is specified in the body of main.py.

The html pages are generated using some basic local template files for each part of the pages to minimise duplication and ensure consistency across the pages.

## Future development

The program is designed as a first stage standalone project with a plan to extend it to include a more interactive web app and improved search functionality.

The current command line interface would be replaced by an interactive web app. The page designs are very basic and written by hand in html. A more aesthetically pleasing website could be designed given more html/css knowledge and the possible use of templating tools.

The current form requires the data to be input and processed every time a search is carried out. It will be much more efficient for large libraries by processing once and then using a dynamic search from the web interface to carry out pattern and type searches. 

The data handling may progress to using the csv data to populate a database allowing linkage between pattern and designer datasets. There are only simple searches available at the moment but a more complex set of searches may be possible by using SQL queries on such a database.

## **Installation**

To set up and run this project, follow these steps:

1. Clone the repository:

```
git clone https://github.com/fds66/patterns
```

1. Navigate to the project directory:

```
cd patterns
```

1. Provide a csv file containing the fields header in the first line and the record of a pattern in each subsequent line. Ensure any images linked either have a full image directory listed in [main.py](http://main.py) or are stored locally in the image directory along with the html pages.
2. To use a different table structure, set up a custom pattern child class to use the keys in that data.

