# PyPerfectTable
This is my first lib ever written in python and first project uploaded to github
usage:

add_title() <- adds title of the table
arguments:
list of string words
NOTE: Table cannot be created without title

add_stroke() <- adds stroke to the table
arguments:
list of string words

===================================================================
edit_stroke() <- function to edit any stroke
arguments:
string arguments:

    stroke position ; position of colomn u wanna edit : word

example:

		0; 1: Hello World; 2: cake
===================================================================
edit_title() <- function to edit title
arguments:
string arguments:

     position of colomn u wanna edit : word

example:

		1: Hello World; 2: cake

===================================================================
remove_stroke() <- function to remove any stroke
arguments:
int (stroke position)

if no arguments provided - will remove all strokes
===================================================================
print_title() <- function to return string
arguments:
[from(int),to(int)]

if no arguments provided - will print all colomns

will return string
===================================================================
print_stroke() <- function to return string
arguments:
[from(int),to(int)]

if no arguments provided - will print all colomns
will return string
===================================================================
print() <- function to print all colomns (title and strokes)
arguments:
[from(int),to(int)]

if no arguments provided - will print all colomns
===================================================================
add_argument() <- function to add arguments to colomns
arguments:
string arguments:

    position of colomn : parameter

example:

		1: %; 2: $
===================================================================
stroke_active() <- will show progress bar
arguments:
condition (bool), position (int) , percents (int), length (int)

example:

True,0,100,10
===================================================================
temp_save() <- function to save table and to have ability to load it back
arguments:
filename (str)
===================================================================
save() <- function to save table in normal way (CANNOT BE USED TO LOAD IT BACK)
