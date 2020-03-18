import sqlite3


conn = sqlite3.connect('hack_db')
cur = conn.cursor()
cur.execute("DELETE FROM HackData WHERE registration_no='KA03MU5190'")
#cur.execute("DELETE FROM RCData WHERE state='Karnataka'")
cur.execute("SELECT * FROM HackData")
#cur.execute("DROP TABLE HackData")
s = cur.fetchall()
conn.commit()
print(s)
