import psycopg2
from psycopg2 import sql

# Database connection details
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "boostdevdb"
DB_USER = "boostdev"
DB_PASSWORD = "supersecret"


def store_client(user):
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        # print("Connected to the database successfully!")

        # Create a cursor object
        cursor = connection.cursor()

        # Create a table (if it doesn't already exist)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE,
            location VARCHAR(100),
            card VARCHAR(100),
            unique_id VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        # Create a table (if it doesn't already exist)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS drivers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE,
            location VARCHAR(100),
            card VARCHAR(100),
            unique_id VARCHAR(100),
            vehicle_reg VARCHAR(100) UNIQUE,
            vehicle_class VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully!")

        # Insert data into the table
        if user.category == "client":
            insert_query = """
            INSERT INTO users (name,location,card,unique_id) VALUES (%s, %s,%s,%s);
            """
            data_to_insert = [
                (user.name, user.location, user.card,str(user.id)),
        ]
        elif user.category == "driver":
            insert_query = """
            INSERT INTO drivers (name,location,card,unique_id,vehicle_reg,vehicle_class) VALUES (%s, %s,%s,%s,%s,%s);
            """
            data_to_insert = [
                (user.name, user.location, user.card,str(user.id),user.vehicle_reg,user.vehicle_class),
        ]
        try:
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            print("Data inserted successfully!")

            # # Fetch and display data
            # cursor.execute("SELECT * FROM users;")
            # users = cursor.fetchall()
            # print("Users in the database:")
            # for user in users:
            #     print(user)
        except Exception as user_exists:
            print(f"An error occurred: {user_exists}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")