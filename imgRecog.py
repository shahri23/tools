import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img1=Image.open('C:/Last_Attempt/Udacity/sample1.jpg')
iar1=np.asarray(img1)

img2=Image.open('C:/Last_Attempt/Udacity/sample2.jpg')
iar2=np.asarray(img2)

plt.imshow(iar2)
plt.show()
















