"""The Christmas Tree Creator is a program that generates an ASCII art Christmas tree using asterisks, including a stump at the bottom of the tree made
using the pipe (|) symbol. It asks the user to enter the height of the Christmas tree they’d like to create. Try generating a few Christmas trees using
the finished program below, and then we’ll show you how to create your own."""

def draw_christmas_tree(height):
    row = 1
    height = int(height)
    while row <= height:
        spaces = height-row
        stars = 2*row-1
        print(" " * spaces + "*" * stars)
        row += 1
#draw_christmas_tree(10)

def draw_stump(height):
    height = int(height)
    stump_width = int(height/3)
    stump_height = int(height/3)
    spaces = int((2 * height - stump_width)/2)
    row = 0
    while row <= stump_height:
        #print(stump_width)
        print(" " * spaces + "|" * stump_width)
        row += 1

tree_height = input("Enter the height of the Christmas tree: ")

draw_christmas_tree(tree_height)
draw_stump(tree_height)


