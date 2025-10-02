class Circle:
    def __init__(self, raio=1):
        self.raio = raio
        print("Círculo criado com raio:", self.raio)

    def area(self):
        return self.raio**2 * 3.14

    def retorna_raio(self):
        return self.raio

c1 = Circle()
print(c1.retorna_raio())

