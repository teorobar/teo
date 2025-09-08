# File: homework1.py

# --- Variables and Data Types ---

'''
a=10
print(a)
print(type(a)) # a is an int, or integer, a whole number with no decimals

b=1.5
print(b)
print(type(b)) # b is a float, or floating-point number, a number with a decimal point or a fraction

c=3j
print(c)
print(type(c)) # c is a complex, or complex number, a number with a real component and an imaginary component

d="hello"
print(d)
print(type(d)) # d is a str, or string, a sequence of letter or characters contained in quotes

e=[1,2,3]
print(e)
print(type(e)) # e is a list, a sequence of various data types enclosed in brackets

f={"name":"Ellen","favorite fruit":"strawberry"}
print(f)
print(type(f)) # f is a dict, or dictionary, a list of pairs of data enclosed in curly braces

g=(1,2)
print(g)
print(type(g)) # g is a tuple, a sequence of various data types enclosed in parentheses that are not changeable

h=["apple","bananna","strawberry"]
print(h)
print(type(h)) # h is a list, a sequence of various data types enclosed in brackets

i=True
print(i)
print(type(i)) # i is a bool, or boolean, representing a binary True or False

j=None
print(j)
print(type(j)) # j is a nonetype, representing the absence of any value

k=[True,"blue",12]
print(k)
print(type(k)) # k is a list, a sequence of various data types enclosed in brackets

l=str(14) # note: str() was sued to convert the int 14 into its corresponding string form
print(l)
print(type(l)) # l is a str, or  string, a sequence of letter or characters contained in quotes

m=1e4 # note: python interprets <a>e<b> as scientific notation
print(m)
print(type(m)) # m is a float, or floating point number, a number with a decimal point or a fraction

# Question 5
n=range(6)
print(n)
print(type(n)) # n is a range, a sequence of integers 0 through n-1
'''

'''
1. I found 9 unique data types.
2. int, float, complex, str, list, dict, tuple, bool, and nonetype.
3. b and m are both floats. e, h , and k are all lists. d and l are both strings.
4. l is a string. It is not an integer because it was defined using str(), which turns a data type into its corresponding string form.
5. (See Question 5 or n)
'''

# --- Booleans ---

print(10>9) # True, 10 is greater than 9

print(10==9) # False, 10 does not equal 9

print(10<=9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, not empty set

print(bool(123)) # True, non-zero number

print(bool(["apple","cherry","banana"])) # True, not empty set

print(bool(True)) # True, defined to be True

print(bool(False)) # False, defined to be False

print(bool(0)) # False, 0 is synonymous to False

print(bool("")) # False, empty set

print(bool(" ")) # True, not empty set

print(bool(())) # False, empty set

print(bool([])) # False, empty set

print(bool({})) # False, empty set

print(bool(True and False))

print(bool(True and True))

print(bool(False and False))

print(bool(True or False))

print(bool(True or True))

print(bool(False or False))

print(bool(not(False)))

print(bool(not(True)))