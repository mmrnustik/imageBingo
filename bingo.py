import numpy as np
import os
import sys

import cv2


def bingo(imgs):
    """ generates bingo matrix from images in imgs
        returns large image
    """
    s = imgs[0].shape[0]   # size of small image in pixels
    n = int(np.sqrt(len(imgs)))  # size of large image in images
    sI = (s + 1) * n + 1  # size of large image in pixels
    I = np.zeros((sI, sI))

    for i in range(n * n):
        x = (i % 5) * (s + 1) + 1
        y = (i / 5) * (s + 1) + 1
        I[x:x+s, y:y+s] = imgs[i]
    return I


def unique_permutations(N, n, count):
    """ returns list of unique permutations of N shortened to n
    """
    def arrayInList(a, L):
        for l in L:
            if np.array_equal(a, l):
                return True
        return False

    P = []
    for i in range(count):
        while True:
            p = np.random.permutation(N)[:n]
            if not arrayInList(p, P):
                break
        P.append(p)

    return P


if __name__ == '__main__':
    try:
        n, count, input_dir = sys.argv[1:4]

        files = [input_dir + f for f in os.listdir(input_dir)]
        # print files
        images = np.array([cv2.imread(f, 0) for f in files])

        i = 0
        bingos = []
        for p in unique_permutations(len(images), n*n, count):
            img = bingo(images[p][:n*n])
            i += 1
            cv2.imwrite('out/{:02d}.png'.format(i), img)

    except Exception as e:
        print e
        print """
        Usage:
        python2 bingo.py n count input_dir
        n - side of square for bingo (if you want 5x5 images, n is 5)
        count - how many bingo tiles you want in pdf files
        input_dir - directory with square images of the same size
        """
