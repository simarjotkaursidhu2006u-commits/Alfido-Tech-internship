def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def floordiv(a,b):
    return a//b 
print("    CALCULATOR   ")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
op=str(input("Enter the operation to perform"))
if(op=="+"):
    print(add(a,b))
elif(op=="-"):
    print(sub(a,b))
elif(op=="*"):
    print(mul(a,b))
elif(op=="/"):
    print(div(a,b))
elif(op=="%"):
    print(mod(a,b))
elif(op=="//"):
    print(floordiv(a,b))
else:
    print("Enter a valid operation!")
