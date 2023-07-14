import sqlite3
import pandas as pd
#This is for creating connection for db
con_db = sqlite3.connect("flight.db")

cur = con_db.cursor()
#These commands will create tables aircraft, flight, trip, pilot
cur.execute(
  "CREATE TABLE IF NOT EXISTS aircraft(aircraft_id INTEGER PRIMARY KEY, aircraft_name TEXT, manufacture_date TEXT, model TEXT, capacity INTEGER)"
)

cur.execute(
  "CREATE TABLE IF NOT EXISTS flight(flight_id INTEGER PRIMARY KEY, flight_name TEXT , source TEXT, destination TEXT, date TEXT, flight_time TEXT, aircraft_id INTEGER, FOREIGN KEY(aircraft_id) REFERENCES aircraft(aircraft_id))"
)

cur.execute(
  "CREATE TABLE IF NOT EXISTS flight_trip(trip_id INTEGER PRIMARY KEY, flight_id INTEGER, FOREIGN KEY(flight_id) REFERENCES flight(flight_id))"
)

cur.execute(
  "CREATE TABLE IF NOT EXISTS pilot(pilot_id INTEGER PRIMARY KEY, pilot_name TEXT, year_of_joining NUMBER, country TEXT, trip_id INTEGER, FOREIGN KEY(trip_id) REFERENCES trip(trip_id))"
)

#These are for inserting values into desired tables

#These for inserting data into aircraft
cur.execute(
  "INSERT INTO aircraft(aircraft_id, aircraft_name, manufacture_date, model, capacity) VALUES(100, 'Air Bird 302', '10-12-2021', 'air plane', 120 )"
)

cur.execute(
  "INSERT INTO aircraft(aircraft_id, aircraft_name, manufacture_date, model, capacity) VALUES(102, 'Air Bird 300', '10-10-2021', 'air bus', 140 )"
)

cur.execute(
  "INSERT INTO aircraft(aircraft_id, aircraft_name, manufacture_date, model, capacity) VALUES(104, 'Air Bus 380', '22-2-2020', 'air bus', 800 )"
)

cur.execute(
  "INSERT INTO aircraft(aircraft_id, aircraft_name, manufacture_date, model, capacity) VALUES(106, 'Boeing 777', '08-12-2018', 'air plane', 400 )"
)

#This is for inserting into flight
cur.execute(
  "INSERT INTO flight(flight_id, flight_name, source, destination, date, flight_time, aircraft_id) VALUES (200, 'Delhi Air', 'Delhi', 'Banglore', '18-12-2022', '20:30', 100)"
)

cur.execute(
  "INSERT INTO flight(flight_id, flight_name, source, destination, date, flight_time, aircraft_id) VALUES (202, 'Banglore Air', 'Banglore', 'Manchester', '20-12-2022', '22:30', 102)"
)

cur.execute(
  "INSERT INTO flight(flight_id, flight_name, source, destination, date, flight_time, aircraft_id) VALUES (204, 'British Air', 'London', 'Banglore', '20-12-2022', '14:30', 104)"
)

cur.execute(
  "INSERT INTO flight(flight_id, flight_name, source, destination, date, flight_time, aircraft_id) VALUES (206, 'London Air', 'Chennai', 'London', '18-12-2022', '06:30', 106)"
)

#This is for inserting into trip
cur.execute(
  "INSERT INTO flight_trip(trip_id, flight_id) VALUES (500, 200)"
)

cur.execute(
  "INSERT INTO flight_trip(trip_id, flight_id) VALUES (502, 202)"
)

cur.execute(
  "INSERT INTO flight_trip(trip_id, flight_id) VALUES (504, 204)"
)

cur.execute(
  "INSERT INTO flight_trip(trip_id, flight_id) VALUES (506, 206)"
)

#This is for inserting into pilot
cur.execute(
  "INSERT INTO pilot(pilot_id, pilot_name, year_of_joining, country, trip_id) VALUES (1124, 'Jenny', 2014, 'Belgium', 500)"
)

cur.execute(
  "INSERT INTO pilot(pilot_id, pilot_name, year_of_joining, country, trip_id) VALUES (1125, 'Sam', 2015, 'India', 502)"
)

cur.execute(
  "INSERT INTO pilot(pilot_id, pilot_name, year_of_joining, country, trip_id) VALUES (1126, 'Jack', 2010, 'United Kingdom', 504)"
)

cur.execute(
  "INSERT INTO pilot(pilot_id, pilot_name, year_of_joining, country, trip_id) VALUES (1127, 'Danny', 2011, 'France', 506)"
)

#This is for inserting data into flight table by user
print("Enter details into Flight Table for inserting")
data1 = input("Enter the flight id :")
data2 = input("Enter Flight name:")
data3 = input("Enter Source:")
data4 = input("Destination:")
data5 = input("Date:")
data6 = input("Time:")
data7 = input("Aircraft ID:")
cur.execute(
  "INSERT INTO flight VALUES(?,?,?,?,?,?,?)",(data1, data2, data3, data4, data5, data6, data7)
)

#This is for updating data
print("pilot data before updating")
for row3 in cur.execute("SELECT * FROM PILOT"):
  print(row3)

cur.execute(
  "UPDATE pilot SET country = 'India' WHERE pilot_id = 1124"
)
print("Pilot data after updating")
for row3 in cur.execute("SELECT * FROM PILOT"):
  print(row3)

#This is for taking user given input for updating flight name with the help of flight id in flight table
data9 = input("Give flight name for updating flight table:")
data8 = input("Give flightid to update flight table with name constaint:")
cur.execute(
  "UPDATE flight SET flight_name = ? WHERE flight_id = ? ",(data9, data8)
)  

#This is for deleting data
print("Flight data before deleting")
for row6 in cur.execute("SELECT * FROM flight;"):
  print(row6)  
  
cur.execute(
  "DELETE from flight where flight_id = 206"
)

print("Displaying of flight table after deleting:")
for row1 in cur.execute("SELECT * FROM flight;"):
  print(row1)
#This is for taking user given input for deleting the coloumn
data10 = input("Give pilotid for deleting the entire coloumn from pilot table:")
cur.execute("DELETE FROM pilot WHERE pilot_id = {};".format(data10))



for row7 in cur.execute("SELECT * FROM pilot"):
  print(row7)  

#This is for caluclating number of flights for specific destination from flight table by user input
data11 = input("Give the destination to find number of flights there in flight table:")

cur.execute("SELECT destination, COUNT(flight_id) FROM flight WHERE destination ='{}'".format(data11))
var = cur.fetchone()
print(var)

#This is for caluclating number of flights in a particular date
cur.execute("SELECT date, COUNT(flight_id) FROM flight WHERE date ='18-12-2022'")
dar = cur.fetchone()
print(dar)

#This is for creating view and printing the values for view table

cur.execute("CREATE VIEW banglore AS SELECT * FROM flight WHERE destination = 'Banglore'")
for val in cur.execute("SELECT * FROM banglore"):
 print(val)
#This is for user defined view
  
# data111 = input("Give destination to create view")
# cur.execute("CREATE VIEW destination_table AS SELECT * FROM flight WHERE destination={}".format(data111))


#This is for searching the flight details from user given input by both destination and date 
data12 = input("Give destination for finding flight details :")
data13 = input("and give date also")
cur.execute("SELECT * from flight WHERE destination = ? AND date = ?;",(data12,data13))
res = cur.fetchone()
print(res)

#This data is searched and displayed by using inner join from another table
print("By using Inner Join the data displayed from flight table with the help of trip_id from flight_trip table")
for row4 in cur.execute("SELECT * FROM flight INNER JOIN flight_trip ON flight.flight_id = flight_trip.flight_id WHERE flight_trip.trip_id = 502"):
  print(row4)

# print("Displaying of aircraft table:")
# for row in cur.execute("SELECT * FROM aircraft;"):
#   print(row)

  

# print("Displaying of flight_trip table:")
# for row2 in cur.execute("SELECT * FROM flight_trip"):
#   print(row2) 

# print("Displaying of pilot table after deleting:")
# for row3 in cur.execute("SELECT * FROM PILOT"):
#   print(row3)



# print("Select the table");


# cur.execute("SELECT * FROM flight")

#This can help user to chose which performance to do  

print("This is for chosing options for performing tasks")
  
option = input(
    """Select options to perform the operations:
  1: Insert data
  2: Update data
  3: Delete data
  4: Caluclating number of flights
  5: Searching based on flight id
  """
)
if option == '1':
    print("Enter details into Flight Table")
    data1 = input("Enter the flight id :")
    data2 = input("Enter Flight name:")
    data3 = input("Enter Source:")
    data4 = input("Destination:")
    data5 = input("Date:")
    data6 = input("Time:")
    data7 = input("Aircraft ID:")
    cur.execute(
        "INSERT INTO flight VALUES(?,?,?,?,?,?,?)",
        (data1, data2, data3, data4, data5, data6, data7),
    )
elif option == '2':
    data9 = input("Give flight name:")
    data8 = input("Give flightid to update flight table with name constaint:")
    cur.execute(
        "UPDATE flight SET flight_name = ? WHERE flight_id = ? ", (data9, data8)
    )
elif option == '3':
    data10 = input("Give pilotid for deleting the entire coloumn from pilot table:")
    cur.execute("DELETE FROM pilot WHERE pilot_id = {};".format(data10))
elif option == '4':
    data11 = input("Give the destination to find number of flights there in flight table:")
    cur.execute("SELECT destination, COUNT(flight_id) FROM flight WHERE destination ='{}'".format(data11))
    var = cur.fetchone()
    print(var)
elif option == '5':
   data12 = input("Give destination for finding flight details :")
   data13 = input("and give date also")
   cur.execute("SELECT * from flight WHERE destination = ? AND date = ?;",(data12,data13))
   res = cur.fetchone()
   print(res)

  

con_db.commit()

con_db.close()

#Using pandas for printing the tables in format
con_db = sqlite3.connect("flight.db")
pd_aircraft = pd.read_sql_query('SELECT * FROM aircraft', con_db)
print("Displaying of aircraft table:")
print(pd_aircraft)
pd_flight = pd.read_sql_query('SELECT * FROM flight', con_db)
print("Displaying of flight table:")
print(pd_flight)
pd_flight_trip = pd.read_sql_query('SELECT * FROM flight_trip', con_db)
print("Displaying of flight_trip table:")
print(pd_flight_trip)
pd_pilot = pd.read_sql_query('SELECT * FROM pilot', con_db)
print("Displaying of pilot table:")
print(pd_pilot)
