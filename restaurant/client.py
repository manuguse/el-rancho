# imports do Python
from threading import Thread
from time import sleep

# imports do projeto

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i):
        self._id = i
        super().__init__()
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        print(f"[TICKET] - O cliente {self._id} pegou o ticket.")

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print(f"[WAIT] - O cliente {self._id} esta aguardando atendimento.")

    
    """ O cliente pensa no pedido."""
    def think_order(self):
        print(f"[THINK] - O cliente {self._id} esta pensando no que pedir.")

    """ O cliente faz o pedido."""
    def order(self):
        print(f"[ORDER] - O cliente {self._id} pediu algo.")

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print(f"[WAIT MEAL] - O cliente {self._id} esta aguardando o prato.")
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print(f"[WAIT SEAT] - O cliente {self._id} esta aguardando um lugar ficar livre")
        print(f"[SEAT] - O cliente {self._id} encontrou um lugar livre e sentou")

    """ O cliente deixa o restaurante."""
    def leave(self):
        print(f"[LEAVE] - O cliente {self._id} saiu do restaurante")
    
    """ Thread do cliente """
    def run(self):
        self.get_my_ticket()
        self.wait_crew()
        self.think_order()
        self.order()
        self.wait_chef()
        self.seat_and_eat()
        self.leave()