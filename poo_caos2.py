import random
#tipo 1 de pessoa =  vai pegar o halter e devolver no lugar certo ( se tiver bagunçado ele não vai organizar)
#tipo 2 de pessoa =  vai pegar o halter e devolver em qualquer lugar ( bagunçando a academia)

class Academia():
    def __init__(self):
        self.halteres = [i for i in range(10,36,2)]
        self.porta_halteres = {}
        self.resetar_academia()


    def resetar_academia(self):
        self.porta_halteres = {i : i for i in self.halteres}
    
    #função que retorne todos os halteres disponíveis, que podem ser pegos
    def halteres_disponiveis(self):
        return [i for i in self.porta_halteres.values()]

    #função de pegar os halter e zerar a keyword do halter, retornando o peso pego
    def pegar_halter(self,peso):
        halteres_position = list(self.porta_halteres.values()).index(10)
        self.porta_halteres[10] = 0
    #função para devolver o halter 

    #função para mostrar o a porcentagem de halteres fora do lugar
