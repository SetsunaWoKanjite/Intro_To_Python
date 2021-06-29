print("Hello World") #Echo Echo Echo
print("Bye World")
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print ("he went to the military  at {0} and his name in {1}".format(age, name))
print ("He is {0} and {0} also {1}".format(name, age))
print (f"{name}dfsjjknfskjngs")
print('a')
print('b')
print('a', end="b")
print('b', end='')
print ("c", end="")
print ("d")
print ('"well will sail the sea"')
print('This is the first line\nThis is the second line')
print(''' wawaaawaawa"shut upe" ''')
print ("This is the first sentence.\
This is the second sentence.")
i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)
print (i)
print (f"{i} and 5")
s = 'This is a string. \
gvyvgv'
print(s)
print ('''2 + 3
5
3 * 5
15 ''')
print ('''    Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!''')
length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

print_max(3, 4)

x = 5
y = 7


print_max(x, y)


x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)