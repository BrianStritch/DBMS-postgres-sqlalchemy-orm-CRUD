# to import psycopg2 you type the following into the command line 
# pip3 install psycopg2


import psycopg2  

# connect to chinook database
connection = psycopg2.connect(database = "chinook")

# build a curser object of the database
cursor = connection.cursor()


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
#results = cursor.fetchone()


# close the connection
connection.close()

# print results
for result in results:
    print(result)
