import cv2
import numpy as np
import time
import os


char = " .:-=+*#%@"


def normalize_function(n, nmin=0, nmax=255, resmin=0, resmax=10):
    return char[(n * resmax) // nmax]


camera = cv2.VideoCapture(0)
normalizer = np.vectorize(normalize_function)


width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
quit = ord("q")
capturing = True


while capturing:
    # os.system("clear")  # Clearing screen
    ret, frame = camera.read()

    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Displaying camera image
    # cv2.imshow("camera", grayscale_frame)

    image = normalizer(grayscale_frame)

    for i in range(0, len(image), 10):
        for j in range(len(image[0]) - 1, 0, -5):
            print(image[i][j], end='')
        print()

    time.sleep(1/60)

    if cv2.waitKey(1) == quit:
        capturing = False

camera.release()
cv2.destroyAllWindows()
