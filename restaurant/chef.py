# imports do Python
from threading import Thread, Lock
from time import sleep
from random import randint

# Imports necessarios para executar as threads
from . import shared as shared

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        with shared.lock_chef:
            self._now_cooking = shared.client_waiting_chef.pop(0)
        print(f"[COOKING] - O chefe esta preparando o pedido para a senha {self._now_cooking._ticket}.")
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print(f"[READY] - O chefe está servindo o pedido para a senha {self._now_cooking._ticket}.")
        self._now_cooking._semaphore.release()
        shared.chef_attended += 1
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        with shared.new_order:
            if len(shared.client_waiting_chef) == 0:
                print("O chefe está esperando algum pedido.")
                shared.new_order.wait()

    """ Thread do chefe."""
    def run(self):
        while shared.chef_attended < shared.max_clients:
            self.wait_order()
            self.cook()
            self.serve()