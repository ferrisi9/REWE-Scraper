import csv
import pandas as pd

filename = "Rewe_prices_2020-12-20.csv"
filename_1 = "Rewe_prices_2020-12-29.csv"

dict = {}
dict_01 = {}
shared_dict = {}


def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    # else:
    #    continue
    # As key is not in dict,
    # so, add key-value pair
    # dict_obj[key] = value


def create_dict(file, dict):
    with open(file, 'r') as data:
        for row in csv.DictReader(data, delimiter=';'):
            try:
                dict[row['Product_Name']] = [float(row['Price'])]
            except Exception:
                continue


def create_shared_dict(file_01, file_02, dict):
    create_dict(file_01, dict)
    shared_dict = dict
    with open(file_02, 'r') as data:
        for row in csv.DictReader(data, delimiter=';'):
            try:
                append_value(shared_dict, row['Product_Name'], float(row['Price']))
            except Exception:
                continue
        #for line in data:
        #    line = line.split(';')
        #    if len(line) < 6:
        #        continue
        #    else:
        #        append_value(shared_dict, line[4], line[5])


def change_price(shared_dict):
    for key, value in shared_dict.items():
        if len(value) > 1:
            if value[0] == value[1]:
                same_price[key] = value[1]
            elif value[0] < value[1]:
                more_expensive[key] = round((value[1] - value[0]), 4)
            else:
                less_expensive[key] = round((value[0] - value[1]), 4)
        else:
            continue



create_dict(filename, dict)
# print(dict)

# create_dict(filename_1, dict_01)

create_shared_dict(filename, filename_1, shared_dict)
print(shared_dict['Salatgurke'])

more_expensive = {}
less_expensive = {}
same_price = {}

#for item in shared_dict.values():
#    print(type(item))

change_price(shared_dict)

print(len(more_expensive))
print(less_expensive)
print(len(same_price))


# comparison = pd.DataFrame(zip(item_name, item_price), columns=['ItemName', 'Price'])
# comparison_1 = pd.DataFrame(zip(item_name_1, item_price_1), columns=['ItemName', 'Price'])
