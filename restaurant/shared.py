from threading import Lock, Condition, Semaphore
from restaurant.table import Table

max_clients = 0              # número máximo de clientes
crew_served = 0            # controle de quantos clientes já foram atendidos pela equipe
lock_totem = Lock()          # lock para garantir que apenas um cliente pegue um ticket por vez
lock_table = Lock()          # lock para garantir que apenas um cliente tente sentar na mesa por vez
new_ticket = Semaphore(0)     # condição para avisar que um novo ticket foi emitido
lock_crew = Lock()           # lock para controlar o próximo cliente a ser atendido
lock_chef = Lock()           # lock para controlar o próximo pedido a ser preparado
new_order = Semaphore(0)      # condição para avisar o chef que há um novo pedido
clients = list()             # lista total de clientes
clients_waiting_chef = list() # lista de clientes aguardando o chef
totem = None

table = Table(0)
