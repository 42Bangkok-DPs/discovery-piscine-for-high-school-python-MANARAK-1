print("Enter the first number:")
a = int(input())
print("Enter the second number:")
b = int(input())
print (a, "x", b, "=", a * b)
if a * b > 0 :
    print("The result is positive.")
elif a * b < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")