import sqlite
conn = sqlite.connect("temp.db")
c = conn.cursor()
res = c.execute("select * from table1")

print(res.fetchone())
