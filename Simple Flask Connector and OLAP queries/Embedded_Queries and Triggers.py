import mysql.connector

context = mysql.connector.connect(user = "root",password = "root",port = "3306",database = "mydb")

cursor = context.cursor(dictionary=True)

cursor.execute('''SELECT a.name,b.name
FROM cities a
CROSS JOIN cities b
WHERE a.name != b.name;''')

c = cursor.fetchall()

print(c)

cursor.execute('''UPDATE drivers
SET Admin_Employee_ID = 2
WHERE D_Phone_Number = 9811443772;''')

c = cursor.fetchall()

print(c)

context.close()

##trigger 1:
## The functionality of this trigger is when a car is unavailable
## and its services cannot be provided we must remove the respective
## driver from the table as well.

# delimiter $$
# CREATE TRIGGER Car_go_driver_go
# AFTER DELETE
# ON car
# FOR EACH ROW
# BEGIN
# 	DELETE FROM drivers WHERE drivers.Car_number NOT IN (SELECT number FROM cars);
# END$$

##trigger 2:
## In case a driver is fired then
## we must remove their car from the database as well
## Hence we create a trigger for the same

# delimiter $$
# CREATE TRIGGER Driver_go_car_go
# AFTER DELETE
# ON drivers
# FOR EACH ROW
# BEGIN
# 	DELETE FROM cars WHERE number NOT IN (SELECT Car_number FROM drivers);
# END$$



# Embedded Query for Front end

# DELETE car, drivers
# FROM car
# INNER JOIN drivers ON car.number = drivers.car_number
# WHERE drivers.D_Phone_number = '0504020563';