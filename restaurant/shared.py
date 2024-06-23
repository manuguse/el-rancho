from threading import Lock, Condition, Semaphore
from restaurant.totem import Totem
from restaurant.table import Table
# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

max_clients = 0
crew_attended = 0
chef_attended = 0
lock_totem = Lock()
lock_table = Lock()
new_ticket = Condition()
lock_crew = Lock()
lock_chef = Lock()
new_order = Condition()
clients = list()
client_waiting_chef = list()
totem = None
table = Table(0)
