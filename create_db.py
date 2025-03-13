import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Adjola12.,"  # Ensure your password is correct
)

# Create a cursor object
cursor = conn.cursor()

# Define the database name
database_name = "farmconnect_db"  # Replace with your preferred database name

# Execute the CREATE DATABASE command
cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")

print(f"Database '{database_name}' created successfully!")

# Close the connection
cursor.close()
conn.close()
