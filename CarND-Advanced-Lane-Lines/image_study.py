import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import cv2
from time import sleep

normimg = cv2.imread("/Car-ND-Projects/CarND-Advanced-Lane-Lines/harder_challenge/918.jpg")

fig, ax = plt.subplots(1,2)
plt.subplots_adjust(bottom=0.25)

initlo = 25
inithi = 100

axcolor = 'lightgoldenrodyellow'
axthreshlo = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axthreshhi = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sthreshlo = Slider(axthreshlo, 'Thresh Lo', 0, 255, valinit=initlo)
sthreshhi = Slider(axthreshhi, 'Thresh Hi', 0, 255, valinit=inithi)

def update(val):
    threshlo = int(sthreshlo.val)
    threshhi = int(sthreshhi.val)
    
    imggray = cv2.cvtColor(normimg, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(imggray,threshlo,threshhi)
    
    ax[0].imshow(cv2.cvtColor(normimg,cv2.COLOR_BGR2RGB))
    ax[1].imshow(canny,cmap='gray')    
    fig.canvas.draw_idle()

if True:    
    sthreshlo.on_changed(update)
    sthreshhi.on_changed(update)
    sleep(0.1)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sthreshlo.reset()
    sthreshhi.reset()

'''
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)
'''

plt.show()