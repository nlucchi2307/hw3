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