import csv
import os


def create_employees():
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'employees_data.csv'), 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
        return data


def create_customers():
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'customers_data.csv'), 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
        return data


def create_orders():
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'orders_data.csv'), 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
        return data

# ty1 = create_employees()
# ty2 = create_customers()
# ty3 = create_orders()
# print(ty3)