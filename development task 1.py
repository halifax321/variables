#Alex Bray
#18/09/2014
#Development tasks 1
print("This program will divde two numbers and then display the remainder")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
ans = num1 // num2
ans1 = num1 % num2
print("The floor division answer {0} // {1} is {2}.".format(num1,num2,ans))
print("The remainder is {0} % {1} is {2}.".format(num1,num2,ans1))
