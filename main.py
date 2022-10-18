import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from cell import Cell

np.random.seed(0)


class Layout:
    def __init__(self, size=200, dropout=0.1):
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

    def drop_pic(self, epoch):
        cmapmine = ListedColormap(['w', 'g'], N=2)
        fig, (ax) = plt.subplots(1, 1)
        ax.imshow(self.state_mat, cmap=cmapmine, vmin=0, vmax=1)
        ax.set_title('Life')
        # plt.show()
        plt.savefig(f'out/{epoch}.jpg', bbox_inches='tight')

    def iteration(self, epoch):
        for _ in range(epoch):
            self.update()
            self.drop_pic(_)

    def update(self):
        for index, item in enumerate(self.state_mat):
            # _alive = np.where(item == 1)[0]
            for idx, col in enumerate(item.tolist()):
                self.process(index, idx, self.mat[index][idx])
                # self.create_state_mat()
                
        for index, item in enumerate(self.state_mat):
            # _alive = np.where(item == 1)[0]
            for idx, col in enumerate(item.tolist()):
                if self.mat[index][idx].get_status() == 1:
                    if self.mat[index][idx].neighbour < 2:
                        # print(index, col)
                        self.mat[index][idx].shutdown_status()

                    elif self.mat[index][idx].neighbour > 3:
                        # print(index, col)
                        self.mat[index][idx].shutdown_status()
                else:
                    if self.mat[index][idx].neighbour == 3:
                        self.mat[index][idx].set_status()
        self.create_state_mat()

    def process(self, index, col, cell):
        cell.pruge_neighbour()
        # print(index, col)
        possible_direct = [(index - 1, col - 1), (index - 1, col), (index - 1, col + 1),
                           (index, col - 1), (index, col + 1),
                           (index + 1, col - 1), (index + 1, col), (index + 1, col + 1)]
        # k = 0
        for direct in possible_direct:
            direct_row, direct_col = direct
            if direct_row not in range(0, self.size):
                continue
            if direct_col not in range(0, self.size):
                continue
            if self.mat[direct_row][direct_col].status == 1:
                cell.neighbour += 1
                # k += 1
        # print(k)

        # if cell.get_status() == 1:
        #     if cell.neighbour < 2:
        #         # print(index, col)
        #         cell.shutdown_status()
        # 
        #     elif cell.neighbour > 3:
        #         # print(index, col)
        #         cell.shutdown_status()
        # else:
        #     if cell.neighbour == 3:
        #         print(index, col)
        #         cell.set_status()


if __name__ == '__main__':
    l = Layout()
    l.create_object_mat()
    l.iteration(200)
