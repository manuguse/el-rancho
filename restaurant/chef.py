# imports do Python
from threading import Thread
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
        self._served = 0 # contador de pedidos prontos
        self._now_cooking = None # pedido sendo preparado

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        with shared.lock_chef: # o lock bloqueia o acesso de outras threads à lista de clientes aguardando o chef
            self._now_cooking = shared.clients_waiting_chef.pop(0) # o chef recebe o cliente do pedido sendo preparado e o remove da lista
        print(f"[COOKING] - O chefe esta preparando o pedido para a senha {self._now_cooking._ticket}.")
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print(f"[READY] - O chefe está servindo o pedido para a senha {self._now_cooking._ticket}.")
        self._now_cooking._semaphore.release() # libera o semáforo do cliente cujo pedido ficou pronto
        self._served += 1 # incrementa o contador de pedidos prontos
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        pedidos_na_fila = shared.new_order.acquire(blocking=False)
        if not pedidos_na_fila:
            print("O chefe está esperando um pedido.")
            shared.new_order.acquire()

    """ Thread do chefe."""
    def run(self):
        while self._served < shared.max_clients:
            self.wait_order()
            self.cook()
            self.serve()
