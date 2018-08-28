#
#   Disciplina de Métodos Numéricos (2018.2 UFC)
#
#   Autor: Allan César
#   Data: 24/08/2018
#
#   Algoritmo do Método Numérico: Bisseção 
#
#   Base environment: Anaconda 3 (Python 3.6)
#
from Method import *

class Bissection(Method):
    def __init__(self, function, a, b, E, maxIter = 50):
        Method.__init__(self, function, a, b, E, maxIter)

    def mean(self):                                     #   Regra de negócio da Bisseção
        return ((self.a + self.b)/2)

    def bissection(self):
        if not self.signal_is_valid(self.a, self.b):                  #   Testa se o sinal do intervalo muda em relação aos extremos do intervalo
             return Exception                            #   Se não, lança um exception
        if not self.E_is_valid():                       #   Testa se o valor da raiz já está proximo aos extremos do intervalo
            return Exception                            #   Se não, lança um exception        

        self.x = self.mean()                            #   Calcula o primeiro x provisório

        self.print_header()                             #   Printa o cabeçalho do debug no console

        k = 1                                           #   Declara o iterador começando em 1
        while k < self.maxIter:                         #   Enquanto o iterador for menor que o número máximo de iterações repita:
            
            if not self.signal_is_valid(self.a, self.x):#   Se a função não mudar de sinal entre a e x,  
                self.a = self.x                         #   então atualiza o a = x
            else:                       
                self.b = self.x                         #   Se não, atualiza o b = x

            self.x = self.mean()                        #   Calcula o valor da raiz provisória da próxima iteração 
            
            self.print_debug(k)                         #   Printa uma linha de debug com todas as variáveis 
            
            if not self.E_is_valid():                   #   Testa se a aproximação ainda pode ser refinada
                break                                   #   Saí do loop

            k += 1                                      #   Incrementa nosso iterador
        return self.x                                   #   Retorna o valor da raiz calculada