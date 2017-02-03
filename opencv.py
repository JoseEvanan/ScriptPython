import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagen.png',0)
img = cv2.medianBlur(img,5)

BLUE = [255,0,0]
im_gray = cv2.imread('imagen.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)

#replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
#reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
#reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
#wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
#constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY)

#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
plt.subplot(),plt.imshow(im_bw,'gray'),plt.title('ORIGINAL')
#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
#plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
#plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
#plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
#plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bw_image.png', im_bw)

plt.show()

"""
import email
import smtplib

msg = email.message_from_string('warning')
msg['From'] = "jozhe25@hotmail.com"
msg['To'] = "jose.evanan@gmail.com"
msg['Subject'] = "helOoooOo"

s = smtplib.SMTP("smtp.live.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('jozhe25@hotmail.com', 'jose12345')

s.sendmail("jozhe25@hotmail.com", "jose.evanan@gmail.com", msg.as_string())

s.quit()
"""