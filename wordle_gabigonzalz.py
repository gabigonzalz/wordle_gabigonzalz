# -------------------> Wordle de Gabi Gonzalez<------------------- #
#> Variables necesarias
palabra_del_dia = "VACAS" #Debe estar en mayusculas
contador_intentos = 0
palabra_procesada = [" "," "," "," "," ",] #Aca van las letras con su identificador

#> Titulo
print("""░█░░░█░▄▀▀▄░█▀▀▄░█▀▄░█░░█▀▀
░▀▄█▄▀░█░░█░█▄▄▀░█░█░█░░█▀▀
░░▀░▀░░░▀▀░░▀░▀▀░▀▀░░▀▀░▀▀▀""")

#---------------------------------------------------------------------
#Armamos nuestro funcion procesadora de letras
def procesador_de_letras (intento_del_usuario,palabra_del_dia,palabra_procesada):
    for letra in range(5): #Revisamos las 5 letras del intento
        #Si alguna letra del intento se encuentra en la palabra del dia
        if intento_del_usuario[letra] in palabra_del_dia:
            #Si la letra que esta en su lugar correcto y es correcta entonces:[ ]
            if intento_del_usuario[letra] == palabra_del_dia[letra]:
                palabra_procesada[letra] = "["+intento_del_usuario[letra]+"]"
            #Si la letra esta dentro de la palabra correcta pero en el lugar incorrecto: ( )
            else: 
                    palabra_procesada[letra] = "("+intento_del_usuario[letra]+")" 
        #Si la letra no se encuentra dentro de la lista: " " (vacio)
        else:
            palabra_procesada[letra] = " "+intento_del_usuario[letra]+" "
    return(palabra_procesada)
#---------------------------------------------------------------------

#> Unimos nuestras funciones de WORDLE

while contador_intentos != 6:  
    intento_del_usuario = input("ADIVINE LA PALABRA DEL DIA: ").upper()#El usuario ingresa su intento

    
    #Verificamos si el intento de el usuario tiene 5 letras o no, solo participan palabras de 5 letras
    if len(intento_del_usuario) != 5:
         #Si tiene menos o mas de 5 letras vuelve a intentar (no se elimina un intento)
         print("LA PALABRA NO CONTIENE 5 LETRAS. INTENTELO DE NUEVO")
         continue
    else: #Si el intento tiene 5 letras continuamos y contamos como un intento
        contador_intentos = contador_intentos + 1
        procesador_de_letras(intento_del_usuario,palabra_del_dia,palabra_procesada)
        print(str(contador_intentos)+"- "+" ".join(palabra_procesada)) #Imprimimos el intento del usuario procesado
        #Si el usuario adivina la palabra
        if intento_del_usuario == palabra_del_dia:
            print("¡FELICIDADES HAS ADIVINADO LA PALABRA DEL DIA!")
            break
        else:
            continue 

#---------------------------------------------------------------------

#> Por ultimo: al terminar la cantidad de intentos:

#Si el usuario se queda sin intentos sin haber adivinado
if contador_intentos == 6 and intento_del_usuario != palabra_del_dia:
    print("LO SIENTO. TE HAS QUEDADO SIN INTENTOS.")
else: #Si es que se quedo sin intentos y se ha adivinado la palabra no hace falta hacer nada
    pass
#---------------------------------------------------------------------