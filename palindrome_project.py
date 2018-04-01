# Create the list from the input
pal = input('Please enter a word: ')
# Convert the list to a string
pal = str(pal)
# Reverse the string
rvs = pal[::-1]
# Compare the results
if pal == rvs:
  print('This is a palindrome, front side = %s and reverse is %s'%(pal,rvs))
else:
  print('This isn\'t a palindrome, front side = %s and reverse is %s'%(pal,rvs))


"""
[::-1] - first colon reads the whole list, second colon reads the list backwards and lists the individual items in the list. -2 would list every second, -3 every third, etc.
"""
