"This builds on my skills with lists"

#4.3 For Loop
for value in range(1,21):
    print(value)

#4.45 List Statistics
numbers = list(range(1,101))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6 Odd Numbers, the third argument in the function is the step
for value in list(range(1, 21, 2)):
    print(value)

#4.7 Multiples of Three
for value in list(range(3, 31, 3)):
    print(value)

#4.8 List of Cubes - Need to Fix
#cubes = []
#for value in range(1,11):
#    cube = value**2
#    print(cubes.append(cube))

#4.9 List Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)

#4.10 Slices
random = [1, 2, 1, 2, 1, 2, 1, 2, 5, 2]

print("The first three items in the list are:")
print(random[0:3])

print("The middle three items in the list are:")
print(random[4:7])

print("The last three items in the list are:")
print(random[-3:])

#4.11 Pizzas
pizzas = ['cheese', 'pesto', 'hawaiian']
friend_pizzas = pizzas[:]
friend_pizzas.append('pep')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's fav pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4.13 Buffet (tuples)
foods = ('wings', 'coffee', 'eggs', 'grits', 'bacon')
new_foods = ('wings', 'coffee', 'eggs', 'grits', 'bacon', 'burger', 'jello')
for food in new_foods:
    print(food)
