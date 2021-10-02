# PyPerfectTable
This is my first lib ever written in python and first project uploaded to github
usage:

add_title()
===
adds title of the table

	add_title("First Colomn","Second Colomn")
NOTE: Table cannot be created without title

add_stroke()
===
adds stroke to the table

	add_stroke("Hello world",5,10)
edit_stroke()
===
function to edit any stroke

how to use: `stroke position ; position of colomn u wanna edit : word`

	edit_stroke("0;0:Hello World;1: Cake")

edit_title()
===

function to edit title

how to use: `position of colomn u wanna edit : word`

example:

		1: Hello World; 2: cake

remove_stroke()
===

function to remove any stroke

`int (stroke position)`
example:

	remove_stroke(0)

if no arguments provided will remove all strokes

print_title()
===

function to return string

example:

	print_title()
or:

	print_title([0])
or:

	print_title([0,1])

`print(object.print_stroke())`
aditional arguments: `[from(int),to(int)]`
if no arguments provided will print all colomns

print_stroke()
===


arguments: `[from(int),to(int)]`

example:

	print_stroke()
or:

	print_stroke([0])
or:

	print_stroke([0,1])

`print(object.print_stroke())`

if no arguments provided will print all colomns
will return string

print()
===
function to print all colomns (title and strokes)

arguments:
[from(int),to(int)]

if no arguments provided - will print all colomns
add_argument() <- function to add arguments to colomns
arguments:
string arguments:

    position of colomn : parameter

example:

		1: %; 2: $

stroke_active()
===

will show progress bar
arguments: `condition (bool), position (int) , percents (int), length (int)`

example:

	stroke_active(True,0,100,10)

temp_save()
===

function to save table and to have ability to load it back

arguments: `filename (str)`

save()
===

function to save table in normal way (CANNOT BE USED TO LOAD IT BACK)

parameters:
===

```
self.default_cursor = ' <--'
self.WHITE = 15 #Default white color
self.red_to_green = (88,124,160,196,202,208,172,178,148,46) #color pallete
self.enable_color = False
self.enable_numbers = False
self.enable_cursor = False
```
