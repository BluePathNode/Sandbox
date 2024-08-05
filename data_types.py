#---------------------------------------------#
# String data types (with a Star Wars flavor!)
#---------------------------------------------#

# literal assignment
first = "Obiwan"
last = "Kenobi"

#-------------------------------------------#
# select and crtl / to comment or uncomment!
#-------------------------------------------#

# # Check types
# print(type(first))
# # Is it a 'string'
# print(type(first) == str)
# # Is it an instance of ?
# print(isinstance(first, str))

#-------------------------------

# # Constructor function
# saber = str("Blue lightsaber")
# # Check types
# print(type(saber))
# # Is it a 'string'
# print(type(saber) == str)
# # Is it an instance of ?
# print(isinstance(saber, str))

#----------------------------

# Concatenation
fullname = first + " " + last 
print(fullname)

#fullname += "!"

print("")

#-----------------------------

# casting a number to a string
amount = str(90)
# # check the data type then print the data type in this case <class 'str'> for string
# print(type(amount))
# # print the number casted
# print(amount)



statment = "My lightsaber accuracy against blaster's is in the high " + amount + "'s!"
print(statment)


#-------------------------------------------------------------------------------------

multiline = """

Since my arrival on Tatooine,       
                   I have had to destroy at least    
                                         3692 imperial probes!
droids... :/
"""

print(multiline)

#------------------------------------------------------------------------------------

# escaping special characters
sentance = 'I\'m back in my cave.\t There were Sand people!\n\nWhere\'s my \\lightsaber located?'
print(sentance)



# string methods

# print(first)
# print(first.lower()) # no caps
# print(first.upper()) # ALL CAPS 
# print(first)



# # Capitalizes every letter in the text
# print(multiline.title())
# # replace a string with another string
print(multiline.replace("Tatooine", "Geonosis").replace("imperial probes", "battledroids").replace("3692", "14589"))
# # print out the original with no change
# print(multiline)

#-------------------------------------------------------------------------------------------.

# # add whitespace

# # check the length of spaces multiline happens to take up
# print(len(multiline))
# # Add more whitespace to the end
# multiline  +=  "                                   "
# # Add more white space to the beggining and concatenate to whats already there
# multiline =  "             "  +  multiline
# # Check the length again
# print(len(multiline))

#-----------------------------------------------------------------------------------

# remove whitespace

# # check length len whitespace is not visible 
# # Remove whitespace
# print(len(multiline.strip()))
# # remove from the left side
# print(len(multiline.lstrip()))
# # remove from the right side
# print(len(multiline.rstrip()))

#-----------------------------------------

# Build a Menu 

title = "Jedi Credentials".upper()

print(title.center(30, "-"))
print(fullname.ljust(22, ".") + "Master".rjust(8))
print("Lightsaber".ljust(24, ".") + "Blue".rjust(6))
print("Accuracy".ljust(26, ".") + amount.rjust(4))


