#!/bin/python3
# Written by Michael Beavitt on 01/11/2022
# This script takes a preset .csv data file containing four columns and parses it

# Reading file as list of rows
with open("data.csv") as file:
    data = file.read().strip().split('\n')

print("\n\nGenes of D. melanogaster and D. simulans:\n")

# Processing rows, returning gene names for melanogaster and simulans
for line in data:
    entry = line.split(",")
    species = entry[0].split(" ")
    if species[1] == "melanogaster":
        print("Drosophila " + species[1] + ": " + entry[2])
    elif species[1] == "simulans":
        print("Drosophila " + species[1] + ": " + entry[2])
    else:
        continue

print("\n\nGenes between 90 and 110 bases long...:\n")

for line in data:
    entry = line.split(",")
    if len(entry[1]) > 90 and len(entry[1]) < 110:
        print("gene is: " + entry[2])

print('\n')
