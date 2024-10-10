# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

#This code is used to to add the doubled value of each element to total_double_sum. However, it is currently adding the original element (elem), not the doubled value.
#The corrected version of the code block is the following:

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

#The code will only assign the last iteration's value (Groot_Groot) to strings producing "Groot_Groot".Considering that the goal is to concatenate all strings with underscores (e.g., "I_am_Groot"), this logic needs to be fixed.
#The corrected version of the code block is the following:

strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + "_"
strings = strings.rstrip('_') # This removes the trailing underscore


### (c) Careful!
j=10
while j > 0:
   j += 1

#This loop will run forever because because j is being incremented (j += 1) every time the loop runs. Since j starts at 10 and keeps getting larger, it will never be less than or equal to zero, which means the condition j > 0 will always be true. As a result, the loop never stops.
#The corrected version of the code block is the following:

j=10
while j > 0:
   j -= 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

#Initializing productory to 0 will result in the product always being zero since anything multiplied by zero remains zero. Instead should be initialized to 1.
#The corrected version of the code block is the following:

productory = 1
for elem in [1, 5, 25]:
    productory *= elem
