# Walljuster

Simple Python script for splitting an image for use as a single wallpaper spread
across multiple monitors.

Sample usage:

`walljuster.py test.jpg 768x1360+0-200 2560x1080 1920x1080 -y 800`

This would create `test-0.jpg`, `test-1.jpg` and `test-2.jpg` in the current
directory, each with the respective specified resolution, with the first one
having a -200 pixels vertical offset (going up) and a global 800
pixels vertical offset (going down).

Read the usage text with `walljuster.py -h`.