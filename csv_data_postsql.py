import psycopg2
from psycopg2.extras import execute_values
import csv



try:
    conn = psycopg2.connect(
        dbname="add_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    cursor = conn.cursor()
    print("Connected to the database successfully.")
    
except:
    exit()
# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS season(
    id SERIAL PRIMARY KEY,
    State TEXT,
    Pre_Monsoon TEXT,
    Monsoon TEXT,
    Post_Monsoon TEXT,
    Post_Monsoon_Rabi TEXT
);
"""
cur.execute(create_table_query)
conn.commit()
print("Table created successfully.")


with open('season_distribution.sql', 'r') as file:
        sql_commands = file.read() 

for row in sql_commands:
        id=row['id']
        State=row['State']
        Pre_Monsoon=row['Pre_Monsoon']
        Monsoon=row['Monsoon']
        Post_Monsoon=row['Post_Monsoon']
        Post_Monsoon_Rabi=row['Post_Monsoon_Rabi']





# Insert query
insert_query = f"""INSERT INTO season_distribution(State,Pre_Monsoon,Monsoon,Post_Monsoon,Post_Monsoon_Rabi
) VALUES ({id},'{State}','{Pre_Monsoon}','{Monsoon}','{Post_Monsoon}','{Post_Monsoon_Rabi}');"""
cursor.execute(insert_query,(id,State,Pre_Monsoon,Monsoon,Post_Monsoon,Post_Monsoon_Rabi))
conn.commit()

cur.close()
conn.close()

print("Table created and data inserted successfully!")
