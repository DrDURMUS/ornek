import sqlite3
conn = sqlite3.connect("employee.db")
c=conn.cursor()

#c.execute("""CREATE TABLE employees(
#first text,
#last text,
#pay integer)""")

#c.execute("INSERT INTO employees VALUES ('durmus','durmaz',334445)")
c.execute("SELECT * FROM employees WHERE last='durmaz'")
print(c.fetchone())
print(c.fetchmany(3))
print(c.fetchall())
conn.commit()
conn.close()
