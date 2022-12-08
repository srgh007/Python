import psycopg2

conn = psycopg2.connect(
    dbname="strength", user="postgres", password="postgres", host="localhost"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks LIMIT 10")
records = cursor.fetchall()

print(records)

cursor.close()
conn.close()
