# 1) sqaure root
# n=int(input("enter n : "))

# through exponention
# print(f"square root of {n} is : ",n**(1/2))

# math module
# import math
# print(f"sqaure root of {n} is : ",math.sqrt(n))


# 2) area of traingle
# formula = 1/2 *b*h
# h=float(input("enter height : "))
# b=float(input("enter base : "))
# area = (1/2)*b*h
# print(f"Area of triangle is: {area}")

# 3) swap two variable in python
# a=int(input("enter a : "))
# b=int(input("enter b : "))
# a=a+b
# b=a-b
# a=a-b
# print(f" a : {a}")
# print(f" b: {b}")


#4) convert km to miles
# 1 km = 0.621371 mix
# 1 mi = 1.609344 km(1.6 km)
# a=int(input("enter km : "))
# ans = float(a/1.6)
# print(f"the coversion of {a} km in miles is : {ans} miles")



# 5) generate random number
# import random
# list=[1,2,3,4,5]
# r= random.choice(list)
# print(r)


# 6) all prime number

# a=int(input("enter a : "))
# b=int(input("enter b : "))

# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,num):
#            if num%i==0:
#                break
#         else:
#                print(num)

# 7) fah to celsius
# c=(f-32)*5/9
# a=int(input("enter fah : "))
# cel = (a-32)*5/9
# print(f"{a} Fahrenheit equal to {cel} Celsius ")


# 8) fibonacci sequnce
# 0,1,(0+1)=1,(1+1=2),(2+1=3)........
# num=int(input("enter num : "))
# print("0 1")
# a=0
# b=1

# for i in range(1,num+1):
#     c=a+b
#     a=b 
#     b=c
#     print(f"{c}")
    

# 9) armstrong number
# 1 5 3 
# (1*1*1)+(5*5*5)+(3*3*3)
# 1+127+27=153

# num=int(input("enter num : "))
# num2=int(input("enter num2 : "))
# for num in range(num,num2+1):
#     order = len(str(num))
#     sum=0
#     temp=num
#     while temp>0:
#         # 3
#         digit =  temp%10  
#         # 27
#         cube=digit**order
#         # add sum
#         sum=sum +cube
#         # floor divide
#         temp=temp//10   
#     if num==sum:
#         print(num)


# 10)  decimal to octal hexadecimal binary
# dec=int(input("enter num : "))
# print("binary : ",bin(dec))
# print("octal : ",oct(dec))
# print("hexadecimal : ",hex(dec))

# 11) ascii value
# char = "a"
# print("the ascii value of : ",char,"is",ord(char))



# 12) find HCF or GCD

def findHCF(a,b):
    if a > b :
        small = b
    else :
        small= a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf = i
    return hcf

print("HCF is : ",findHCF(64,45))


# 13)  find LCM
def LCM():
    if 12>20:
        print("hello")
    else:
        print("hello world")
print("nice")
print("hello")


