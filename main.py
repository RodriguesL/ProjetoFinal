from rtree import index
import User
import Server
import random

PLAYER_COUNT = 1000
SERVER_COUNT = 4

spatial_index = index.Index()
server_id = random.randint(0, SERVER_COUNT)
#spatial_index.insert(server_id, (0.0, 0.0, 1.0, 1.0))
user = User(random.randint(1000, PLAYER_COUNT+1000), server_id, spatial_index)
server = Server(server_id, spatial_index)





