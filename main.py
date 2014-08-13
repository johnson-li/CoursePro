__author__ = 'johnson'

import character
import Image
import os


def generate_characters():
    files = os.listdir('/home/johnson/workspace/verificationCode/')
    n = 0
    for imageFile in files:
        n += 1
        print imageFile
        if not imageFile.__contains__('jpg'):
            continue
        if n >= 50:
            break

        my_character = character.Character('/home/johnson/workspace/verificationCode/' + imageFile)
        my_character.store()


def classify_characters():
    files = os.listdir('image')
    for imageFile in files:
        image = Image.open('image/' + imageFile)
        image.show()
        value = raw_input()
        path = 'classified/' + value
        if not os.path.isdir(path):
            os.mkdir(path)
        os.rename('image/' + imageFile, path + '/' + imageFile)

classify_characters()
