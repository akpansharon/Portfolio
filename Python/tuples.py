#Tuple - values that cannont change (immutable), an imutable list is a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 trying to alter an immutable list
for dimension in dimensions:
    print(dimension)
    
#write over a tuple
dimensions = (400, 100)
print('\nModify Dimensions: ')
for dimension in dimensions:
    print(dimension)
    

