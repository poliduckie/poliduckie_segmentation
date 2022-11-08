import cv2
import pickle

'''
BirdEyeView HOW TO USE

- Set the FILE_NAME to the pickle file containing the transformation matrix
- Instance an object
- Compute the transformation by calling obj.computeBirdEye(desired image)

'''


class BirdEyeView():
    FILE_NAME = './BirdEyeCalibration/BirdEye.pkl'

    def __init__(self):
        file = open(BirdEyeView.FILE_NAME, 'rb')
        self.Matrix = pickle.load(file)
        pass

    def computeBirdEye(self, img):
        return cv2.warpPerspective(img, self.Matrix, img.shape[:2][::-1])
