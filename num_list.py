spam = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []

for i in spam:
  even.append(i % 2 == 0)
print(even)

evens = [elem for elem in spam if elem % 2 == 0]
print(evens)
