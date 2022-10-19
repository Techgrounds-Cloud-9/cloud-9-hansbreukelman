# PRG-Bonus Pls fix
Fixing problems in different python codes

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
### Sources
No sources needed

### Overcome challenges
No challenges

## Results

### 1.py
```
'''
The output should be:
hello Casper
hello Floris
hello Esther
'''
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(loo,name)
'''
```
```
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(foo,name)
# foo was spelled wrong in the print line
```
#
### 2.py

```
'''
The output should be:
100
'''
foo = 20
bar = '80'
print(foo + bar)
```
```
foo = 20
bar = 80
print(foo + bar)
# The number 80 was considered a string because it was enclosed in parentheses
```
#
### 3.py
```
'''
The output should be:
30
'''
foo = 20
for i in range(10):
	foo -= 1

print(foo)
```
```
foo = 20
for i in range(10):
	foo += 1

print(foo)
# the minus should be a plus
```
#
### 4.py
```
'''
The output should be:
there are 0 kids on the street
there are 1 kids on the street
there are 2 kids on the street
there are 3 kids on the street
there are 4 kids on the street
'''
foo = 0
while foo <= 5:
	print('there are', foo, 'kids on the street')
	foo += 1
```
```
foo = 0
while foo <= 4:
	print('there are', foo, 'kids on the street')
	foo += 1
    # The 5 has to be an 4
```
#
### 5.py
```
'''
The output should be:
Star Wars
'''
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[4])
```
```
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[3])
# In the list, you start counting at 0, so the 4 must be a 3
```
#
### 6.py
```
'''
The output should be:
80
'''
foo = 80
if foo < 30:
	print(foo)
else:
	print('big number wow')
elif foo < 100:
	print(foo)
```
```
foo = 80
if foo < 30:
	print(foo)
elif foo < 100:
    print(foo)
else:
    print('big number wow')
# elif comes immediately after the if statement, else is last.
```
#
### 7.py
```
'''
The output should be:
['Dog', 'Cat', 'Fly']
'''
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
	short_names = []

print(short_names)
```
```
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']

short_names = []
for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
	# short_names = [] this one was not needed

print(short_names)
```
#
### 8.py
```
'''
The output should be:
20
'''
foo = 10
bar = 2
print(foo**bar)
```
```
foo = 10
bar = 2
print(foo*bar) 
# there was an '*' to much
```
#
### 9.py
```
'''
The output should be:
0
1
2
3
4
8
9
'''
for i in range(10):
	if i < 5:
		print(i)
	elif i < 8:
		break
	else:
		print(i)
```
```
for i in range(10):
	if i < 5:
		print(i)
	elif i < 8:
		continue
	else:
		print(i)
# instead of if break it should be continue
```
#
### 10.py
```
'''
The output should be:
the number is 20
'''
print('the number is' + 20)
```
```
print('the number is', 20)
# Instead of the '+ 20' I did a comma
```
#
### 11.py
```
'''
The output should be:
IT LIVES!
'''
dev monster():
	print('IT LIVES!')

monster()
```
```
def monster():
	print('IT LIVES!')

monster()
# dev should be def
```
#
### 12.py
```
'''
The output should be:
4
16129
'''
def square(x):
	return x**2

nr = square(2)
print(nr)

big = square(foo)
print(big)

foo = 127
```
```
def square(x):
	return x**2

nr = square(2)
print(nr)

foo = 127

big = square(foo)
print(big)
# the foo statement should be above the 'big = square(foo)' statment
```
#
### 13.py
```
'''
The output should be:
Your random number is: <insert random number here>
'''
import random

random.randint(1,100)
print("Your random number is:")
```
```
import random

number = random.randint(1,100)
print("Your random number is:", number)
# you have to make an statmenet of thet random.randit and use it in the print line
```
#
### 14.py
```
'''
The output should be:
True
'''
def rtn(x):
	return(x)

foo = rtn(3)

if foo > rtn(4):
	print(True)
else:
	print(False)
```
```
def rtn(x):
	return(x)

foo = rtn(3)

if foo < rtn(4):
	print(True)
else:
	print(False)
# the arrow has to point left for 'lower then' instead of right
```
#
### 15.py
```
'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''
foo = ''
for i in range(3):
	foo += 'a'
	for j in range(3):
		foo += '5'
	for k in range(3):
		foo += '|'

print(foo)
```
```
foo = ''
for i in range(3):
    foo += 'a'
    for j in range(3):
        foo += '5'
        for k in range(3):
            foo += '|'

print(foo)

# the strings and statements weren't good aligned
```
#
### 16.py
```
'''
The output should be:

'''
import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
	try:
		# ask for input
		inpt = int(input("Please input a number between 1 and 100: "))
		# count attempt as a try
		tries += 1

		# check for match
		if inpt == goal:
			win = True
			print("Congrats, you guessed the number!")
			print("It took you", tries, "tries")
		# give hints
		elif inpt < goal:
			print("The number should be higher")
		else:
			print("The number should be lower")

	except:
		print("Please type an integer")

# 
if win == False:
	print("Game over! You took more than seven tries")

# This one is just fine!

```


