def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print('select operation.')
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')

while True:
    operation = input("enter the operation number(1/2/3/4):")
    if operation in ('1','2','3','4') :
        try:
            num1 = float(input('enter the first number:'))
            num2 = float(input('enter the second number:'))
        except ValueError:
            print("invalid input.please enter a number:")    
            continue
        if operation == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif operation == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif operation == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif operation =='4':
            print(num1,"/",num2,"=",divide(num1,num2))
        else:
            print('invalid')
            
print("____________________________________________________________")



