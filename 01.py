import os
import time
import math

os.system("cls")
print (""" .d88b.  d8888b. d88888b d8888b.  .d8b.   .o88b. d888888b  .d88b.  d8b   db d88888b .d8888. 
.8P  Y8. 88  `8D 88'     88  `8D d8' `8b d8P  Y8   `88'   .8P  Y8. 888o  88 88'     88'  YP 
88    88 88oodD' 88ooooo 88oobY' 88ooo88 8P         88    88    88 88V8o 88 88ooooo `8bo.   
88    88 88~~~   88~~~~~ 88`8b   88~~~88 8b         88    88    88 88 V8o88 88~~~~~   `Y8b. 
`8b  d8' 88      88.     88 `88. 88   88 Y8b  d8   .88.   `8b  d8' 88  V888 88.     db   8D 
 `Y88P'  88      Y88888P 88   YD YP   YP  `Y88P' Y888888P  `Y88P'  VP   V8P Y88888P `8888Y' 
                                                                            """)
time.sleep(3)
os.system("cls")

print ("*************************************************")
print ("1.-Suma")
print ("2.-Resta")
print ("3.-Multiplicacion")
print ("4.-Division")
print ("5.-Potencia")
print ("6.-Raiz")
print ("7.-Funcion Cuadratica")
print ("8.-Formula General")
print ("0.-Salir")
print ("*************************************************")
menu = input("Elige la OPCION: ")
print (menu)
os.system("cls")
if menu == 1:
	os.system("cls")
	suma1 = input("Inserta numero 1: ")
	print (str(suma1) + " + x = ?")
	suma2 = input("Inserta numero 2: ")
	print (str(suma1) + " + " + str(suma2) + " = ?")
	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	resultado_suma = suma1 + suma2
	print ("RESULTADO: " + str(resultado_suma))
	time.sleep(3)
if menu == 2:
	os.system("cls")
	resta1 = input("Inserta numero 1: ")
	print (str(resta1) + " - x = ?")
	resta2 = input("Inserta numero 2: ")
	print (str(resta1) + " - " + str(resta2) + " = ?")
	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	resultado_resta = resta1 - resta2
	print ("RESULTADO: " + str(resultado_resta))
	time.sleep(3)
if menu == 3:
	os.system("cls")
	multi1 = input("Inserta numero 1: ")
	print (str(multi1) + " * x = ?")
	multi2 = input("Inserta numero 2: ")
	print (str(multi1) + " * " + str(multi2) + " = ?")
	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	resultado_multi = multi1 * multi2
	print ("RESULTADO: " + str(resultado_multi))
	time.sleep(3)
if menu == 4:
	os.system("cls")
	div1 = input("Inserta numero 1: ")
	print (str(div1) + " / x = ?")
	div2 = input("Inserta numero 2: ")
	print (str(div1) + " / " + str(div2) + " = ?")
	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	resultado_div = div1 / div2
	print ("RESULTADO: " + str(resultado_div))
	time.sleep(3)
if menu == 5:
	os.system("cls")
	pote1 = input("Inserta numero 1: ")
	print (str(pote1) + " ** x = ?")
	pote2 = input("Potencia: ")
	print (str(pote1) + " ** " + str(pote2) + " = ?")
	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	resultado_pote = pote1 ** pote2
	print ("RESULTADO: " + str(resultado_pote))
	time.sleep(3)
if menu == 6:
	os.system("cls")
	raiz1 = input("Numero de Raiz: ")
	time.sleep(3)
	resultado_raiz = math.sqrt(raiz1)
	print ("RESULTADO: " + str(resultado_raiz))
	time.sleep(3)
if menu == 7:
	os.system("cls")
	eca = input("Inserta numero A: ")
	print (str(eca) + " ?x + ? = ?")
	ecb = input("Inserta valor de B: ")
	print (str(eca) + str(ecb) + "x + ? = ?")
	ecc = input("Inserta valor de C: ")
	print (str(eca) + str(ecb) + "x " + str(ecc) + " = ?")

	print ("ESPERA UN MOMENTO")
	time.sleep(3)
	os.system("cls")
	resultado_ec1 = -(ecb) / 2*eca
	print ("RESULTADO VERTICE X: " + str(resultado_ec1))
	resultado_ec2 = (resultado_ec1 ** 2) + (ecb * resultado_ec1) + (ecc)
	print ("RESULTADO VERTICE Y: " + str(resultado_ec2))
	resultado_dis= ecb**2 - 4*eca*ecc
	print ("RESULTADO DISCRIMINANTE: " + str(resultado_dis))
	resultado_ec3 = (-ecb+math.sqrt(ecb**2-4*eca*ecc))/(2*eca)
	print ("RESULTADO X1: " + str(resultado_ec3))
	resultado_ec4 = (-ecb-math.sqrt(ecb**2-4*eca*ecc))/(2*eca)
	print ("RESULTADO X2: " + str(resultado_ec4))
	time.sleep(3)
if menu == 8:
	os.system("cls")
	a = input("Introduce Valor de A: ")
	b = input("Introduce Valor de B: ")
	c = input("Introduce Valor de C: ")
	os.system("cls")
	resultado_discr = b**2-4*a*c
	print ("Resultado Discriminante: " + str(resultado_discr))
	resultado_8 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
	print ("El resultado X1: " + str(resultado_8))
	resultado_81 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
	print ("El resultado x2: " + str(resultado_81))
if menu == 0:
	os.system("exit")