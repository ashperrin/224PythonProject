import mysql.connector

shop_db = mysql.connector.connect(host="127.0.0.1",
                                database="amazon_bot_db",
                                user="root",
                                passwd="1890BTz!"
                            )
print("Connected to " + str(shop_db))


# A test to fetch all data from the User datatable
#sql_query = "select * from User"
#cursor = shop_db.cursor()
#cursor.execute(sql_query)
#records = cursor.fetchall()
#print(records)

# Close the database connection
#shop_db.close()
