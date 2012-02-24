#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name)
    print "hello,", name.lower()



# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    #checking type
    if type(w) != int or type(h) != int or w < 1 or h < 1:
        print "Error: Invalid Dimensions"
        return

    #first line
    if w == 1:
        print "+"
    else:
        print "+" + "-"*(w-2) + "+"
    # mid
    for i in range(h-2):
       if w == 1:
           print "|"
       else:
           print "|" + " "*(w-2) + "|"
    #final line
    if h > 1:
        if w == 1:
            print "+"
        else:
            print "+" + "-"*(w-2) + "+"




# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

def tree(branch=5):
    tr = []
    tr.append("    *")
    tr.append("    ^")
    tr.append("   ^-^")
    tr.append("  ^-^-^")
    tr.append(" ^-^-^-^")
    tr.append("^-^-^-^-^")
    tr.append("   | |")
    tr.append("   | |")

    return "\n".join(tr)
