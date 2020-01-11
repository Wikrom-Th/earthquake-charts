# rename the known pan-asia regions into countries 
import csv
import sys

# countries that is considered in this project (in pan-asia)
countries = ["China", "Taiwan", "Japan", "South Korea", "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", 
            "Myanmar/Burma", "Philippines", "Singapore", "Thailand", "Timor-Leste", "Vietnam", "Bangladesh", 
            "Bhutan", "India", "Nepal", "Sri Lanka", "Micronesia", "Papua New Guinea"]

# takes the input for the region from the user
print("Please input the region that you are interested in assigning countries:")
input_region = str(input())

# country_in_list is a boolean which will be use to help check whether that country is in the countries list or not
country_in_list = False

# takes the input for the country from the user
print("Please input the country you want to assign the region to:")
input_country = str(input())

# only pass this part when the country input is in the countries list
while not country_in_list:

    for country in countries:
        if input_country.lower() == country.lower():
            input_country = country
            country_in_list = True
            break

    if not country_in_list:
        print("This input country is not in the list, please put a valid country:")
        input_country = str(input())

# initializing necessary variables to store data
assigning_row = []
other_row = []
count = 0

with open('./eq_data/other_eqs.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if input_region.lower() in row[0].lower():
            print(row[0])
            row[0] = input_country
            assigning_row.append(row)
            count += 1
        else:
            other_row.append(row)

print(f"Total count for the selected region: {count}")
print(f"The regions above will be assigned to the country {input_country}. Do you wish to proceed? [y/n]")

user_continue = str(input())

while True:

    if user_continue.lower() == "y":
        break

    elif user_continue.lower() == "n":
        print("Task cancelled")
        sys.exit()

    else:
        print("Please input either 'y' or 'n'. Do you wish to proceed? [y/n]")
        user_continue = str(input())

with open('./eq_data/pan_asia_eqs.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(assigning_row)


with open('./eq_data/other_eqs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(other_row)