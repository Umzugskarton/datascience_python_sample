import numpy as np
import matplotlib.pyplot as plt


class Checker:

    def __init__(self, resolution=100, tile_size=10):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = np.zeros((resolution, resolution))

    def draw(self):
        num = int(self.resolution/self.tile_size)
        bl = np.tile([100], self.tile_size)
        wh = np.tile([0], self.tile_size)
        p1 = np.tile(np.concatenate((bl, wh), axis=None), int(num/2))
        p2 = np.tile(np.concatenate((wh, bl), axis=None), int(num/2))
        if num % 2 != 0:
            p1 = np.concatenate((p1, bl), axis=None)
            p2 = np.concatenate((p2, wh), axis=None)
        p1_fulltile = np.tile(p1, (self.tile_size, 1))
        p2_fulltile = np.tile(p2, (self.tile_size, 1))
        ch = np.concatenate((p1_fulltile, p2_fulltile), axis=0)
        self.output = np.tile(ch, (int(num/2), 1))
        if num % 2 != 0:
            self.output = np.concatenate((self.output, p1_fulltile), axis=0)

    def show(self):
        plt.imshow(self.output, vmin=0, vmax=self.resolution, cmap=plt.cm.binary)
        plt.show()


if __name__ == "__main__":
    test = Checker()
    test.draw()
    test.show()

