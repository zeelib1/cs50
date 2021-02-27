import csv
from sys import argv
import re

# Conditions for the argc quantity

if len(argv) != 3:
    print("DNA requires three CL-arguments")

# Opening and storing the CSV file; DNA individual seq. stored into a list

person_dna = []
generic_dna = []

with open(argv[1]) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    count_lines = 0

    for row in reader:
        if count_lines == 0:
            person_dna = ','.join(row)

            count_lines += 1

person_dna = person_dna.split(',')
person_dna.pop(0)


# Open the generic DNA sequnce and store it as a string

with open(argv[2]) as file:
    generic_dna = csv.reader(file)
    for row in generic_dna:
        generic_dna = row

generic_dna = generic_dna[0]

# Take person_dna and check STR sequences in the generic_dna sequence

l = len(generic_dna)
max_occurence_length = 0
new = []
counting_matches = 0

for sequence in person_dna:

    res = max(re.findall('((?:' + re.escape(sequence) + ')*)', generic_dna), key=len)
    sequence_len = len(sequence)
    for i in range(len(res)):
        if(sequence == res[i:i + sequence_len]):
            while sequence == res[i:i + sequence_len]:

                counting_matches += 1
                new.append(sequence)
                break

# count the sequences
dna_object = {i: new.count(i) for i in new}

dna_list = []
for value in dna_object.values():
    dna_list.append(value)


# making names as the keys and dict values containing list of values for comparison
# https://stackoverflow.com/questions/16139558/read-csv-then-enumerate
compare_dna = {}
with open(argv[1]) as csvfile:
    plotlist = csv.reader(csvfile)
    for i, row in enumerate(plotlist):
        compare_dna[row[0]] = [str(x) for x in row[1:]]

# 'stringification' of list elements for comparisons
dna_list_string = []
for i in dna_list:
    i = str(i)
    dna_list_string.append(i)


# Compare the values inside the human DNA; print the name accordingly
count = 0
for key, value in compare_dna.items():

    if value == dna_list_string:
        count += 1
        print(key)
        exit(0)
print("No match")
