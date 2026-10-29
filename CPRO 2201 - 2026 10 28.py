#%% Using 'with' 

import sqlite3
from dataclasses import dataclass

con = sqlite3.connect("college.db")
con.row_factory = sqlite3.Row

@dataclass
class Student:
    id: int
    name: str
    program: str

def read_all(c):
    c.execute(
        "SELECT id, name, program FROM students"
    )    
    
    students = []    
    for row in c.fetchall():
        students.append(
            Student(
                row["id"], row["name"], row["program"]
            )
        )
    return students
    
def print_all(s_list):
    for s in s_list:
        print(f"{s.id}, {s.name}, {s.program}")
    

cur = con.cursor()

students_list = read_all(cur)
print_all(students_list)

con.close()


#%%
import sqlite3
from dataclasses import dataclass

con = sqlite3.connect("college.db")
con.row_factory = sqlite3.Row

try:
    with con:
        con.execute("INSERT INTO students (id, name, program) "
                    "VALUES (?,?,?)",
                    (25, "Name3", "Program3")                
        )
except sqlite3.Error as e:
    print(f"ERROR: {e}")
finally:
    con.close()

# reopening the connection
con = sqlite3.connect("college.db")
con.row_factory = sqlite3.Row

cur = con.cursor()
students_list = read_all(cur)
print_all(students_list)







#%% Using try...[catch]...finally


#%% Using 'dataclasses'