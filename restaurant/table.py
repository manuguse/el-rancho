from threading import Semaphore
"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number
        self._semaphore = Semaphore(number) # semáforo para controlar o número de clientes sentados
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
        self._semaphore.acquire() # ocupa um lugar na mesa, se não for possível aguarda um lugar vago
    
    """ O cliente deixa a mesa."""
    def leave(self, client):
        self._semaphore.release() # aumenta um lugar na mesa

