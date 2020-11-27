def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		

	try:
		return num1/num2
	except ZeroDivisionError:
		print("Can't divide by 0")
		return("Error Operation")
	

op1=(int(input("Introduce el primer nmero: ")))

op2=(int(input("Introduce el segundo nmero: ")))		
	
operacion=input("Introduce la operacin a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacin no contemplada")


print("Operacin ejecutada. Continuacin de ejeccin del programa ")