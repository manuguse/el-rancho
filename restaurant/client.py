# imports do Python
from threading import Thread, Semaphore
from time import sleep
from random import randint


# imports do projeto
from . import shared as shared

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i):
        self._id = i
        super().__init__()
        self._semaphore = Semaphore() #semáforo pessoal do cliente para controlar o fluxo de execução
        self._semaphore._value = 0 #inicializa o semáforo com 0 para bloquear o cliente na próxima chamada
        shared.clients.append(self) #adiciona o cliente à lista de clientes
        self._waiter = None #membro da equipe que atendeu o cliente
        self._ticket = None #número do ticket do cliente
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        '''fazemos uma chamada de acquire para garantir que o semáforo esteja com o valor 0
        para garantir que ele não possa prosseguir quando chamar acquire novamente'''
        with shared.lock_totem: #o lock garante que não será emitido um valor de ticket repetido
            self._ticket = shared.totem.get_ticket() #atualiza o valor pessoal do ticket do cliente com o retorno da função
        print(f"[TICKET] - O cliente {self._id} pegou o ticket.")

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print(f"[WAIT] - O cliente {self._id} esta aguardando atendimento.")
        self._semaphore.acquire() #o cliente aguarda o semáforo ser liberado pela equipe para prosseguir

    
    """ O cliente pensa no pedido."""
    def think_order(self):
        print(f"[THINK] - O cliente {self._id} esta pensando no que pedir.")
        sleep(randint(1,3)) #tempo aleatório para o cliente pensar no pedido

    """ O cliente faz o pedido."""
    def order(self):
        print(f"[ORDER] - O cliente {self._id} pediu algo.")
        self._waiter._semaphore.release() #libera o semáforo do garçom que estava aguardando o pedido
        

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print(f"[WAIT MEAL] - O cliente {self._id} esta aguardando o prato.")
        self._semaphore.acquire() #o cliente aguarda o semáforo ser liberado pelo chef
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        with shared.lock_table: #o lock garante que duas pessoas não tentem simultaneamente sentar na mesa
            if shared.table._semaphore._value == 0: #se não houver lugar na mesa
                print(f"[WAIT SEAT] - O cliente {self._id} esta aguardando um lugar ficar livre")
            shared.table.seat(self) #chama a função seat da mesa para o cliente sentar
        print(f"[SEAT] - O cliente {self._id} encontrou um lugar livre e sentou")
        sleep(randint(1,3)) #cliente come por um tempo aleatório

    """ O cliente deixa o restaurante."""
    def leave(self):
        shared.table.leave(self) #chama a função leave da mesa para liberar o lugar
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