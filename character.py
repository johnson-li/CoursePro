__author__ = 'johnson'

import cv2
import Image
import datetime


class Character:

    def __init__(self, src):
        self.src = src
        self.image = cv2.imread(src)
        self.grayImage = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.ret, self.mask = cv2.threshold(self.grayImage, 170, 255, cv2.THRESH_BINARY_INV)
        self.image1 = Image.Image
        self.image2 = Image.Image
        self.image3 = Image.Image
        self.image4 = Image.Image

    def cut_image(self):
        character1 = self.mask[0:-1, 3:13]
        character2 = self.mask[0:-1, 13:23]
        character3 = self.mask[0:-1, 23:33]
        character4 = self.mask[0:-1, 33:43]
        character1 = self.cut_boarder(character1)
        character2 = self.cut_boarder(character2)
        character3 = self.cut_boarder(character3)
        character4 = self.cut_boarder(character4)
        self.image1 = Image.fromarray(character1)
        self.image2 = Image.fromarray(character2)
        self.image3 = Image.fromarray(character3)
        self.image4 = Image.fromarray(character4)

    @staticmethod
    def cut_boarder(data):
        up = 0
        while sum(data[up]) == 0:
            up += 1

        down = data.shape[0] - 1
        while sum(data[down]) == 0:
            down -= 1

        left = 0
        while sum(data[:, left]) == 0:
            left += 1

        right = data.shape[1] - 1
        while sum(data[:, right]) == 0:
            right -= 1

        return data[up:down, left:right]

    def store_image(self):
        self.image1.save(self.get_file_name())
        self.image2.save(self.get_file_name())
        self.image3.save(self.get_file_name())
        self.image4.save(self.get_file_name())

    @staticmethod
    def get_file_name():
        return 'image/' + str(datetime.datetime.now().microsecond) + '.png'

    def store(self):
        self.cut_image()
        self.store_image()
