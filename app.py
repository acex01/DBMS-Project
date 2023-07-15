import pyinputplus as pyip
import mysql.connector
import random
import time

# establish connection to the database


context = mysql.connector.connect(
    user="root", password="root", port="3306", database="mydb")


def get_wallet(phone_number):
    query = """select customer.Wallet from customer
    where C_Phone_number = %s
    limit 1;"""
    cursor = context.cursor(dictionary=True)
    cursor.execute(query, (phone_number['C_Phone_Number'],))
    balance = cursor.fetchall()
    return balance


def update_driver(phone_number, revenue, city):
    cursor = context.cursor(dictionary=True)
    revenue_query = "UPDATE drivers SET Revenue = Revenue + %s WHERE D_Phone_number = %s"
    location_query = "UPDATE drivers SET Cities_name = %s WHERE D_Phone_number = %s"
    cursor.execute(revenue_query, (revenue, phone_number))
    print(cursor.rowcount, "record(s) updated in revenue.")
    cursor.execute(location_query, (city, phone_number))
    print(cursor.rowcount, "record(s) updated in location.")
    context.commit()


def update_wallet(phone_number, cost):
    query = """update customer ##update wallet
    set Wallet = Wallet - %s
    where C_Phone_number = %s;"""
    cursor = context.cursor(dictionary=True)
    cursor.execute(query, (cost, phone_number,))
    context.commit()
    print(f"Deducted {cost} from wallet \n")


def recharge_wallet(phone_number, cost):
    query = """update customer ##update wallet
    set Wallet = Wallet + %s
    where C_Phone_number = %s;"""
    cursor = context.cursor(dictionary=True)
    cursor.execute(query, (cost, phone_number,))
    context.commit()
    print(f"Chadge wallet by {cost} Rs\n")


def get_customer(phone_number):
    """Retrieve customer information from the database based on the phone number."""
    cursor = context.cursor(dictionary=True)
    query = "SELECT * FROM CUSTOMER WHERE C_Phone_Number=%s  limit 1"
    cursor.execute(query, (phone_number,))
    customer = cursor.fetchall()

    return customer


def get_trips_by_customer(phone_number):
    """Retrieve a list of trips taken by the customer."""
    cursor = context.cursor(dictionary=True)
    query = "select * from trips where Trip_ID in (select Trips_trip_ID from customer where C_Phone_number =%s);"
    cursor.execute(query, (phone_number,))
    trips = cursor.fetchall()

    return trips


def get_driver(location):
    """Retrieve an available driver for the specified location."""
    cursor = context.cursor(dictionary=True)
    query = """ select *
                from drivers
				where drivers.Cities_name = %s
                order by rating desc
                limit 1;"""
    cursor.execute(query, (location,))
    driver = cursor.fetchall()
    return driver

# def adminlogin():
#     print("Admin Login")
#     username = pyip.inputStr("Enter username: ")
#     password = pyip.inputStr("Enter password: ")
#     if username == "admin" and password == "admin":
#         print("Login Successful")
#         admin()
#     else:
#         print("Invalid username or password")
#         adminlogin()
# def admin():
#     print("Admin Menu")
#     print("1. Add Driver")
#     print("2. Add Customer")
#     print("3. Add Car")
#     print("4. Add City")
#     print("5. Add Trip")
#     print("6. Exit")
#     choice = pyip.inputInt("Enter your choice: ")
#     if choice == 1:
#         add_driver()
#     elif choice == 2:
#         add_customer()
#     elif choice == 3:
#         add_car()
#     elif choice == 6:
#         print("Exiting...")
#         exit()
#     else:
#         print("Invalid choice")
#         admin()

# def add_driver():
#     print("Add Driver")
#     name = pyip.inputStr("Enter name: ")
#     phone_number = pyip.inputInt("Enter phone number: ")
#     rating = pyip.inputInt("Enter rating: ")
#     revenue = pyip.inputInt("Enter revenue: ")
#     city = pyip.inputStr("Enter city: ")
#     cursor = context.cursor()
#     query = "INSERT INTO DRIVERS(D_Phone_number, D_Name, Rating, Revenue, Cities_name) VALUES (%s, %s, %s, %s, %s)"
#     cursor.execute(query, (phone_number, name, rating, revenue, city))
#     context.commit()
#     print("Driver added successfully")
#     admin()
# def add_customer:
#     print("Add Customer")
#     name = pyip.inputStr("Enter name: ")
#     phone_number = pyip.inputInt("Enter phone number: ")
#     wallet = pyip.inputInt("Enter wallet: ")
#     cursor = context.cursor()
#     query = "INSERT INTO CUSTOMER(C_Phone_number, C_Name, Wallet) VALUES (%s, %s, %s)"
#     cursor.execute(query, (phone_number, name, wallet))
#     context.commit()
#     print("Customer added successfully")
#     admin()
# def add_car():
#     print("Add Car")
#     car_id = pyip.inputInt("Enter car ID: ")
#     model = pyip.inputStr("Enter model: ")
#     color = pyip.inputStr("Enter color: ")
#     cursor = context.cursor()
#     query = "INSERT INTO CARS(Car_ID, Model, Color) VALUES (%s, %s, %s)"
#     cursor.execute(query, (car_id, model, color))
#     context.commit()
#     print("Car added successfully")
#     admin()

def create_trip(driver_phone, start_location, end_location, cost, glob):
    """Create a new trip in the database."""
    new_query = '''insert into trips values(123456789,500,'start time','1:11:2',(select temp.Cities_name from temp),'destination',(select temp.D_Phone_number from temp));'''
    cursor = context.cursor()
    query = "INSERT INTO TRIPS(Trip_ID,Cost,StartTime,Duration,PickUpLocation,DropLocation,Drivers_D_Phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (glob, cost, '08:15:30', '0:0:15', start_location,
                   end_location, driver_phone))  # starttime and duration
    context.commit()


def create_customer(phone_number, trip_id, driver_phone_number):
    cursor = context.cursor()
    query1 = '''SELECT * FROM CUSTOMER
                   where
                     C_Phone_Number = %s
                     LIMIT 1'''
    # Fetch the first customer in the database
    cursor.execute(query1, (phone_number,))
    first_customer = cursor.fetchall()[0]

    # Get the parameters from the first customer
    name = first_customer[2]
    phone_number = first_customer[0]
    email = first_customer[1]
    wallet = first_customer[3]
    rating = first_customer[4]
    query2 = """select Car_number from drivers where D_Phone_number=%s;"""
    cursor.execute(query2, (driver_phone_number,))
    car_number = cursor.fetchall()[0][0]

    # Add the new customer row to the database
    query = """INSERT INTO CUSTOMER(C_Phone_Number, C_email_ID, C_Name, Wallet, rating, Trips_Trip_ID, 
                                    Drivers_D_Phone_number, Drivers_D_Phone_number1, Car_number)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (phone_number, email, name, wallet, rating, trip_id,
                   driver_phone_number, driver_phone_number, car_number))
    context.commit()


def main():
    # admin = pyip.inputMenu(['Admin', 'Customer'], numbered=True)
    # if admin == 'Admin':
    #     admin_login()
    phone_number = pyip.inputStr('Enter customer phone number: ')
    customer = get_customer(phone_number)[0]
    print('Welcome', customer['C_Name'])

    while True:
        glob = random.randint(100, 100000)
        choice = pyip.inputMenu(
            ['View Trip History', 'Book a Trip', 'Add balance to wallet', 'Exit'], numbered=True)

        if choice == 'View Trip History':
            trips = get_trips_by_customer(phone_number)
            print(
                'Trip_ID \t StartTime \t Duration \t Cost \t PickUpLocation \t DropLocation')
            for trip in trips:
                print('%s \t %s \t %s \t %s \t %s \t %s', trip['Trip_ID'], trip['StartTime'], trip['Duration'],
                      trip['Cost'], trip['PickUpLocation'], trip['DropLocation'])
                time.sleep(1)

        elif choice == 'Book a Trip':
            start_location = pyip.inputStr('Enter starting location: ')
            end_location = pyip.inputStr('Enter end location: ')
            cost = random.randint(120, 500)

            # get available driver for the start location
            driver = get_driver(start_location)
            time.sleep(3)
            if driver:

                if (get_wallet(customer)[0]['Wallet'] > cost):
                    create_trip(driver[0]['D_Phone_number'],
                                start_location, end_location, cost, glob)
                    print('Trip booked successfully')
                    update_driver(
                        driver[0]['D_Phone_number'], cost, end_location)
                    print(phone_number, "\n Driver Phone Number :",
                          driver[0]['D_Phone_number'], "\n From : ", start_location, "\n To", end_location, "\nCost : ", cost)

                    recharge_wallet(phone_number, -cost)
                    create_customer(phone_number, glob,
                                    driver[0]['D_Phone_number'])
                else:
                    print("Hatt gareeb \n")
            else:
                print('No driver available for the start location')

        elif choice == 'Add balance to wallet':  # adding money to the wallet
            balance = int(input("Enter the amount to be added : "))
            time.sleep(3)
            recharge_wallet(phone_number, balance)

        elif choice == 'Exit':
            break


if __name__ == '__main__':
    main()
