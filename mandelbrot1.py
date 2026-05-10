import pygame
from pygame import surfarray
import numpy as np
import time

# This program shows the Mandelbrot set fractal in a small window on screen
# By left-clicking with the mouse, you can zoom in on a particular region

# zoomfac set the magnification of the zoom. Increase to zoom in faster
zoomfac = 2.0

print "----------------------------"
print "A view of the Mandelbrot set"
print "----------------------------"
print "Once the fractal appears, left-click on the window to zoom in on a particular region."
print "Warning: It's rather slow, so please be patient!"
print "The Zoom Factor (magnification) is set at " + str(zoomfac)
print ""

pygame.init()  # initialise pygame 

# Set the boundary of the Mandelbrot region
x_boundary = (-2.0, 1.0)
y_boundary = (-1.0, 1.0)

# Set the patch of the complex plane that will be plotted.
xdim = x_boundary
ydim = y_boundary

# Choose the resolution, which will determine the size of the window
res = 100 
size = (res*int(xdim[1] - xdim[0]), res*int(ydim[1] - ydim[0]))
# If the code is too slow, try reducing "res"

# Create a new window, and display
pygame.display.set_caption("Mandelbrot set: click to zoom in")
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))  # white background
pygame.display.flip()

# This particular palette is borrowed from a code by Ian Mallett
#   http://geometrian.com/programming/projects/index.php?project=Mandelbrot%20Set
# You can specify your own palette with a list of RGB values
ColourPalette = [(241, 233, 191), (248, 201, 95), (255, 170, 0), (204, 108, 0), (153, 87, 0), (106, 52, 3), (66, 30, 15), (25, 7, 26), (25, 7, 26), (9, 1, 47), (4, 4, 73), (0, 7, 100), (12, 44, 138), (24, 82, 177), (57, 125, 209), (134, 181, 229), (211, 236, 248)]
nColours = len(ColourPalette)

max_it = 255  # Maximum number of function iterations

# This function maps a pixel coordinate onto a point c in the complex plane,
# and then iterates the complex function (z^2 + c) until either
#   (1) |z| > 2,  or (2) the maximum number of iterations is reached.
def fracmap(i, j):
    global max_it, size, xdim, ydim
    # First, convert the pixel coordinates into coordinates in the complex plane
    x0 = xdim[0] + i*(xdim[1]-xdim[0])/float(size[0])
    y0 = ydim[0] + j*(ydim[1]-ydim[0])/float(size[1])
    x = 0   # Start with z = x + i y = 0
    y = 0
    it = 0
    while it < max_it:
        xsq, ysq = x*x, y*y   
        if xsq + ysq > 4:   # if |z| > 2
            break
        # iterate the complex function, to get a new real and imaginary part
        x, y = xsq - ysq + x0, 2*x*y + y0
        it += 1
    return it

# Use surfarray and numpy, to get an array which holds the RGB colour values
# of each pixel in the window.
arr = pygame.surfarray.array3d(screen)

# This function changes the region of the complex plane that will be plotted,
# by zooming in on a region centred around (x1, y1)
def zoom_in(x1, y1, zoomfac):
    global xdim, ydim
    xwid = (xdim[1] - xdim[0])/zoomfac
    ywid = (ydim[1] - ydim[0])/zoomfac
    x = xdim[0] + x1*(xdim[1]-xdim[0])/float(size[0])
    y = ydim[0] + y1*(ydim[1]-ydim[0])/float(size[1])
    # Take care not to go outside the boundary:
    x = max(x_boundary[0]+xwid/2, x)
    x = min(x_boundary[1]-xwid/2, x)
    y = max(y_boundary[0]+ywid/2, y)
    y = min(y_boundary[1]-ywid/2, y)
    xdim = (x - xwid/2, x + xwid/2)
    ydim = (y - ywid/2, y + ywid/2)


ctr = 0
# Function to compute and draw the fractal
def draw_fractal():
    global ctr

    # Warn the user that this may take some time ...
    font = pygame.font.Font(None, 36)
    text = font.render("Please wait ...", 1, (10, 10, 10), pygame.Color("white"))
    textpos = text.get_rect()   
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery
    screen.blit(text, textpos)
    pygame.display.flip()
    
    t1 = time.time()
    for i in range(size[0]):
        for j in range(size[1]):
            k = fracmap(i,j)
            colour = ColourPalette[k % nColours]
            arr[i,j,:] = colour[:] 
    t2 = time.time()
    print "Computing the fractal took " + str(t2 - t1) + " secs."
    pygame.surfarray.blit_array(screen, arr)
    pygame.display.flip()

    # If you want to save the image to file, uncomment these lines:
    #pygame.image.save(surfarray.make_surface(arr),"frames/mandelbrot_frame_" + str(ctr).zfill(2) + ".png")
    #ctr += 1    

draw_fractal()

# Main loop, to respond to user input
done = False
while not done:
    # wait for user-generated events
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        done = True

    # respond to a left-button click by magnifying a region centred around the current mouse position
    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            x, y = e.pos
            zoom_in(x, y, zoomfac)
            draw_fractal()
            # we can't handle multiple clicks
            pygame.event.clear()
            
pygame.quit()


