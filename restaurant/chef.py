# imports do Python
from threading import Thread, Lock
from time import sleep
from random import randint

# Imports necessarios para executar as threads
import restaurant.shared as shared

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print(f"[COOKING] - O chefe esta preparando o pedido para a senha {0}.") # Modifique para o numero do ticket
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print(f"[READY] - O chefe está servindo o pedido para a senha {0}.") # Modificar para o numero do ticket
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        print("O chefe está esperando algum pedido.")

    """ Thread do chefe."""
    def run(self):
        self.wait_order()
        self.cook()
        self.serve()