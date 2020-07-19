#
# Your previous JavaScript content is preserved below:
#
# // Click "Settings" in the lower-right corner to set editor preferences
# //
# // Click "Run" in the top-left corner to run your code
# //
# // If you're not comfortable with JavaScript, click the pulldown labeled
# // "JavaScript" near the top-middle and select something different
# //
# // When done, just stop & email your recruiter. There's no "submit" button
# // in CoderPad.
# //
# // Interview question:
# // Write a function that parses and evaluates an arithmetic string
# // Ex. "1+2", "34-5*100", "10-20*30+40/50"
# // Positive integers separated by +, -, * or /. No parentheses
# // You must respect the order of operations: *, / take precedence over +, -
# // Do not use "eval" or 3rd party libraries.
# // There is no timer, but this should take around 60 minutes to get a working // solution. Do not spend more than two hours. Good luck!
# //
#
# 
# MarkedForged Coding Challenge
#By: David Meichle
#Effective time elapsed ~2.5 Hours

import re
operations = ['/', '*', '+', '-'] # in order of precedence

def mathHelper( a,b, operationChar):
  '''
  utility function to compute operation between numbers a and b
  '''
  subAnswer = 0
  a = float(a)
  b = float(b)
  if operationChar == '/':
    subAnswer = a/b
  elif operationChar == '*':
    subAnswer = a*b
  elif operationChar == '+':
    subAnswer = a+b
  elif operationChar == '-':
    subAnswer = a-b
  else:
    subAnswer = 0 #this should not happen
    print("something bad happened")
  print('  mathHelper:  ',a,operationChar,b,'=', subAnswer)
  return float(subAnswer)

def getNumbers(s):
  #regex to split by all operations, is ['/', '*', '+', '-']
  return re.split('\/|\*|\+|\-',s)

def getOperationIndex(operatorTypeList, operation):
  #return the index in the list (including more than one) of where 'operation' exists
  return [i for i,o in enumerate(operatorTypeList) if o == operation]

def resubDivMult(numbers, operatorTypeList, calcInd):
  #substitute the answer of a mult/divide/add/subtract inplace
  subAnswer = 0.0
  subAnswer = mathHelper(numbers[calcInd], numbers[calcInd+1], operatorTypeList[calcInd])
  del(numbers[calcInd+1])
  del(operatorTypeList[calcInd])
  numbers[calcInd] = subAnswer
  return(numbers, operatorTypeList)

def calculate(s):
  numbers = getNumbers(s)
  operatorTypeList = [] #operators inbetween the list of numbers, initially
  #list of what operators are inbetween which numbers
  for (index,c) in enumerate(s):

    if c in operations:
      operatorTypeList.append(c)

  #iterate over operators in preference of '/' '*' '+' '-'
  for op in operations:
    while(op in operatorTypeList): #loop while operator type 'op' still exists
        calcIndicies = getOperationIndex(operatorTypeList, op) #find index in number list to do calculation around
        print('Processing Operation:', op)
        while( len(calcIndicies) != 0): #contuine until all of these operators gone
          print('Number List: ', numbers, 'Operation List: ',operatorTypeList)
          numbers, operatorTypeList = resubDivMult(numbers,operatorTypeList, calcIndicies[0])
          calcIndicies = getOperationIndex(operatorTypeList, op) #update operator index list after substitution

  print('The Answer is: ', numbers[0])
  return numbers[0]
#%%
#Examples:
s = '1+2'
calculate(s)
print("\n\n \tshould read '3'\n\n")

s = '34-5*100'
calculate(s)
print("\n\n \tshould read '-466'\n\n")

s = '10-20*30+40/50'
calculate(s)
print("\n\n \tshould read '-590.8'\n\n")

s = '1 + 1 + 1 + 1 + 1 + 10*10 - 10/2'
calculate(s)
print("\n\n \tshould read '100.0'\n\n")




