import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from cell import Cell

np.random.seed(0)


class Layout:
    def __init__(self, size=100, dropout=0.05):
        self.size = size
        self.dropout = dropout
        self.mat = None
        self.state_mat = None

    def create_object_mat(self):
        vcell = [Cell() for i in range(self.size ** 2)]
        self.mat = np.array(vcell).reshape((self.size, self.size))

        vector = []
        p = np.array([self.dropout, 1 - self.dropout])
        for i in range(self.size ** 2):
            index = np.random.choice([True, False], p=p.ravel())
            vector.append(index)
        _matrix = np.array(vector)

        bool_mat = np.reshape(_matrix, (self.size, self.size))
        for item in self.mat[bool_mat]:
            item.set_status()
        # print(self.mat[bool_mat])
        self.create_state_mat()

    def create_state_mat(self):
        flat_mat = self.mat.flatten()
        _ = list(map(lambda x: x.get_status(), flat_mat))
        self.state_mat = np.array(_)
        self.state_mat = np.reshape(self.state_mat, (self.size, self.size))

    def drop_pic(self):
        cmapmine = ListedColormap(['w', 'g'], N=2)
        fig, (ax) = plt.subplots(1, 1)
        ax.imshow(self.state_mat, cmap=cmapmine, vmin=0, vmax=1)
        ax.set_title('Life')
        plt.show()

    def iteration(self, epoch):
        for _ in range(epoch):
            self.update()
            print(self.state_mat)
            # self.drop_pic()

    def update(self):
        for index, item in enumerate(self.state_mat):
            # _alive = np.where(item == 1)[0]
            for col in item.tolist():
                self.process(index, col, self.mat[index][col])
                self.create_state_mat()

    def process(self, index, col, cell):
        possible_direct = [(index - 1, col - 1), (index - 1, col), (index - 1, col + 1),
                           (index, col - 1), (index, col + 1),
                           (index + 1, col - 1), (index + 1, col), (index + 1, col + 1)]
        if cell.get_status() == 1:
            for direct in possible_direct:
                direct_row, direct_col = direct
                if direct_row not in range(0, self.size - 1):
                    continue
                if direct_col not in range(0, self.size - 1):
                    continue
                cell.neighbour += 1

            if cell.neighbour < 2:
                cell.shutdown_status()

            elif cell.neighbour > 3:
                cell.shutdown_status()
        else:
            for direct in possible_direct:
                direct_row, direct_col = direct
                if direct_row not in range(0, self.size - 1):
                    continue
                if direct_col not in range(0, self.size - 1):
                    continue
                cell.neighbour += 1
            if cell.neighbour >= 3:
                cell.set_status()


if __name__ == '__main__':
    l = Layout()
    l.create_object_mat()
    l.drop_pic()
    l.iteration(10)
