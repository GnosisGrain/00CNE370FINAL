### Code written by Doc McDowell for CNE370 Winter Quarter, 2023, mcdowelldoc@gmail.com with assistance from the following resources:
# This app runs a command in Ubuntu environtments to shard SQL databases and merges data from command line
#https://mariadb.com/resources/blog/schema-sharding-with-mariadb-maxscale-2-1-part-1/
#https://k21academy.com/docker-kubernetes/docker-compose/
#https://devhints.io/docker-compose

import mysql.connector

# Connect to Maxscale instance
db = mysql.connector.connect(
    host="127.0.0.1",
    user="maxusr",
    password="maxpwd",
    database="zipcodes"
)

# Query to get last 10 rows of zipcodes_one
zipcodes_one_query = "SELECT * FROM zipcodes_one ORDER BY id DESC LIMIT 10"

# Query to get first 10 rows of zipcodes_two
zipcodes_two_query = "SELECT * FROM zipcodes_two LIMIT 10"

# Query to get the largest zipcode in zipcodes_one
zipcodes_one_max_query = "SELECT MAX(zipcode) FROM zipcodes_one"

# Query to get the smallest zipcode in zipcodes_two
zipcodes_two_min_query = "SELECT MIN(zipcode) FROM zipcodes_two"

# Execute the queries
cursor = db.cursor()
cursor.execute(zipcodes_one_query)
zipcodes_one_result = cursor.fetchall()

cursor.execute(zipcodes_two_query)
zipcodes_two_result = cursor.fetchall()

cursor.execute(zipcodes_one_max_query)
zipcodes_one_max_result = cursor.fetchone()[0]

cursor.execute(zipcodes_two_min_query)
zipcodes_two_min_result = cursor.fetchone()[0]

# Print the results to console
print("Last 10 rows of zipcodes_one:")
for row in zipcodes_one_result:
    print(row)

print("\nFirst 10 rows of zipcodes_two:")
for row in zipcodes_two_result:
    print(row)

print("\nLargest zipcode in zipcodes_one:", zipcodes_one_max_result)

print("\nSmallest zipcode in zipcodes_two:", zipcodes_two_min_result)

# Close the database connection
db.close()
