import pandas as pd
import glob
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Make print line width wider
pd.options.display.max_colwidth = 1000

# Read replacement abbriviation slang csv file
replacementPath = "Replacement"

replacementFile = glob.glob(replacementPath + '\*.csv')
print('File names:', replacementFile)

for file in replacementFile:

   dfReplacement = pd.read_csv(file, encoding= 'unicode_escape')
   print(dfReplacement)
   
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
path = 'Excel Files'

# read all the files with extension .csv
filenames = glob.glob(path + '\*.csv')
print('File names:', filenames)

nValues = []
timeValues = []
countN = 0
number = 100
# number = 5
firstloop = True
differencetemp = 0

print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:
   
   # print(file)
   
   try:
      df = pd.read_csv(file)
      # print("\nReading file = ",file)
      # print("The length of this file is ",len(df.index))

      contentColContent = df[["content"]]
      
      # contentColReply = df[["replyContent"]]
      
      # count = 0
      
      content = {}
      contentReply = {}
      
      for i in range(len(df.index)):
         content[i] = contentColContent.loc[i].to_string().replace("content    ", '')
         # contentReply[count] = contentColReply.loc[i].to_string().replace("replyContent    ", '').replace("NaN", '')
         # count = count + 1
         
      # print(content)
      # print(contentReply)

      # print("Abbriviation text replacement for this file starts.")
      # #Replace slang keywords with proper keywords
      
      # count = 0
      
      start = time.time()
      for key, value in content.items():
         countN = countN + 1
         # print(key, value)
         for k, v in replaceDict.items():  
            # print(k)
            # print(v)
            if k in value:
               content[key] = value.replace(k, v)
            # if k in contentReply[count]:
            #    contentReply[key] = contentReply[k].replace(k, v)
            
            # print(content[key])
            # print(contentReply[key])
      
         # print(content[key])
         
         if (countN == (number)):
            if(firstloop):
               end = time.time()
               difference = ((end - start) + differencetemp)*1000*1000
               timeValues.append(difference)
               nValues.append(countN)
               number = number + 100
               # number = number + 5
               firstloop = False
               start = time.time()
            else:
               end = time.time()
               difference = (end - start)*1000*1000
               timeValues.append(difference)
               nValues.append(countN)
               number = number + 100
               # number = number + 5
               start = time.time()
            
      end = time.time()
      differencetemp = (end - start)
      firstloop = True
      
      # print("Abbriviation text replacement has been finished.")

      #Replace the column "content" and "replyContent" from array
      df["content"] = content
      # df["replyContent"] = contentReply
      
      # print(df["content"])
      
      # print("The array of abbriviation replacement has been copied and replace into a dataframe")

      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)
      
      # print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")
      
   
   except:
      print('File is empty')
      
print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")
      
for index in range(len(timeValues)-1):
   timeValues[index+1] = timeValues[index+1] + timeValues[index]
   
print(nValues)
print(timeValues)   
   
print(countN)
# plt.plot(nValuesNaive, tValuesNaive, color="red", label="Naive version")
plt.plot(nValues, timeValues, color="red", label="Second algorithm runtime tweets")
plt.xlabel("n(Number of tweets)")
plt.ylabel("Time(ms * 1000)")
plt.legend()
plt.title("Second algorithm runtime vs number of tweet")
plt.show()   
