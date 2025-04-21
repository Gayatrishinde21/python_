import psycopg2



try:
   conn = psycopg2.connect(
        dbname="add_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
)
   cur = conn.cursor()
   print("Connected to the database successfully.")
except:
    exit()

cur.execute("CREATE SCHEMA IF NOT EXISTS gatishakti;")
conn.commit()

cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
conn.commit() 
# Connect to PostgreSQL

create_table_query = """
    CREATE TABLE gatishakti.cmp_master (
        gid INTEGER,
        cmp_name VARCHAR(50),
        cmp_fullname VARCHAR(50),
        eurja_id VARCHAR(50),
        geom GEOMETRY(MultiPolygon)
    );
    """

cur.execute(create_table_query)
conn.commit()
print("Table created successfully.")

try:
    with open('cmp_master.sql', 'r') as file:
        sql_commands = file.readlines()  # Read lines from the file
        #print(sql_commands)

    for command in sql_commands:
        command = command.strip()  # Remove leading/trailing whitespace
        
        # Skip empty lines and comments
        if not command or command.startswith('--'):
            continue
        try:
            cur.execute(command)  # Execute the command directly
        except Exception as e:
           conn.rollback()  # Rollback the transaction on error

    conn.commit()  
    
except Exception as e:
   exit()


conn.commit()    
cur.close()
conn.close()
print("Table created and data inserted successfully!")
