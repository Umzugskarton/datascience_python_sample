import numpy as np
import matplotlib.pyplot as plt


class Spectrum:

    def __init__(self, resolution=1000):
        self.resolution = resolution
        self.output = np.ndarray

    def draw(self):
        r = np.linspace(0, 1, self.resolution)
        g = np.array(r)[np.newaxis]
        g = g.T
        b = np.linspace(1, 0, self.resolution)
        rgb = np.zeros((self.resolution, self.resolution, 3))
        rgb[:, :, 0] = r[:]
        rgb[:, :, 2] = b[:]
        rgb[:, :, 1] += g
        self.output = rgb

    def show(self):
        plt.imshow(self.output, vmin=0, vmax=self.resolution)
        plt.show()


if __name__ == "__main__":
    s = Spectrum()
    s.draw()
    s.show()
