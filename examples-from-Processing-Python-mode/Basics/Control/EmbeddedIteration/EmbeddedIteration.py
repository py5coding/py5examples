"""
Embedding Iteration.

Embedding "for" structures allows repetition in two dimensions.
"""

size(640, 360)
background(0)
no_stroke()

grid_size = 40

for x in range(grid_size, width, grid_size):
    for y in range(grid_size, height, grid_size):
        no_stroke()
        fill(255)
        rect(x - 1, y - 1, 3, 3)
        stroke(255, 50)
        line(x, y, width / 2, height / 2)
