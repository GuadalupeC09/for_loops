#Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):
    print(x)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for z in range(1,101):
    if z%10 == 0:
        print("Coding Dojo")
    elif z%5 == 0:
        print("Coding")
    else:
        print(z)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0 
for x in range(1,500001,2):
    sum += x 
print(sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for number in range(2018,0,-4):
    print(number)

#Flexible Counter Set three variables: lowNum, highNum, mult.
lowNum = 2
highNum = 9
mult = 3

for number in range(lowNum, highNum+1):
    if number % 3 ==0:
        print(number)




