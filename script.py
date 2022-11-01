#!/bin/python3
# Written by Michael Beavitt on 01/11/2022
# This script takes a preset .csv data file containing four columns and parses it

# Reading file as list of rows
#with open("data.csv") as file:
#    data = file.read().strip().split('\n')
file=open('data.csv')

# Setting variables
exercise_1 = []
exercise_2 = []
exercise_3 = []
exercise_4 = []
exercise_5 = []

for line in file:
    entry = line.split(",")
    species = entry[0].split(" ")[1]
    gene = entry[1]
    ad = gene.count("a")
    th = gene.count("t")
    cy = gene.count("c")
    gu = gene.count("g")
    total = ad + th + cy + gu
    genename = entry[2]
    AT_cont = ((ad + th) / total)
# Returning gene names for melanogaster and simulans
    if species == "melanogaster":
        exercise_1.append("Drosophila " + species + ": " + genename)
    elif species == "simulans":
        exercise_1.append("Drosophila " + species + ": " + genename)
#     Parsing gene length
    if len(gene) > 90 and len(gene) < 110:
        exercise_2.append("gene is: " + genename)
#     Parsing base counts and performing calculations
    if AT_cont < 0.5 and int(entry[3]) > 200:
        exercise_3.append(genename)
#     Printing gene names based on the characteristics of their name and the species
    if genename.startswith("k") or genename.startswith("h") and species!= "melanogaster":
        exercise_4.append(genename)
#     Finding AT content level
    if AT_cont > 0.65:
        contentlevel = "high"
    elif AT_cont < 0.45:
        contentlevel = "low"
    else:
        contentlevel = "medium"
    exercise_5.append(genename + ": " + contentlevel)

print("Gene names for all genes from the species Drosophila melanogaster or Drosophila simulans")
print([f"{x}" for x in exercise_1])
print("Gene names for all genes that are between 90 and 110 bases long")
print([f"{x}" for x in exercise_2])
print("Gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200")
print([f"{x}" for x in exercise_3])
print("Gene names for all genes whose name begins with 'k' or 'h' except those belonging to Drosophila melanogaster.")
print([f"{x}" for x in exercise_4])
print("AT content level (high, medium, low...)")
print([f"{x}" for x in exercise_5])
