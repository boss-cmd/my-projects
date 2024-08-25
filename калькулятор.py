#калькулятор версия 2

what = input( "что делаем?(+,-,*,:): ")

a = float (input("введи первое число: ") )
b = float (input("введи второе число: ") )

if what == "+":
	c = a + b
	print("результат: " + str(c))
elif what == "-":
	c = a - b
	print("результат: " + str(c))
elif what == "*":
	c = a * b
	print("результат: "+ str(c))
elif what == ":":
	c = a / b
	print("результат: "+ str(c))

input()