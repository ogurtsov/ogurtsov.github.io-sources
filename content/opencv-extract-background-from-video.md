Title: Extracting background from a video using OpenCV and Python
Date: 2015-10-09 10:37
Category: Blog
Tags: opencv, python


Input video example:

[![Video](http://img.youtube.com/vi/Jjj-5OQiT-0/0.jpg)](http://www.youtube.com/watch?v=Jjj-5OQiT-0)

Result:

![Photo]({attach}attached/bg.png)


Code:

```python

import cv2
import numpy as np


def main(filename):
    capture = cv2.VideoCapture(filename)
    _, first_frame = capture.read()
     
    average = np.float32(first_frame)

    while 1:
        ret, frame = capture.read()
        cv2.accumulateWeighted(frame, average, 0.01)
        bg = cv2.convertScaleAbs(average)
        cv2.imwrite('bg.png', bg)
        
    capture.release()



if __name__ == "__main__":
    main(sys.argv[1])

```


