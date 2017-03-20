class Server:
    def __init__(self, server_id, spatial_index):
        self.server_id = server_id
        self.spatial_index = spatial_index
        self.forwards_count = 0

    def get_server_id(self):
        return self.server_id

    def get_player_count(self):
        return self.spatial_index.count(self.spatial_index.bounds)

    def get_forwards_count(self):
        return self.forwards_count


