import numpy as np
import math
import matplotlib.pyplot as plt


class Circle:

    def __init__(self, resolution=1000, radius=150, position=(200, 500)):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = np.ones((resolution, resolution))

    def draw(self):
        for i in range(self.radius - 1):
            x = round(math.sqrt((math.pow(self.radius-1, 2) - (math.pow(i, 2)))))
            for j in range(x+1):
                self.output[i+self.position[0]][j+self.position[1]] = self.resolution
                self.output[j+self.position[0]][i+self.position[1]] = self.resolution
                self.output[self.position[0]-i][j+self.position[1]] = self.resolution
                self.output[self.position[0]-j][i+self.position[1]] = self.resolution
                self.output[i+self.position[0]][self.position[1]-j] = self.resolution
                self.output[j+self.position[0]][self.position[1]-i] = self.resolution
                self.output[self.position[0]-i][self.position[1]-j] = self.resolution
                self.output[self.position[0]-j][self.position[1]-i] = self.resolution

    def show(self):
        plt.imshow(self.output, vmin=0, vmax=self.resolution,  cmap=plt.cm.gray)
        plt.show()


if __name__ == "__main__":
    test = Circle(1000 , 150, (200,500))
    test.draw()
    test.show()



