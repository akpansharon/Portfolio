for value in range (1, 6):
    print(value)
for value in range(10):
    print(value)

numbers = list(range(1, 6))
print(numbers)

#even numbers
even_number  = list(range(2, 11, 2))
print(even_number)

#square numbers
squares = []
for value in range(1, 11):
    sqaure = value ** 2
    squares.append(sqaure)
print(squares)

#square number 2
squares1 = []
for value in range(1,20):
    squares1.append(value ** 2)
print(squares1)

#simple statistics with a list of numbers:
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
sqaures2 = [value**2 for value in range(1, 11)]
print(sqaures2)

