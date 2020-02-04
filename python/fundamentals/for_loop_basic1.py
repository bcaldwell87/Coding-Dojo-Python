#  Basic - Print all integers from 0 to 150.
def basic():
    for i in range(151):
        print(i)

basic()

#Print all the multiples of 5 from 5 to 1,000
def multiples_of_five():
    for i in range(5,1001,5):
        print(i)

multiples_of_five()

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

counting()

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def woah_huge():
    sum = 0
    for i in range(1, 500000, 2):
        sum += i
        print(sum)

woah_huge()

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    print(x)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)
lowNum = 1
highNum = 50
mult = 4
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)