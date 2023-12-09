import psycopg2
from north_data.csv_reader import create_employees, create_customers, create_orders

password = input('Введите свой пароль postgress\n')
table1 = psycopg2.connect(host="localhost", database="north", user="postgres", password=password)


def create_table_employees():
    data1 = create_employees()
    with table1:
        for i in data1:
            if i != data1[0]:
                with table1.cursor() as cursor:
                    cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (i))

def create_table_customers():
    data2 = create_customers()
    with table1:
        for i in data2:
            if i != data2[0]:
                with table1.cursor() as cursor:
                    cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)", (i))


def create_table_orders():
    data3 = create_orders()
    with table1:
        for i in data3:
            if i != data3[0]:
                with table1.cursor() as cursor:
                    cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (i))



if __name__ == '__main__':
    create_table_employees()
    create_table_customers()
    create_table_orders()
