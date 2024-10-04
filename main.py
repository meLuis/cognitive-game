import random
import time
import os

def crear_lista(elementos):
    lista=2*list(range(1,elementos//2+1))
    random.shuffle(lista)
    return lista

def crear_matriz(m_cuadrada, elementos):
    lista=crear_lista(elementos)
    matriz=[[] for i in range(m_cuadrada)]
    for i in range(elementos):
        matriz[i//m_cuadrada].append(lista[i])
    return matriz

def crear_matriz_volteada(simbolo, m_cuadrada, elementos):
    matriz_volteada=[[] for i in range(m_cuadrada)]
    for i in range(elementos):
        matriz_volteada[i//m_cuadrada].append(simbolo)
    return matriz_volteada

def dibujar_matriz(matriz,m_cuadrada):
    for i in range(m_cuadrada):
        for j in range(m_cuadrada):
            print(f"{matriz[i][j]:>4}",end=' ')
        print()

def calcular_puntaje_normal(jugador,puntaje,pares):
    puntaje+=100
    pares+=1
    print(f"El jugador {jugador} ha encontrado una pareja\n")
    return [puntaje,pares]

def calcular_puntaje_bonus(jugador,puntaje,cant_bonus,pares):
    cant_bonus+=1
    puntaje+=1000
    pares+=1
    print(f"El jugador {jugador} ha encontrado una pareja bonus\n")
    return [puntaje,pares,cant_bonus]

def validar_final_normal(pares_encontrados,elementos,cant_bonus_1,cant_bonus_2,pares_1,pares_2):
    if pares_encontrados==elementos//2:
        print("El juego ha terminado")
        if cant_bonus_1>cant_bonus_2:
            print("El ganador es el jugador 1")
            print("Bonus points multiplicados por el total de pares destapados: ",cant_bonus_1*pares_1)
        elif cant_bonus_1<cant_bonus_2:
            print("El ganador es el jugador 2")
            print("Bonus points multiplicados por el total de pares destapados: ",cant_bonus_2*pares_2)
        else:
            print("El juego ha terminado en empate")

        return 'no'
    return 'si'

def validar_final_forzado(pares_1,pares_2,puntos_1,puntos_2,cant_bonus_1,cant_bonus_2):
    print("El juego se ha detenido")
    print("Pares jugador 1: ",pares_1)
    print("Pares jugador 2: ",pares_2)
    print("Bonus jugador 1: ",puntos_1)
    print("Bonus jugador 2: ",puntos_2)
    if cant_bonus_1:
        print("Bonus points jugador 1: ",cant_bonus_1*1000)
    if cant_bonus_2:
        print("Bonus points jugador 2: ",cant_bonus_2*1000)
    

def main():
    #m_cuadrada debe ser par o crear_matriz no tendra sentido
    m_cuadrada=6
    elementos=pow(m_cuadrada,2)
    simbolo="*"
    jugar='si'
    pares_encontrados=0
    jugador=0
    cant_bonus_1=0
    cant_bonus_2=0
    puntos_1=0
    puntos_2=0
    pares_1=0
    pares_2=0
    matriz=crear_matriz(m_cuadrada,elementos)
    matriz_volteada=crear_matriz_volteada(simbolo, m_cuadrada,elementos)
    dibujar_matriz(matriz_volteada,m_cuadrada)

    while jugar=='si':

        jugador=jugador%2+1

        print(f"\nTurno del jugador {jugador}\n")

        print("Ingrese la fila y columna de la primera carta")
        fila_indicada_1=int(input("Ingrese la fila: "))-1
        columna_indicada_1=int(input("Ingrese la columna: "))-1

        matriz_volteada[fila_indicada_1][columna_indicada_1]=matriz[fila_indicada_1][columna_indicada_1]
        dibujar_matriz(matriz_volteada,m_cuadrada)
        valor_1=matriz[fila_indicada_1][columna_indicada_1]


        print("Ingrese la fila y columna de la segunda carta")
        fila_indicada_2=int(input("Ingrese la fila: "))-1
        columna_indicada_2=int(input("Ingrese la columna: "))-1

        matriz_volteada[fila_indicada_2][columna_indicada_2]=matriz[fila_indicada_2][columna_indicada_2]
        dibujar_matriz(matriz_volteada,m_cuadrada)
        valor_2=matriz[fila_indicada_2][columna_indicada_2]

        if valor_1==valor_2:
            pares_encontrados+=1
            if valor_1%5==0:
                print(f"El jugador {jugador} ha encontrado una par bonus\n")

                if jugador==1:
                    lista_bonus=calcular_puntaje_bonus(jugador,puntos_1,cant_bonus_1,pares_1)
                    puntos_1=lista_bonus[0]
                    pares_1=lista_bonus[1]
                    cant_bonus_1=lista_bonus[2]
                else:
                    lista_bonus=calcular_puntaje_bonus(jugador,puntos_2,cant_bonus_2,pares_2)
                    puntos_2=lista_bonus[0]
                    pares_2=lista_bonus[1]
                    cant_bonus_2=lista_bonus[2]
            else:
                print(f"El jugador {jugador} ha encontrado una par\n")
                if jugador==1:
                    lista_normal=calcular_puntaje_normal(jugador,puntos_1,pares_1)
                    puntos_1=lista_normal[0]
                    pares_1=lista_normal[1]
                else:
                    lista_normal=calcular_puntaje_normal(jugador,puntos_2,pares_2)
                    puntos_2=lista_normal[0]
                    pares_2=lista_normal[1]
        else:
            print(f"El jugador {jugador} no ha encontrado una par\n")
            matriz_volteada[fila_indicada_1][columna_indicada_1]=simbolo
            matriz_volteada[fila_indicada_2][columna_indicada_2]=simbolo


        jugar=validar_final_normal(pares_encontrados,elementos,cant_bonus_1,cant_bonus_2,pares_1,pares_2)

        if jugador==2 and jugar!="no":
            jugar=input("Desea seguir jugando? si/no: ")
            if jugar=="no":
                validar_final_forzado(pares_1,pares_2,puntos_1,puntos_2,cant_bonus_1,cant_bonus_2)

    

if __name__=='__main__':
    main()

