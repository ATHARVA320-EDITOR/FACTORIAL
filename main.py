def factorial(x):
    '''function to find factorial'''
    if x==0 or x==1:
        return 1
    else:
        # call function inside
        return x*factorial(x-1)
# display result
print(factorial.__doc__)
print("Factorial of 0:",factorial(0))
print("Factorial of 1:",factorial(1))
print("Factorial of 3:",factorial(3))
print("Factorial of 4:",factorial(4))
print("Factorial of 5:",factorial(5))
print("Factorial of 10:",factorial(10))