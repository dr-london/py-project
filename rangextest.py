num = int(input('Please choose a number to divide: ')) #'int' converts the input to a number aka integer

listRange = list(range(1, num + 1)) #num + 1 sets the range to be +1 of the input

divisorList = [] # defines 'divisorList' as a list

for number in listRange: # for all the numbers in 
    if num % number == 0:
        divisorList.append(number) # all numbers that evenly divide into the input get added (appended) to the list

print(divisorList) # prints the list
