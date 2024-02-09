import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

from astropy.io import fits

FITS_FILE = '/home/jfgout/Astro/Software/jf-photutils/test.fits'

coords = []
def onclick(event):
    global ix, iy
    global data
    ix, iy = event.xdata, event.ydata

    global imageWidth, imageHeight

    if(ix is not None and iy is not None):
        ix = int(ix)
        iy = int(iy)
        if(ix >= 0 and iy >= 0 and ix < imageWidth and iy < imageHeight):
            pixIntensity = data[int(iy)][int(ix)]
            print (f'x = {ix}, y = {iy}, intensity = {pixIntensity}')



hdulist = fits.open(FITS_FILE)
data = hdulist[0].data.astype(float)
imageWidth = len(data)
imageHeight = len(data[0])

fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.imshow(data, cmap='gray_r', origin='lower', vmin=0, vmax=2500)
plt.show()

