#!/usr/bin/env python3
"""HSV-based Pan-Sharpening example."""

import ee
import ee.mapclient

ee.Initialize()

# There are many fine places to look here is one.  Comment
# this out if you want to twiddle knobs while panning around.
ee.mapclient.centerMap(-61.61625, -11.64273, 14)

# Grab a sample L7 image and pull out the RGB and pan bands
# in the range (0, 1).  (The range of the pan band values was
# chosen to roughly match the other bands.)
image1 = ee.Image('LANDSAT/LE07/C01/T1/LE07_230068_19990815')

rgb = image1.select('B3', 'B2', 'B1').unitScale(0, 255)
gray = image1.select('B8').unitScale(0, 155)

# Convert to HSV, swap in the pan band, and convert back to RGB.
huesat = rgb.rgbToHsv().select('hue', 'saturation')
upres = ee.Image.cat(huesat, gray).hsvToRgb()

# Display before and after layers using the same vis parameters.
visparams = {'min': [.15, .15, .25], 'max': [1, .9, .9], 'gamma': 1.6}
ee.mapclient.addToMap(rgb, visparams, 'Orignal')
ee.mapclient.addToMap(upres, visparams, 'Pansharpened')
