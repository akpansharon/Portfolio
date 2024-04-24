#Counting to Twenty
for i in range (1,21):
    print(i)
    
#One Million
list = list(range(1, 1001))
print(list)

#Summing a Million  
print(sum(list))
print(min(list))
print(max(list))

#Odd Number
for odd in range (1,20,2):
    print(odd)

#Threes
for three in range (3,33,3):
    print(three)
    
#Cube
cube =[]
for value in range(1,11):
    cube.append(value**3)
print(cube)

#Cube Comprehension
cube1 = [value**3 for value in range(1,11)]
print(cube1)