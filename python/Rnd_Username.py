# Attempts to generate usernames using random generator

import random 
import string
try:
  from random_word import RandomWords
except Exception as e:
  print("Exception at import: [",e," ]")
  exit()

def genUserName():
  r = RandomWords()
  lGen1 = r.get_random_words(hasDictionaryDef='True',includePartOfSpeech='noun')
  lGen1.extend(r.get_random_words(hasDictionaryDef='True',includePartOfSpeech='noun'))
  lGen1.extend(r.get_random_words(hasDictionaryDef='True',includePartOfSpeech='noun'))
  lUniq1= []
  for count in range(len(lGen1)):
    s = lGen1[count].lower()
    s= "".join(s.split())
    if s not in lUniq1:
      lUniq1.append(s)
  
  def replacer(resultantName,randChoice):
    inds = [i for i,_ in enumerate(resultantName) if not resultantName.isspace()]
    choiceRand_Max = 3 if len(resultantName)/3 > 2 else int(len(resultantName)/3)
    sam = random.sample(inds, random.randint(0,choiceRand_Max))
    lst = list(resultantName)
    for ind in sam:
      lst[ind] = random.choice(randChoice)
    resultantName="".join(lst)
    return resultantName

  #print(len(lGen1), len(lUniq1))

  lGenName1=[]
  for count in range(len(lUniq1)):
    ranOption = random.randint(0,3)
    resultantName=lUniq1[count]
    if ranOption == 1:
      #Append Numbers
      resultantName=resultantName+str(random.choice(string.digits))
    elif ranOption ==2:
      #Change some parts of a string to numbers
      resultantName=replacer(resultantName,string.digits)
    elif ranOption ==3:
      #Change some parts of a string to punct
      allowedPunct=['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '-', '~']
      resultantName=replacer(resultantName,allowedPunct)
    else:
      #Do no change
      continue
    lGenName1.append(resultantName[:16])
  return lGenName1

def cmd_runTimes(timesToRun=1):
  if isinstance(timesToRun,int):
    if timesToRun < 1:
      print("Requires input to be positive int. Defaulted to 1 iteration.")
      timesToRun = 1
  else:
    print("Requires input to be an int. Defaulted to 1 iteration")
    timesToRun = 1

  lGen1=[]
  for i in range(timesToRun):
    lGen1.extend(genUserName())

  lUniq1= []
  for count in range(len(lGen1)):
    s = lGen1[count].lower()
    s= "".join(s.split())
    if s not in lUniq1:
      lUniq1.append(s)
  return lUniq1

def cmd_selectRandomNames(uInputList,uChoice=1):
  if not (isinstance(uInputList,list) and isinstance(uChoice,int)):
    return None
  if len(uInputList) < uChoice:
    uChoice = len(uInputList)
  sam = random.sample(uInputList, uChoice)
  return sam

def cmd_fileWrite(thingstowrite,fOutput='output.txt', doNotWrite=False):
  if doNotWrite:
    return False
  try:
    f = open(fOutput,"a+")
    if isinstance(thingstowrite,list):
      for i in range(len(thingstowrite)):
        f.write(thingstowrite[i]+"\r\n")
    else:
      f.write(thingstowrite+"\r\n")
    f.close()
    return True
  except Exception as e:
    print("EXCEPTION OCCURED: [", e," ]")
    return False

def cmd_fileRead_rList(fInput='output.txt', doNotRead=False):
  if doNotRead:
    return None
  try:
    f = open(fInput,"r")
    f1=[]
    for x in f:
      wor=x.strip()
      f1.append(wor)
    return f1
  except Exception as e:
    print("EXCEPTION OCCURED: [", e," ]")
    return []

#cmd_fileWrite(cmd_runTimes(5))
#cmd_selectRandomNames(cmd_fileRead_rList(),100)
print(cmd_selectRandomNames(cmd_runTimes(5),100))
