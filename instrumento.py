class Instrumento:
    def __init__(self, nombre, puede_afinar=False):
        self.nombre = nombre
        self.puede_afinar = puede_afinar

    def afinar(self):
        if self.puede_afinar:
            print(f"Afinando {self.nombre}")
        else:
            print(f"{self.nombre} no se puede afinar")
    def tocar(self):
        pass
    def consultar(self):
        print("Soy: ", self.nombre)

class Piano(Instrumento):
    def __init__(self):
        super().__init__("Piano")
    def tocar(self):
        print("Tocando piano: ¡tink tink tank!")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando guitarra: ¡truum struum!")
        
class Saxofon(Instrumento):
    def __init__(self):
        super().__init__("Saxofon")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando saxofon: ¡fuum!")   
         
class Bajo(Instrumento):
    def __init__(self):
        super().__init__("Bajo")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando bajo: ¡sruum!")
        
class Violin(Instrumento):
    def __init__(self):
        super().__init__("Violin")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando Violin: ¡sriiim!")
        
class Trompeta(Instrumento):
    def __init__(self):
        super().__init__("Trompeta")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando Trompeta: ¡pruuuum!")
             
if __name__ == "__main__":
    a = Piano()
    a.consultar()