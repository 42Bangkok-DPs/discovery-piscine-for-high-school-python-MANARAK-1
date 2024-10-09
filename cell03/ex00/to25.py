#!/usr/bin/env python3

a = int(input("Enter a number below 25\n"))
if a > 25 :
    print("Error")
while a < 26 :
    print("Inside the loop, my variable is", a)
    a += 1
