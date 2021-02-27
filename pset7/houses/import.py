# inserting csv into  students db

import csv
from cs50 import SQL
from sys import argv

# command line arguments conditions

if len(argv) != 2:
    print("Houses.py requires two CL-arguments")
    exit(1)

# defining SQL db
db = SQL("sqlite:///students.db")

# opening CSV and reading into SQL students table

with open(argv[1]) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        name = row["name"].split()
        if len(name) > 2:
            db.execute("INSERT INTO students (first,middle, last, house, birth) VALUES (?, ?, ?, ?,?)",

                       name[0], name[1], name[2], row["house"], row["birth"])

        elif(len(name) == 2):
            db.execute("INSERT INTO students (first,middle,last, house, birth) VALUES (?, ?, ?, ?, ?)",

                       name[0], None, name[1], row["house"], row["birth"])
