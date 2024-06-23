# imports do Python
from threading import Thread, Semaphore
from time import sleep
from . import shared as shared


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._semaphore = Semaphore()
        self._semaphore.acquire()
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print(f"O membro da equipe {self._id} está esperando um cliente.")    
        with shared.new_ticket:
            shared.new_ticket.wait()

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        print(f"[CALLING] - O membro da equipe {self._id} está chamando o cliente da senha {ticket}.")
        for client in shared.clients:
            if client._ticket == ticket:
                self.now_attending = client
                client._waiter = self
                client._semaphore.release()
                break
        self._semaphore.acquire()

    def make_order(self, order):
        print(f"[STORING] - O membro da equipe {self._id} está anotando o pedido {order} para o chef.")
        with shared.lock_chef:
            shared.client_waiting_chef.append(self.now_attending)
        with shared.new_order:
            shared.new_order.notify()


    """ Thread do membro da equipe."""
    def run(self):
        
        while shared.crew_attended < shared.max_clients:
            with shared.lock_crew:
                order = shared.crew_attended
                shared.crew_attended += 1
            self.wait()
            with shared.lock_totem:
                next_client = min(shared.totem.call)
                shared.totem.call.remove(next_client)
            self.call_client(next_client)
            self.make_order(order)