# Walljuster

Simple Python script for splitting an image for use as a single wallpaper spread
across multiple monitors. **Requires the pillow library to be installed**, you
can do so through `pip install pillow`.

Sample usage:

`walljuster.py test.jpg 768x1360+0-200 2560x1080 1920x1080 -y 800`

This would create `test-0.jpg`, `test-1.jpg` and `test-2.jpg` in the current
directory, each with the respective specified resolution, with the first one
having a -200 pixels vertical offset (going up) and a global 800
pixels vertical offset (going down).

Read the usage text with `walljuster.py -h`.

There are many improvements to be made, such as:
- Vertical slicing (currently it is done only horizontally).
- Resampling, allowing an image to be resized to
fit the total resolution).
- A GUI is mandatory too, with a preview of the result and visual 
editing/guides.
- Automatically setting the wallpaper(s) from within
the program would be nice too.
  - XFCE seems to automatically apply any changes to
images set as wallpapers, so it's already possible to make adjustments on the
fly in this way.