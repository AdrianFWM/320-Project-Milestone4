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

   # Store it into an array
   replaceArray = [[0]*1]*(len(dfReplacement.index))

   for i in range(len(dfReplacement.index)):
      txt = dfReplacement.loc[i].to_string()
      txt = txt.replace("Slang    ", '')
      replaceArray[i] = txt.split(": ")
      # print(txt)

   # print("\n",replaceArray)
   

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
differencetemp = 0
firstloop = True

print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:
   
   print(file)
   
   try:
      df = pd.read_csv(file)
      # print("\nReading file = ",file)
      # print("The length of this file is ",len(df.index))
         
      contentCol = df[["content", "replyContent"]]
      # print("\nThe contents are: ")
      # print(contentCol, "\n")

      #Content of df
      dfcontent = [[0]*1]*(len(df.index))

      contentColContent = df[["content"]]

      for i in range(len(df.index)):
         txt = contentColContent.loc[i].to_string()
         txt = txt.replace("content    ", '')
         dfcontent[i] = txt.split(" ")
      # print("The content array: \n",dfcontent,"\n")

      #Reply Content of df
      # dfreply = [[0]*1]*(len(df.index))

      # contentColReply = df[["replyContent"]]

      # for i in range(len(df.index)):
      #    txt = contentColReply.loc[i].to_string()
      #    txt = txt.replace("replyContent    ", '')
      #    txt = txt.replace("NaN", '')
      #    dfreply[i] = txt.split(" ")
      # print("The reply content array: \n",dfreply, "\n")


      # print("Abbriviation text replacement for this file starts.")
      # #Replace slang keywords with proper keywords
      
      
      
      start = time.time()
      for x in range(len(dfcontent)):
         countN = countN + 1
         for y in range(len(dfcontent[x])):
            for i in range(len(replaceArray)):
               
               if (replaceArray[i][0] == dfcontent[x][y]):
                  dfcontent[x][y] = dfcontent[x][y].replace(replaceArray[i][0], replaceArray[i][1])
                  
               # if replaceArray[i][0] in dfreply[x]:
               #    dfreply[x] = dfreply[x].replace(replaceArray[i][0], replaceArray[i][1])
               
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
         
         dfcontent[x] = " ".join(dfcontent[x])
            
      end = time.time()
      differencetemp = (end - start)
      firstloop = True
      
      # print("Abbriviation text replacement has been finished.")

      #Replace the column "content" and "replyContent" from array
      df["content"] = dfcontent
      # df["replyContent"] = dfreply
      
      # print("The array of abbriviation replacement has been copied and replace into a dataframe")

      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)
      
      # print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")
      
   

   except:
      print('File is empty')

print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")

timeValues.sort()

for index in range(len(timeValues)-1):
   timeValues[index+1] = timeValues[index+1] + timeValues[index]
   
print(nValues)
print(timeValues)
   
   
print(countN)
# plt.plot(nValuesNaive, tValuesNaive, color="red", label="Naive version")
plt.plot(nValues, timeValues, color="blue", label="First algorithm runtime tweets")
plt.xlabel("n(Number of tweets)")
plt.ylabel("Time(ms * 1000)")
plt.legend()
plt.title("First algorithm runtime vs number of tweet")
plt.show()   
   