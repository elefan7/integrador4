import os
from typing import List, Tuple
from readchar import readkey, key

print("Hola ingresa tu nombre por favor: ")
nombre = input()
print(f"Bienvenido al juego {nombre}")


def convertir(maze_generator: str):
    filas = maze_generator.split('\n')

    laberinto = []

    for fila in filas:
        laberinto.append(list(fila))

    return laberinto

def mostrar_laberinto(mapa):
    for fila in mapa:
          print(" ".join(fila))


def limpiar_mostrar(laberinto):
     os.system('cls' if os.name == 'nt' else 'clear')
     for fila in laberinto:
          print(''.join(fila))


def main_loop(mapa, inicio, end):
     px, py = inicio
     while (px, py) != end:

          if 0 <= px < len(mapa[0]) and 0 <= py < len(mapa):
            mapa[py][px] = 'P'
          limpiar_mostrar(mapa)
          print(px, py)
          teclado = readkey()
          px_nueva, py_nueva = px, py

          if teclado == key.UP and py > 0 and mapa[py - 1][px] != '#':
               py_nueva -= 1
          elif teclado == key.DOWN and py < len(mapa) - 1 and mapa[py + 1][px] != '#':
               py_nueva += 1
          elif teclado == key.LEFT and px > 0 and mapa[py][px - 1] != '#':
               px_nueva -= 1
          elif teclado == key.RIGHT and px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
               px_nueva += 1
          
          if 0 <= px_nueva < len(mapa[0]) and 0 <= py_nueva < len(mapa):
              
             mapa[py][px] = ' '
             px, py = px_nueva, py_nueva

          mapa[py][px] = 'P'
          limpiar_mostrar(mapa)
     print(f"Felicidades {nombre} lo has logrado")


if __name__ == "__main__":
     

 map_generator = """..###################
........#.#.#.#...#.#
#.#.###.#.#.#.#.#.#.#
#.#.#.....#.....#.#.#
#.###.#####.###.###.#
#.#.#.......#.......#
#.#.#####.#######.#.#
#.....#...#...#...#.#
#.###.###.###.###.###
#.#...#.......#.....#
#####.#####.#########
#.#.#.....#...#.#...#
#.#.#.#####.#.#.###.#
#.......#...#...#...#
###.###.###########.#
#...#.#.#.....#...#.#
#.###.#####.#####.#.#
#...................#
###.#.#####.#####.#.#
#...#...#...#.....#.#
###################.#"""

end = (19, 20)
labto_completo = convertir(map_generator)
inicio = (0, 0)
mostrar_laberinto(labto_completo)
main_loop(labto_completo, inicio, end)
