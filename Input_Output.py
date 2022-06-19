# input(prompt) "This function takes exactly  string anything is typed from the keyboard"

'''
num=input("Enter an Number: ")
name=input("Enter your Name: ")
print("User Name: ",name)
print("User Number: ",num)
print("Type of name: ",type(name))
print("Type of num: ",type(num))
'''

# raw_input(prompt) "This function takes exactly what is typed from the keyboard, converts it to string"
'''
num=raw_input("Enter a number: ")
print(num)
'''


from posixpath import split
import string


#using split() function
'''
x,y=input(),split()
print("x: ",x)
print("Y :",y)
'''


#using end
'''
print("salt",end='@')
print("Pepper")
'''


#Using split() method : 
'''
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print("Firt number is {} and Second number is {}".format(x,y))

x=list(map(int,input("Enter variable: ").split()))
print("Multiple variable: ",x)
'''


#Using List comprehension : 
'''
x,y=[int(x) for x in input("enter value:").split()]
print("x: ",x)
print("y: ",y)

x=[int(x) for x in input("enter value:").split()]
print("x: ",x)
'''

#Normal Method Python: (Python 2.7) 
'''
N=int(input("enter an number: "))
arr=[int(x) for x in input().split()]
summation=0
for x in arr:
    summation +=x
    
print("Summation: ",summation)
'''
#A bit faster method using inbuilt stdin, stdout: (Python 2.7) 
'''
from sys import stdin,stdout
def main():
    N=stdin.readline()
    arr=[int(x) for x in stdin.readline().split()]
    sum=0
    for x in arr:
        sum +=x

    stdout.write(str(sum))
    stdout.write("\n")

if __name__=="__main__":
    main()
'''
#When you want to take input of particular integers of integers given in a single line
'''
from sys import stdin,stdout
def get_ints():
    return map(int,stdin.readline("Enter value : ").strip().split())
a,b,c,d=get_ints()

 
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

arr= get_ints()

import sys
def get_string(): return sys.stdin.readline().strip()
strting=get_string()
print("String: ",string)
'''

'''
import random
random_num=random.randint(0,500)
while True:
    myNum=input("Enter a number: ")
    if random_num==myNum:
        print("You win")
        break
    else:
        print("You lose")
        continue
'''
print("19","June","2022",sep="-")