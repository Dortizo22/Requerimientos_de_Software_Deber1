# Nombre: David Josue Ortiz Ochoa
# Curso: Tercer semestre de Ingenieria de Software A1

# Tipos de Datos y Acciones elementales 
# Ejercicio 1

Lista = ("Hola Mundo", "" , "Verdadero", "1", "c", "256", "8>19" )
print(Lista)

#Respuesta: En una colecciòn se guardarìa esos datos

#Ejercicio 2

#ejemplo
resultado = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(resultado)
print(type(resultado))

#Respuesta: El resultado estaria guardado en una variable de tipo Flotante (Float)

#Ejercicio 4

n1 = 5
n2 = 7

suma = n1 +n2 
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
modulo = n1 % n2

print(suma)
print(resta)
print(multi)
print(div)
print(modulo)

# Ejercicio 5
import math

a = 5
b = 7
c = 9

#Formula General
disc = b * b - 4 * a * c
raiz = math.sqrt(disc)
#Raices discriminantes
x_1 = (-b + raiz) / (2 * a)
x_2 = (-b - raiz) / (2 * a)

print("Las soluciones son: ", x_1 , x_2)

#Ejercicio 6 

c1 = 5
c2 = 7

hipotenusa = math.sqrt((c1**2) + (c2**2))
print("Hipotenusa: ", hipotenusa)


#Ejercicio 7

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("0")
else:
    print("1")

#Ejercicio 9

lista=[]
for x in range(4):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

repeticion = lista.count(1)
if repeticion % 2 == 0:
    print("El codigo de paridad es 1")
else:
    print("El codigo de paridad es 0")

#Ejercicio 10

numero_binario = int(input("Ingrese un numero binario de 4 digitos"))

numero_decimal = 0 

for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion

print("El número decimal que buscamos es: ", numero_decimal)

#Ejercicio 11

numero = int(input("Ingrese un numero entero de 4 digitos: "))
umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("Unidades de millar: %i" % umil)
print("Centenas: %i" % centenas)
print("Decenas: %i" % decenas)
print("Unidades: %i" % unidades)

#Estructuras De Control de Flujo de Datos

#Ejercicio 1

año = 0
lista_1 = []
def string_int(mi_info):
    for i in mi_info:
        lista_1.append(int(i))

pedir_fecha = input("Ingrese fecha en formato (ddmmaaaa): ")
string_int(pedir_fecha)

a = lista_1[7]
b = lista_1[6]
c = lista_1[5]
d = lista_1[4]

if año % 4 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")

#Ejercicio 2

lista_2 = []

def string_int(mi_info):
    for i in mi_info:
        lista_2.append(int(i))

pedir_num = input("Ingrese un numero entero de 5 digitos: ")
string_int(pedir_num)

a = lista_2[0]
b = lista_2[1]
c = lista_2[2]
d = lista_2[3]
e = lista_2[4]

if a == e:
    if b == d:
        print("EL numero ingresado es capicùa")
    else:
        print("EL numero ingresado no es capicùa")
else:
    print("EL numero ingresado no es capicùa")
    

#Ejercicio 3

h = int(input("Ingrese la cantidad de horas: "))
m = int(input("Ingrese la cantidad de minutos: "))

h_a_s = h * (3600)
m_a_s = m * (60)
total = h_a_s + m_a_s

print("El total de segundos es: ", total)

#Ejercicio 4

s = int(input("Ingrese la cantidad de segundos: "))

if s > 0 :
    m = s / 60
    h = s / 3600
    dias = s / 86400

    print("\n La cantidad de minutos es: ", m)
    print("\n La cantidad de horas es: ", h)
    print("\n La cantidad de dias es: ", dias)
else:
    print("Ingrese una cantidad de segundos validos")

#Ejercicio 5

A = int(input("Ingrese el primer numero entero positivo: "))

if A > 0 :
    B = int(input("Ingrese el el segundor numero entero positivo: "))
    if B > 0 :
        C = int(input("Ingrese el Tercer numero entero positivo: "))
        if C > 0:
            if A > B and A > C:
                print("\n El numero mayor es: ", A)
                if B > C:
                    print("\n El segundo mayor es: ", B)
                else:
                    print("\n El segundo mayor es: ", C)
            elif B > A and B > C:
                print("\n EL numero mayor es: ", B)
                if A > C:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", C)
            elif C > A and C > B:   
                print("\n EL numero mayor es: ", C)
                if A > B:
                    print("\n El segundo mayor es: ", A)
                else:
                    print("\n El segundo mayor es: ", B)
            else:
                print("No se ha podido deteerminar el mayor de los 3 numeros")                
        else:
            print("Por favor ingrese un numero entero positivo")  
    else:
        print("Por favor ingrese un numero entero positivo")          
else:
    print("Por favor ingrese un numero entero positivo") 

#Ejercicio 6

H_e = int(input("Ingrese de hora en formato de 12 en la que se estaciono: "))
if H_e >= 0 and H_e <= 12:   
    M_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if M_e >= 0 and M_e < 60: 
        AM_PM_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if AM_PM_e == "A" or AM_PM_e == "P" :
            H_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if H_s >= 0 and H_s <= 12:
                M_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if M_s >= 0 and M_s < 60:
                    AM_PM_s = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if AM_PM_s == "A" or AM_PM_s == "P" :
                        if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "A" and AM_PM_s == "P" or AM_PM_e == "P" and AM_PM_s == "P":
                            if AM_PM_e == "A" and AM_PM_s == "A" or AM_PM_e == "P" and AM_PM_s == "P":
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                            elif AM_PM_e == "A" and AM_PM_s == "P":
                                H_s+=12
                                resta_H = H_e - H_s
                                Total_H = resta_H * 4
                                resta_M = M_e - M_s
                                Total_M = resta_M/30
                                Total_M_2 = 0
                                if Total_M < 0 :
                                    Total_M_2 = 2.50
                                    Total_T = Total_H + Total_M_2
                                    print("El Valor a pagar es: Bs", Total_T)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

#Ejercicio 7

L = float(input("Ingrese su peso en Libras: "))
C = int(input("Ingrese su Altura en Centimetros: "))

P = L*0.453592
A = C /100

promedio = P/(A * A)

print("Su peso en Kg es: ", P)
print("Su altura en Metros es: ", A)
print("Su promedio es: ", promedio)

if promedio < 16 :
    print("Su categoria es Criterio de ingreso.")
elif promedio >= 16 and promedio <= 16.9:
    print("Su categoria es infra peso.")
elif promedio >= 17 and promedio <= 18.4:
    print("Su categoria es bajo peso.")
elif promedio >= 18.5 and promedio <= 24.9:
    print("Su categoria es peso normal.")
elif promedio >= 25 and promedio <= 29.9:
    print("Su categoria es sobrepeso.")
elif promedio >= 30 and promedio <= 34.9:
    print("Su categoria es obesidad pre-mórbida.")
elif promedio >= 40 and promedio <= 45:
    print("Su categoria es obesidad mórbida.")
elif promedio > 45 :
    print("Su categoria es obesidad híper-mórbida.")


#Ejercicio 8

d = int(input("Ingrese un dia correspondiente al 2014: "))
if d > 0 and d < 31:
    m = int(input("Ingrese un numero de mes correspondiente al 2014: "))
    if m > 0 and m <=12 :
        diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        i = 0
        acumulador = 0
        while i <= m - 1:
            acumulador = acumulador + diasMes[i]
            i = i + 1
        total = acumulador + d
        print("\n EL total de dias que han transcurrido desde el 1 de enero del 20154 hasta la fecha que solicito es: ", total)

#Ejercicio 9

m = int(input("Ingrese un numero entre el 1 y el 12: "))
if m > 0 and m <= 12 :
    if m == 1 :
        print("Enero")
    elif m ==2 :
        print("Febrero")
    elif m ==3 :
        print("Marzo")
    elif m ==4 :
        print("Abril")
    elif m ==5 :
        print("Mayo")
    elif m ==6 :
        print("Junio")
    elif m ==7 :
        print("Julio")
    elif m ==8 :
        print("Agosto")
    elif m ==9 :
        print("Septiembre")
    elif m ==10 :
        print("Octubre")
    elif m ==11:
        print("Noviembre")
    elif m ==12 :
        print("Diciembre")       
else:
    print("Ingrese un numero valido")

#Ejercicio 10 

c = float(input("Ingrese la cantidad a pagar en el almacen: "))

if c > 1000:
    total = c * 0.80
    print("SU total a pagar aplicando el descuento de la tienda es de: Bs", total)
else:
    print("Su total a pagar es de: Bs", c)

#Estructuras Iterativas

#Ejercicio 1

import math
n = int(input("ingrese un numero entero: "))
if n > 0:
    digitos = int(math.log10(n))+1
    print(digitos)
elif n == 0:
    digitos = 1
    print(digitos)
elif n < 0:
    print("Ingrese un numero valido")

#Ejercicio 2

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

def capicua(numero):
    return numero == invertir_numero(numero)

numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for numero in numeros:
    es_capicua = capicua(numero)
    print(f"El número {numero} es capicúa? {es_capicua}")

#Ejercicio 3

def es_primo(num):
    contador = 0

    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
    
    if contador == 2:
        print("Es un numero primo")
        return True
    else:
        print("No es un numero primo")
        return False
n = int(input("Ingrese un numero primo positico: "))
if n > 0:
    print(es_primo(n))  

#Ejercicio 4:

n = int(input("Ingrese un numero entero: "))
if n >= 0 :
    x = 1
    f = 1
    while x <= n:
        f = f *x 
        x += 1
    print("El factorial de ",n," es: ",f)
else:
    print("No se pudo calcular el factorial")

#Ejercicio 5:

def validar(valor):
    	return False

valido = 0
while not valido:
    password = input("Introduzca una contraseña con al menos 10 digitos: ")
    valido = len(password) >= 10
print("\n Felicidades has ingresado una contraseña valida")

# EJERCICIO 6

def secuencia_menor_mayor():
    ingresa = True
    lista = []
    while ingresa:
        valor = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
        if valor == 0:
            break
        else:
            lista.append(valor) 
    print(lista)
    print(u'Menor %s' % min(lista)) 
    menor = lista[0] 
    mayor = lista[0] 
    for elemento in lista: 
        if elemento < menor: 
            menor = elemento
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print(u'Menor %s' % menor)
    print(u'Mayor %s ' % max(lista))
    print(u'Mayor %s ' % mayor)




# EJERCICIO 7

def resultado_secuencia(lista): 
    claves = len(lista) 
    edad = 0
    estatura = 0
    peso = 0
    personas_18_25 = 0
    personas_18_35 = 0
    personas_36 = 0
    peso_18_35 = 0
    for d in lista: 
        edad += float(d['edad']) 
        peso += float(d['peso'])
        estatura += float(d['estatura'])
        ## CONDICIONALES
        if 18 <= float(d['edad']) <= 25:
            personas_18_25 += 1 ## CONTADOR DE PERSONAS ENTRE 18 Y 25
        if 18 <= float(d['edad']) <= 35:
            personas_18_35 += 1 ## CONTADOR DE PERSONAS ENTRE 18 Y 35
            peso_18_35 += float(d['peso']) ## ACUMULA VALORES
        if float(d['edad']) > 36:
            personas_36 += 1 # CONTADOR DE PERSONAS MAYORES DE 36
    print(u'Edad promedio de todas las personas: %s' % round((edad / claves), 0))
    print(u'Peso promedio de todas las personas: %s' % (peso / claves))
    print(u'Estatura promedio de todas las personas: %s' % (estatura / claves))
    print(u'Personas con edad entre 18 y 25: %s' % personas_18_25)
    print(u'Personas mayores a 36: %s' % personas_36)
    print(u'Promedio peso personas 18 a 35: %s' % (peso_18_35 / personas_18_25))

def estudio():
    ingresa = True
    lista = []
    datos = {}
    while ingresa: ## MEDIANTE WHILE SE SOLICITA INGRESO DE DATOS, FINALIZA EN CASO DE INGRESAR UN 0
        edad = int(input("Ingresa la edad  o 0 para finalizar, debe ser un valor entero: "))
        if edad == 0:
            break
        peso = float(input("Peso 0 para finalizar, debe ser un valor numerico: "))
        if peso == 0:
            break
        estatura = float(input("Estatura 0 para finalizar, debe ser un valor numerico: "))
        if estatura == 0:
            break
        datos = {'edad': edad, 'peso': peso, 'estatura': estatura}
        lista.append(datos)
    resultado_secuencia(lista)

#Ejercicio 8
numero = 1
x = 1
while x <= 10: 
    for i in range(1, 11):
        print(f"{i} x {numero} = { i * numero}")
    numero+=1
    x+=1

# EJERCICIO 9
def domino():
    #fichas = int(input("Fichas: "))
    #solucion = piramide(fichas)
    #print(solucion[0], solucion[1])
    #### PARA REALIZAR EL DOMINO, ES NECESARIO INCLUIR UN FOR DENTRO DE OTRO
    for i in range(1, 28):
        for j in range(i, 28):
            print("{}:{}".format(i, j))


# EJERCICIO 10
def promedio_serie():
    import statistics
    ingresa = True
    lista = []
    while ingresa: ### EL WHILE INDICA HASTA QUE PUNTO SE SOLICITA VALORES
        valor = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
        if valor == 0: ## SE REALIZA LA VALIDACIÓN
            break
        lista.append(valor)
    ### SE CALCULA EL PROMEDIO DE DOS FORMAS DISTINTAS
    prom = statistics.mean(lista)
    mean = sum(lista) / len(lista)
    print(prom)
    print(mean)



# Procedimientos (Acciones y Funciones)

# EJERCICIO 1
def ejercicio1():
    ingresa = True #Bandera que indica si el ciclo debe seguirse cumpliendo
    lista = [] # elemento lista
    while ingresa:
        digito = input("Por favor, digíte un numero o 'X' para cancelar: ")
        # Como nos pide que el usuario explique que ya no desea seguir ingresando.. los hacemos cuando ingrese una X
        if digito == 'x' or digito == 'X':
            ingresa = False
            break
        digito = int(digito)
        lista.append(digito)
    from statistics import mean
    # Para sacar el promedio de una lista se puede usar mean que es una función propia de python
    # o a su vez, puedo contar los valores con SUM y dividirlos para el total de elemento con la funció LEN
    l = [i for i in lista if i >= 18] # armo sublista con valores mayores a 18
    print(lista)
    print(l)
    print(sum(l) / len(l))
    print(round(mean(l), 0)) #calculo de promedio de lista

# EJERCICIO 2
def eleva():
    base = 0
    exponente = 0
    ### UTILIZAMOS TRY EXCEPT para validar la excepción y especificar que se deben ingresar valores numericos

    try:
        base = int(input("Por favor, ingresa la base, debe ser un valor entero: "))
    except Exception as ex:
        print("El valor ingresado no es un número, intenta otra vez")
        base = int(input("Por favor, ingresa la base, debe ser un valor entero: "))
    try:
        exponente = int(input("Por favor, ingresa el exponente, debe ser un valor entero: "))
    except:
        print("El valor ingresado no es un número, intenta otra vez")
        exponente = int(input("Por favor, ingresa el exponente, debe ser un valor entero: "))
    if base and exponente:
        # puedo usar POW que es una función de python que me calcula el exponencial
        # resultado = pow(base, exponente) "POW funcion que obtiene el valor exponencial
        i=0
        resultado=1
        # utilizamos while para indicar que se multiplique la base tantas veces como indique el exponente
        while i < exponente:
            resultado = resultado*base
            i += 1
        print('base %s:' % base)
        print('exponente %s:' % exponente)
        print('resultado %s:' % resultado)


# EJERCICIO 3
def perimetro():
    # lados = float(input("Número de lados del polígono, debe ser un valor numerico: "))
    # longitud = float(input("Longitud de los lados, debe ser un valor numerico: "))
    # perimetro = lados * longitud
    perimetro = 0
    lados = int(input("Número de lados del polígono (no puedo ser mayor que 5), debe ser un valor numerico: "))
    if lados > 5:
        lados = 5
    i = 1
    # utilizo while para solicitar la longitud de los 5 lados
    while i <= lados:
        longitud = float(input("Longitud de los lados, debe ser un valor numerico: "))
        i += 1
        perimetro += longitud # al final se suma los valores ingresados para calcular perimetro

    print('perímetro %s:' % perimetro)



# EJERCICIO 4
# FUNCIÓN QUE ME PERMITE CALCULAR EL VALOR A PAGAR
def calcula_pago(horas, valor, extra=False):
    if extra:
        total = round(horas * valor, 2)
        return total + ((total*35) / 100.0)
    return round(horas * valor, 2)

def horas_extras():
    i = 1
    data = []
    datos = {}
    #### UTILIZAMOS WHILE PARA SOLICITAR LOS DATOS DE LOS 5 EMPLEADOS
    while i <= 5:
        empleado = input("Identificación del empleado: ")
        valor = float(input("Valor por hora, debe ser un valor numerico: "))
        horas = int(input("Horas laboradas, debe ser un valor entero: "))
        datos = {'identificacion': empleado, 'valor': valor, 'horas': horas}
        data.append(datos)  ##AL FINAL EL DICCIONARIO ARMADO LO AGREGAMOS A LA LISTA GENERAL
        i += 1
    for d in data: ### RECORREMOS LA LISTA PARA HACER LAS VALIDACIONES
        ## SI LAS HORAS SON MENORES O IGUAL A 40 SOLO SE HACE LA MULTIPLICACIÓN CORRESPONDIENTE
        if int(d['horas']) <= 40:
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %
                  (d['identificacion'], d['valor'], d['horas'], 0, calcula_pago(d['valor'], d['horas']), 0))
        else:
            ## SI ES MAYOR QUE 40, ES NECESARIO CALCULAR LAS HORAS EXTRAS, HEMOS DEFINIDO UNA FUNCIÓN PARA ELLO
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %
                  (d['identificacion'], d['valor'], d['horas'], d['horas'] - 40, calcula_pago(d['valor'], 40), calcula_pago(d['valor'], int(d['horas']) - 40, True)))


# EJERCICIO 5
def millas_km(millas):
    ## FUNCIÓN QUE PONDERA MILLAS A HORAS
    return round(millas * 1.60935, 3)

def distancia():
    i = 1
    while i <= 4: ### MEDIANTE CICLO WHILE SE SOLICITA EL INGRESO DE DATOS
        ciudadA = input("Ciudad A: ")
        ciudadB = input("Ciudad B: ")
        millas = float(input("Distancia en millas: "))
        ### IMPRIMIMOS LOS DATOS LLAMANDO A LA FUNCIÓN DE CONVERSIÓN
        print(u'Entre %s y %s hay %s KM' % (ciudadA, ciudadB, millas_km(millas)))