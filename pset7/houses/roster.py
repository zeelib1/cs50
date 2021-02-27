# # reading data from that database, and providing it back to the user
from cs50 import SQL
from sys import argv

# command line arguments conditions

if len(argv) != 2:
    print("Required 2 CLA arguments")
    exit(1)

# python and sql connection
db = SQL("sqlite:///students.db")

# querying the students table
house = db.execute(f"SELECT first,middle,last,birth FROM students WHERE house='{argv[1]}' ORDER BY last ASC")

# filtering middle and printing accordingly
filtered_students = {}
for students in house:

    filtered = {k: v for k, v in students.items() if v is not None}
    filtered_students = filtered
    if filtered_students.get('middle') == None:
        print(f"{filtered_students.get('first')} {filtered_students.get('last')}, born {filtered_students.get('birth')}")
    else:
        print(f"{filtered_students.get('first')} {filtered_students.get('middle')} {filtered_students.get('last')}, born {filtered_students.get('birth')}")

