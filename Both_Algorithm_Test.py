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

   # Store it into an array with number of rows in the excel file times index 2, index[0] for slang/abbriviation key and index[1] for proper phrase replacement
   replaceArray = [[0]*1]*(len(dfReplacement.index))
   
   # Use for loop to store the slangs and proper phrase into an 2D array
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

nValuesFirst = []    # The number of tweets has been read throughout the for loop
timeValuesFirst = [] # The recorded time for running the for loop each 100 times
countN = 0           #  Keep track of the number of for loops (tweets has been read) has been ran
number = 100         # The number of loops (line of tweets) to record the time
differencetemp = 0   # The time from previous file reading, if the previous file did not read 100 tweets, store the time and add the time with the next file until it reaches 100 tweets reading in for loop
firstloop = True     # If it is the first 100 loops (line of tweet reading) set this to true and add the differencetemp time with the current time, else set it to false and not add the differencetemp time

# print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:  # Read all files in the folder
   
   print(file)
   
   try:
      df = pd.read_csv(file)  # Read the excel files
         
      # contentCol = df[["content", "replyContent"]]

      #Content of df
      dfcontent = [[0]*1]*(len(df.index))    # Make an 2D array to with number of rows(tweet contents) and words inside the tweets contents in the excel file times

      contentColContent = df[["content"]]

      # Store the Words in each of the tweets into the 2D array 
      for i in range(len(df.index)):
         txt = contentColContent.loc[i].to_string()
         txt = txt.replace("content    ", '')
         dfcontent[i] = txt.split(" ")
      
      start = time.time()  # Start timer
      for x in range(len(dfcontent)):  # loop the number of line of tweets in the 2D array
         countN = countN + 1     # Increment if next loop, keep track of number of tweet reading
         for y in range(len(dfcontent[x])):  # loop the number of words per tweets in the 2D array
            for i in range(len(replaceArray)):  # loop the number of slang keywords (68 rows in Slang words.csv) in 2D array
               
               if (replaceArray[i][0] == dfcontent[x][y]):  # Replace the word if it matches with the slang keyword, and replace it will the proper phrase 
                  dfcontent[x][y] = dfcontent[x][y].replace(replaceArray[i][0], replaceArray[i][1])
               
         if (countN == (number)):   # If 100 tweet has been read (100 for loops has benn ran)
            if(firstloop):    # if it is the first 100 for loops (100 line of tweets has been read) has been current finish running
               end = time.time()    # Stop timer 
               difference = ((end - start) + differencetemp)*1000*1000  # Get the time for running 100 for loops with differencetemp time
               timeValuesFirst.append(difference)  # Store the time
               nValuesFirst.append(countN)   # Store the current count
               number = number + 100   # add 100 more into number for the next 100 line of tweet reading (for loop running)
               firstloop = False    # Set firstloop to false because the first 100 tweet from this file has been read
               start = time.time()  # Start timer for the next for loops
            else:
               end = time.time()     # Stop timer 
               difference = (end - start)*1000*1000   # Get the time for running 100 for loops
               timeValuesFirst.append(difference)  # Store the time
               nValuesFirst.append(countN)   # Store the current count
               number = number + 100   # add 100 more into number for the next 100 line of tweet reading (for loop running)
               start = time.time()  # Start timer for the next for loops
         
         dfcontent[x] = " ".join(dfcontent[x])  
            
      end = time.time()    # If all of the line of tweets that are in this current excel file has been read, stop the timer
      differencetemp = (end - start)   # Get the time for the tweets that has not been reach 100 for loops
      firstloop = True  # Set firstloop to true for the next file, and add the differencetemp time if 100 tweets has been read

      df["content"] = dfcontent  # Store the replaced tweets to dataframe
      
      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)      
   
   except:
      print('File is empty')

print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
# print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")

timeValuesFirst.sort()  # Sort the time for first algorithm for cleaner graph

for index in range(len(timeValuesFirst)-1):  # Add the previous time for each recorded time to show the running time for each 100 for loops (100 line of tweet reading)
   timeValuesFirst[index+1] = timeValuesFirst[index+1] + timeValuesFirst[index]
   
print("First Algorithm Ends")   
   
   
# Second Algorithm Code
print("Second Algorithm Starts")
# Read replacement abbriviation slang csv file
for file in replacementFile:

   dfReplacement = pd.read_csv(file, encoding= 'unicode_escape')
#    print(dfReplacement)
   
   # Store it into a dictionary
   replaceDict = {}     # Dictionary for slang/abbriviation and proper phrase, key is for slang keywords, value is for proper phrases for replacements
   
   # Use for loop to store the slangs and proper phrase into an dictionary
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

nValuesSecond = []   # The number of tweets has been read throughout the for loop
timeValuesSecond = []   # The recorded time for running the for loop each 100 times
countN = 0           #  Keep track of the number of for loops (tweets has been read) has been ran
number = 100         # The number of loops (line of tweets) to record the time
firstloop = True      # The time from previous file reading, if the previous file did not read 100 tweets, store the time and add the time with the next file until it reaches 100 tweets reading in for loop
differencetemp = 0     # If it is the first 100 loops (line of tweet reading) set this to true and add the differencetemp time with the current time, else set it to false and not add the differencetemp time
  

# print("Reading files in folder", filenames)
print("Abbriviation text replacement for this file starts.")

for file in filenames:  # Read all files in the folder
   
   print(file)
   
   try:
       
      df = pd.read_csv(file)  # Read the excel files

      contentColContent = df[["content"]]
      
      content = {}      # Dictonary for lines of tweets are in the excel file
      # contentReply = {}
      
      # Store the tweet contents into the dictioanry 
      for i in range(len(df.index)):
         content[i] = contentColContent.loc[i].to_string().replace("content    ", '')
      
      start = time.time()  # Start timer
      for key, value in content.items():   # loop the number of line of tweets in dictioanry 
         countN = countN + 1   # Increment if next loop, keep track of number of tweet reading
         for k, v in replaceDict.items():  # loop the number of slang keywords (68 rows in Slang words.csv) in dictioanry 
            if k in value: # If the slang keywords is contains/in the line of tweet
               content[key] = value.replace(k, v)  # Replace the slang word in the tweet to the proper phrase
         
         if (countN == (number)):   # If 100 tweet has been read (100 for loops has benn ran)
            if(firstloop): # if it is the first 100 for loops (100 line of tweets has been read) has been current finish running
               end = time.time() # Stop timer 
               difference = ((end - start) + differencetemp)*1000*1000  # Get the time for running 100 for loops with differencetemp time
               timeValuesSecond.append(difference)  # Store the time
               nValuesSecond.append(countN)   # Store the current count
               number = number + 100   # add 100 more into number for the next 100 line of tweet reading (for loop running)
               firstloop = False # Set firstloop to false because the first 100 tweet from this file has been read
               start = time.time()
            else:
               end = time.time() # Stop timer 
               difference = (end - start)*1000*1000   # Get the time for running 100 for loops
               timeValuesSecond.append(difference)  # Store the time
               nValuesSecond.append(countN)   # Store the current count
               number = number + 100   # add 100 more into number for the next 100 line of tweet reading (for loop running)
               start = time.time()     # Start timer for the next for loops
            
      end = time.time()  # If all of the line of tweets that are in this current excel file has been read, stop the timer
      differencetemp = (end - start)   # Get the time for the tweets that has not been reach 100 for loops
      firstloop = True  # Set firstloop to true for the next file, and add the differencetemp time if 100 tweets has been read

      #Replace the column "content" and "replyContent" from array
      df["content"] = content
      
      #Convert the dataframe in a csv file with the same name as the original file
      df.to_csv(file, index=False)      
   
   except:
      print('File is empty')
      
print("Abbriviation text replacement has been finished.")
print("The array of abbriviation replacement has been copied and replace into a dataframe")      
# print("The file: ", file, " addriviation text words has all been replaced with the proper phrases.")
      
for index in range(len(timeValuesSecond)-1):  # Add the previous time for each recorded time to show the running time for each 100 for loops (100 line of tweet reading)
   timeValuesSecond[index+1] = timeValuesSecond[index+1] + timeValuesSecond[index]

print("Second Algorithm Ends")
   
print("First Algorithm Data")
print(nValuesFirst)  # Print the n values for first algorithm
print(timeValuesFirst)   # Print the time recording for first algorithm
   
print("Second Algorithm Data")
print(nValuesSecond) # Print the n values for second algorithm
print(timeValuesSecond)    # Print the time recording for second algorithm
   
   
print(countN)
plt.plot(nValuesFirst, timeValuesFirst, color="blue", label="First algorithm runtime tweets")   #  Blue is first algorithm data
plt.plot(nValuesSecond, timeValuesSecond, color="red", label="Second algorithm runtime tweets") # Red is second algorithm data
plt.xlabel("n(Number of tweets)")
plt.ylabel("Time(ms * 1000)")
plt.legend()
plt.title("First and Second algorithm runtime vs number of tweet")
plt.show()   
   