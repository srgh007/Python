import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    dbname="strength", user="postgres", password="postgres", host="localhost"
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("SELECT * FROM tasks LIMIT 10")

records = cursor.fetchall()

for row in records:
    print(row["title"])

cursor.close()
conn.close()
