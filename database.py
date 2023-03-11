import pymysql

# Connect to database
conn = pymysql.connect(host='localhost', user='maxuser', passwd='1cadwaer2', db='zipcodes')

# Create cursor object
cursor = conn.cursor()

# Print last 10 rows of zipcodes_one
print('The last 10 rows of zipcodes_one are:')
sql = "SELECT * FROM zipcodes_one LIMIT 9990, 10"
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)

# Print first 10 rows of zipcodes_two
print('The first 10 rows of zipcodes_two are:')
sql = "SELECT * FROM zipcodes_two LIMIT 10"
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)

# Print largest zipcode number in zipcodes_one
print('The largest zipcode number in zipcodes_one is:')
sql = "SELECT Zipcode FROM zipcodes_one ORDER BY Zipcode DESC LIMIT 1"
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)

# Print smallest zipcode number in zipcodes_two
print('The smallest zipcode number in zipcodes_two is:')
sql = "SELECT Zipcode FROM zipcodes_two ORDER BY Zipcode ASC LIMIT 1"
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)

# Close database connection
conn.close()
