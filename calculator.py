#program to make a simple calculator

#This function adds two number
def add(a,b):
    return a + b

#This function subtracts two number
def subtract(a,b):
    return a-b

#This function Multiplys two number
def multiply(a,b):
    return a*b

#This function divides two number
def divide(a,b):
    return a/b


print("Select Operation:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

while True:
    choice = input("Enter Choice(1/2/3/4)")
    
    
    if choice in ('1' , '2' , '3' , '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:"))
        
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
        break
    else:
        print("Invalid Input")
        