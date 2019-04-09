import numpy as np
import os
import json
import matplotlib.pyplot as plt
import cv2 as cv
import random


class Image:

    def __init__(self, label,  img):
        self.img = img
        self.label = label

    def __repr__(self):
        print(self.label, self.img.shape)


class ImageGenerator:

    def __init__(self, batch=9, imgsize=(32, 32), mirr=False, shuffle=False, rotate=False):
        filedir = os.path.dirname(os.path.realpath(__file__))
        datadir = os.path.join(filedir, 'data')
        labelsjson = open(os.path.join(datadir, 'Labels.json')).read()
        self.excData = os.path.join(datadir, 'exercise_data')
        self.labels = json.loads(labelsjson)
        self.mirr = mirr
        self.shuffle = shuffle
        self.rotate = rotate
        self.batch = batch
        self.imgsize = imgsize
        self.images = []
        self.load()

    def load(self):
        for subdir, dirs, files in os.walk(self.excData):
            for file in files:
                a = np.load(os.path.join(subdir, file))
                if self.mirr:
                    a = np.flip(a, 1)
                if self.rotate:
                    a = np.rot90(a)
                name = os.path.splitext(file)[0]
                label = self.labels.get(name)
                self.images.append(Image(label, a))

    def next(self):
        nxt = []
        for b in range(self.batch if len(self.images) >= self.batch else len(self.images)):
            num = b if not self.shuffle else random.randint(b, len(self.images)-1)
            nxt.append(self.images[num])
        self.images = [x for x in self.images if x not in nxt]
        return nxt

    # class_name function with extra functionality to receive the image data in a seperate array
    def class_data(self, images):
        labels = []
        imgs = []
        for img in images:
            labels.append(img.label)
            res = img.img
            if (res.shape[0], res.shape[1]) != self.imgsize:
                res = cv.resize(res, self.imgsize)
            imgs.append(res)
        return labels, imgs

    def show(self):
        for i in range(int(len(self.images)/self.batch)+1):
            nxt = self.next()
            labels, imgs = self.class_data(nxt)
            fig = plt.figure(figsize=(10, 10))
            columns = 3
            rows = int(len(nxt)/3)+1
            for j in range(1, len(nxt)+1):
                ax = fig.add_subplot(rows, columns, j, title=labels[j-1])
                ax.axis('off')
                plt.imshow(imgs[j-1])
            plt.show()


if __name__ == "__main__":
    test = ImageGenerator()
    test.show()
