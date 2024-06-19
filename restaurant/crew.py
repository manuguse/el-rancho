# imports do Python
from threading import Thread


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print(f"O membro da equipe {self._id} está esperando um cliente.")

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        print(f"[CALLING] - O membro da equipe {self._id} está chamando o cliente da senha {ticket}.")

    def make_order(self, order):
        print(f"[STORING] - O membro da equipe {self._id} está anotando o pedido {order} para o chef.")

    """ Thread do membro da equipe."""
    def run(self):
        self.wait()
        self.call_client(0)
        self.make_order(0)