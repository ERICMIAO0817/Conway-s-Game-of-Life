class Cell:
    def __init__(self):
        self.status = 0
        self.neighbour = 0

    def set_status(self):
        self.status = 1

    def shutdown_status(self):
        self.status = 0

    def get_status(self):
        return self.status

    def pruge_neighbour(self):
        self.neighbour = 0