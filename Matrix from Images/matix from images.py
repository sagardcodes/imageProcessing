from PIL import Image
import numpy as np 
img = Image.open("view.jpeg")
img = img.convert('L')
print (np.array(img))
img.show()
print ("Sagar Dahal")
