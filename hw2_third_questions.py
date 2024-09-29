# 7) 
def total_registered_cases(data, country):
    return sum(data[country])
data = {
    'Spain': [4, 8, 2, 0, 1],
    'France': [2, 3, 6],
    'Italy': [6, 8, 1, 7]}
spain_total = total_registered_cases(data, 'Spain')
print(f"Total Registered cases in Spain: {spain_total}")

# 8) 
def total_registered_cases_per_country(data):
    total_cases = {}
    for country, cases in data.items():
        total_cases[country] = sum(cases)
    return total_cases
data = {
    'Spain': [4, 8, 2, 0, 1],
    'France': [2, 3, 6],
    'Italy': [6, 8, 1, 7]}
totals = total_registered_cases_per_country(data)
print(f"Total Registered cases per country: {totals}")

# 9) 
def country_with_most_cases(data):
    max_cases = 0
    country_with_max_cases = None
    for country, cases in data.items():
        total_cases = sum(cases)
        if total_cases > max_cases:
            max_cases = total_cases
            country_with_max_cases = country
    return country_with_max_cases
data = {
    'Spain': [4, 8, 2, 0, 1],
    'France': [2, 3, 6],
    'Italy': [6, 8, 1, 7]}
country_most_cases = country_with_most_cases(data)
print(f"The country with the highest number of cases is: {country_most_cases}")
