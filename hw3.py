# 1)
def car_at_light(light):
    if light == "red":
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise Exception(f"Undefined instruction for color:{light}")

# testing the defined exception 
result=car_at_light("blue")
print(result)
    

# 2) 
def safe_subtract(a,b):
    try:
        return a - b
    except TypeError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# testing the defined exception 
result=safe_subtract("a","b")
print(result)


# 3) 
#EAFP approach 
def retrieve_age_eafp(people):
    try:
        current_year = 2024
        birth_year = people['birth']
        return current_year - birth_year
    except KeyError:
        return "Birth year not available"
    except TypeError:
        return "Birth year is not valid"
people = {
    'person1': {'name': 'John', 'last_name': 'Doe', 'birth': 1987},
    'person2': {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}}
for key, person in people.items():
    print(f"{key} (EAFP):", retrieve_age_eafp(person))
  
# LBYL approach  
def retrieve_age_lbyl(person):
    current_year = 2024
    if 'birth' in person and isinstance(person['birth'], int):
        return current_year - person['birth']
    else:
        return "Birth year not available or invalid"
people = {
    'person1': {'name': 'John', 'last_name': 'Doe', 'birth': 1987},
    'person2': {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}}
for key, person in people.items():
    print(f"{key} (LBYL):", retrieve_age_lbyl(person))

4.
import pandas as pd

def read_data_with_pandas(filename="data.csv"):
    try:
        data = pd.read_csv(filename)  
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        
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
