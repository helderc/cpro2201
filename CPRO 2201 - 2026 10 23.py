import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

sql = """
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    age INTEGER    
)
"""

cur.execute(sql)

name, program, age = "Mary", "Computer P.", 66

cur.execute(
    "INSERT INTO students (name, program, age) "
    "VALUES (?, ?, ?)",
    (name, program, age)
)

con.commit()
con.close()

#%%
def read_all(c):
    c.execute(
        "SELECT id, name, program FROM students"
    )
    
    for row in c.fetchall():
        #print(type(row), row)
        print(
            row["id"], 
            row["name"], 
            row["program"]
        )

#%%
import sqlite3

con = sqlite3.connect("college.db")
con.row_factory = sqlite3.Row

cur = con.cursor()

read_all(cur)

cur.execute(
    "UPDATE students "
    "SET program = ?"
    "WHERE id = ?",
    ("Computer Programming", 2)
)
con.commit()

print("After the change: ")
read_all(cur)

con.close()











