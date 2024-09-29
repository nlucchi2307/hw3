# 1) 
def triple(x):
    return x * 3

result = triple(5)
print(result)

# 2)
def subtract(a, b):
    return a - b

result2 = subtract(8, 10)
print(result2)

# 3) 
def dictionary_maker(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict

tuples_list = [('price1', 100), ('price2', 150)]
result = dictionary_maker(tuples_list)
print(result) 