from banda import *
from instrumento import *

if __name__ == "__main__":

    b = Banda("Los Rítmicos", [Piano(), Guitarra(), Saxofon(), Bajo(), Violin(), Trompeta()])
    
    b.crear()

    b.consultar()
    
    opcion = input("¿Deseas afinar los instrumentos de la banda? (S/N): ").strip().lower()
    b.consultar()
    print ("\nTocando sonidos de la banda:\n")
    if opcion == 's':
        b.afinar_instrumentos() 
    for Musico in b.integrantes:
        Musico.tocar() 