class User:
    def __init__ (self, user_id, server_id, spatial_index):
        self.user_id = user_id
        self.server_id = server_id
        self.spatial_index = spatial_index

    def set_spatial_index(self):
        self.spatial_index.insert(self.user_id, (0.5, 0.5, 0.5, 0.5))

    def get_spatial_index(self):
        return self.spatial_index.bounds

    def get_user_id(self):
        return self.user_id

    def get_user_server_id(self):
        return self.server_id







