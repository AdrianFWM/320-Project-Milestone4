import pandas as pd
import glob
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Make print line width wider
pd.options.display.max_colwidth = 1000

# First Algorithm Code
print("First Algorithm Starts")
# Read replacement abbriviation slang csv file
replacementPath = "Replacement"

replacementFile = glob.glob(replacementPath + '\*.csv')
print('File names:', replacementFile)

for file in replacementFile:

   dfReplacement = pd.read_csv(file, encoding= 'unicode_escape')
#    print(dfReplacement)

   # Store it into an array
   replaceArray = [[0]*1]*(len(dfReplacement.index))

   for i in range(len(dfReplacement.index)):
      txt = dfReplacement.loc[i].to_string()
      txt = txt.replace("Slang    ", '')
      replaceArray[i] = txt.split(": ")
   

# Below is for TA to just use for loop to read and write excel files

# getting excel files from Directory
path = 'Excel Files First'

# read all the files with extension .csv
filenames = glob.glob(path + '\*.csv')
print('File names:', filenames)

nValuesFirst = []
timeValuesFirst = []
countN = 0
number = 100
differencetemp = 0
firstloop = True

# print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:
   
   print(file)
   
   try:
      df = pd.read_csv(file)
         
      # contentCol = df[["content", "replyContent"]]

      #Content of df
      dfcontent = [[0]*1]*(len(df.index))

      contentColContent = df[["content"]]

      for i in range(len(df.index)):
         txt = contentColContent.loc[i].to_string()
         txt = txt.replace("content    ", '')
         dfcontent[i] = txt.split(" ")
      
      start = time.time()
      for x in range(len(dfcontent)):
         countN = countN + 1
         for y in range(len(dfcontent[x])):
            for i in range(len(replaceArray)):
               
               if (replaceArray[i][0] == dfcontent[x][y]):
                  dfcontent[x][y] = dfcontent[x][y].replace(replaceArray[i][0], replaceArray[i][1])
               
         if (countN == (number)):
            if(firstloop):
               end = time.time()
               difference = ((end - start) + differencetemp)*1000*1000
               timeValuesFirst.append(difference)
               nValuesFirst.append(countN)
               number = number + 100
               firstloop = False
               start = time.time()
            else:
               end = time.time()
               difference = (end - start)*1000*1000
               timeValuesFirst.append(difference)
               nValuesFirst.append(countN)
               number = number + 100
               start = time.time()
         
         dfcontent[x] = " ".join(dfcontent[x])
            
      end = time.time()
      differencetemp = (end - start)
      firstloop = True

      df["content"] = dfcontent
      
      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)      
   
   except:
      print('File is empty')

print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
# print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")

timeValuesFirst.sort()

for index in range(len(timeValuesFirst)-1):
   timeValuesFirst[index+1] = timeValuesFirst[index+1] + timeValuesFirst[index]
   
print("First Algorithm Ends")   
   
   
# Second Algorithm Code
print("Second Algorithm Starts")
# Read replacement abbriviation slang csv file
for file in replacementFile:

   dfReplacement = pd.read_csv(file, encoding= 'unicode_escape')
#    print(dfReplacement)
   
   # Store it into a dictionary
   replaceDict = {}
   
   for i in range(len(dfReplacement.index)):
      txt = dfReplacement.loc[i].to_string()
      txt = txt.replace("Slang    ", '')
      temp = txt.split(": ")
      replaceDict[temp[0]] = temp[1]
   
   print(replaceDict)

# Below is for TA to just use for loop to read and write excel files

# getting excel files from Directory
path = 'Excel Files Second'

# read all the files with extension .csv
filenames = glob.glob(path + '\*.csv')
print('File names:', filenames)

nValuesSecond = []
timeValuesSecond = []
countN = 0
number = 100
firstloop = True
differencetemp = 0

# print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:
   
   print(file)
   
   try:
       
      df = pd.read_csv(file)

      contentColContent = df[["content"]]
      
      content = {}
      # contentReply = {}
      
      for i in range(len(df.index)):
         content[i] = contentColContent.loc[i].to_string().replace("content    ", '')
      
      start = time.time()
      for key, value in content.items():
         countN = countN + 1
         for k, v in replaceDict.items():  
            if k in value:
               content[key] = value.replace(k, v)
         
         if (countN == (number)):
            if(firstloop):
               end = time.time()
               difference = ((end - start) + differencetemp)*1000*1000
               timeValuesSecond.append(difference)
               nValuesSecond.append(countN)
               number = number + 100
               firstloop = False
               start = time.time()
            else:
               end = time.time()
               difference = (end - start)*1000*1000
               timeValuesSecond.append(difference)
               nValuesSecond.append(countN)
               number = number + 100
               start = time.time()
            
      end = time.time()
      differencetemp = (end - start)
      firstloop = True

      #Replace the column "content" and "replyContent" from array
      df["content"] = content
      
      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)      
   
   except:
      print('File is empty')
      
print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
# print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")
      
for index in range(len(timeValuesSecond)-1):
   timeValuesSecond[index+1] = timeValuesSecond[index+1] + timeValuesSecond[index]

print("Second Algorithm Ends")
   
print("First Algorithm Data")
print(nValuesFirst)
print(timeValuesFirst)   
   
print("Second Algorithm Data")
print(nValuesSecond)
print(timeValuesSecond)
   
   
print(countN)
plt.plot(nValuesFirst, timeValuesFirst, color="blue", label="First algorithm runtime tweets")
plt.plot(nValuesSecond, timeValuesSecond, color="red", label="Second algorithm runtime tweets")
plt.xlabel("n(Number of tweets)")
plt.ylabel("Time(ms * 1000)")
plt.legend()
plt.title("First and Second algorithm runtime vs number of tweet")
plt.show()   
   