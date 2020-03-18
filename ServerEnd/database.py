import sqlite3


conn = sqlite3.connect('hack_db')
cur = conn.cursor()
cur.execute("DELETE FROM HackData WHERE registration_no='null'")
#cur.execute("DELETE FROM HackData WHERE state='Maharashtra' ")
#cur.execute("SELECT * FROM RCData")
s = cur.fetchall()
conn.commit()
print(s)
