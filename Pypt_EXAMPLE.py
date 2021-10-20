import perfect_table as PT

table = PT.Table()#creating an object

#>ADDING

#First step is to add a title
table.add_title("Hello","and")

#You can add it in one line , or later
table.add_title("Welcome")

#Next we can add strokes
table.add_stroke("String","Or even a number",2)

#or we can add less parameters than title

table.add_stroke("first","second",[1,5,6])#next will be empty

#>

#we can enable colors
table.enable_color = False #by default everything will be white color

#>EDITING

#we can edit any stroke or any title
"""uncomment this section to see the changes
table.edit_stroke("0;0:firstA;1:secondB")
table.edit_stroke("1;1:firstC;0:secondD")
table.edit_title("0:Hi;1:good to see you")
"""

#>>additional information

#if we need to change colors for strokes and title simply use "c":
table.edit_stroke("0;c:1,5,2")
table.edit_title("c:1,2,3")

#>


#>Other

#we can enable cursor (it will appear at the first line)
table.enable_cursor = True

#and move it by 1 step
table.cursor.move(1)

#>


#we can print all strokes and title line by line
table.print()

#or print individual (the functions will return string)
print(table.print_title())
print(table.print_stroke(1))

#also we can print individual colomn
table.print([0])#for the first colomn
#or
table.print([1])#for the second
#or we can print range of colomns
table.print([0,1])
table.print([1,2])
#also it works with individual elements
print(table.print_stroke(0,[0,1]))
print(table.print_title([0,1]))