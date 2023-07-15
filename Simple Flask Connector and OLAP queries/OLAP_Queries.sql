##Driver of the month choose karna hai

select D_Phone_Number,rating,revenue
from drivers
group by revenue,rating,D_Phone_Number;

##kis time par kitna paisa kamaya

select starttime,sum(cost) as total_earnings
from trips
group by starttime
with rollup;

#selecting drivers with a high rating

select D_Phone_Number,rating
from drivers
having rating > 4;

#total frequencies of the places visited

select address,sum(frequency)
from locations
group by address
with rollup;

#Sums up the revenues of different drivers under 2 different admins to show which admin is doing a better job

SELECT
    Cities_Name,
    SUM(CASE WHEN Admin_Employee_ID = 1 THEN Revenue ELSE 0 END) AS Admin1,
    SUM(CASE WHEN Admin_Employee_ID = 2 THEN Revenue ELSE 0 END) AS Admin2
FROM
    drivers
GROUP BY
    Cities_Name;