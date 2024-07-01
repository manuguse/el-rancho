# imports do Python
from threading import Thread, Semaphore
from . import shared as shared

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._semaphore = Semaphore(0) # semáforo pessoal do membro da equipe para controlar o fluxo de execução

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        clientes_na_fila = shared.new_ticket.acquire(blocking=False) # verifica se clientes na fila para serem atendidos
        if not clientes_na_fila: # se não tiver, printa que está esperando um cliente
            print(f"O membro da equipe {self._id} está esperando um cliente.")
            shared.new_ticket.acquire() # aguarda a notificação de um novo ticket
        
    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        print(f"[CALLING] - O membro da equipe {self._id} está chamando o cliente da senha {ticket}.")
        for client in shared.clients: # percorre a lista de clientes
            if client._ticket == ticket: # se o ticket do cliente for igual ao ticket chamado
                self.now_serving = client # o membro da equipe passa a atender o cliente
                client._waiter = self # o cliente passa a ser atendido pelo membro da equipe
                client._semaphore.release() # libera o semáforo do cliente para prosseguir
                break
        self._semaphore.acquire() # aguarda a liberação do cliente após pensar no que pedir

    def make_order(self, order):
        print(f"[STORING] - O membro da equipe {self._id} está anotando o pedido {order} para o chef.")
        with shared.lock_chef: # o lock bloqueia o acesso de outras threads à lista de clientes aguardando o chef
            shared.clients_waiting_chef.append(self.now_serving) # adiciona o cliente à lista de clientes aguardando o chef
        shared.new_order.release() # notifica o chef que há um novo pedido


    """ Thread do membro da equipe."""
    def run(self):
        while True:
            with shared.lock_crew: 
                order = shared.crew_served
                if order == shared.max_clients:
                        return
                shared.crew_served += 1 
            self.wait()
            with shared.lock_totem: # garante que não haverá acesso concorrente à lista de tickets
                next_client = min(shared.totem.call) # chama a menor senha da lista de tickets
                shared.totem.call.remove(next_client) # remove a senha chamada da lista de tickets
            self.call_client(next_client)
            self.make_order(order)
