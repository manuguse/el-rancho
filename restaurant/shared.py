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

ready_to_order = list()
max_clients = 0
crew_attended = 0
totem_attended = 0
chef_attended = 0
lock_totem = Lock()
new_ticket = Condition()
lock_crew = Lock()
new_crew = Condition(lock_crew)
lock_chef = Lock()
new_order = Condition()
lock_table = Lock()
clients = list()
client_waiting_crew = list()
client_waiting_chef = list()
client_waiting_table = list()
totem = None
table = Table(0)
