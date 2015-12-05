# coding: utf-8
import os

filescounter = 0
totalwords = 0
sword = 'python' #sample pattern to search
resfile = '/Users/apple/Documents/result.txt'
dirtosearch = '/Users/apple/Documents/'
print ("Hello! Lets start! Searching for word " + sword + " in files")

result = open(resfile, 'w')

files = os.listdir(dirtosearch)
for file in files:
    s = open(file).read()
    if s.count(sword) > 0:
        filescounter += 1    
        print (s.count(sword), " - words in file", file)        
        totalwords += s.count(sword)
        #result.write("File "+ str(file) + " Contains " +str(totalwords) + " words." + "\n")
        result.write((lambda a, b: "File "+ a + " Contains " + b + " words." + "\n")(str(file), str(totalwords)))
print ("Total files found", filescounter)
print ("Total words found", totalwords)
result.write("Total files " + str(filescounter)  + "\n")
result.write("Total words " + str(totalwords)  + "\n")
result.close()

print ("Result was successfully written in " + resfile)
