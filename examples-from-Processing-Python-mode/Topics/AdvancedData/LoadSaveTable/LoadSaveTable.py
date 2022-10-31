"""
Loading Tabular Data
by Daniel Shiffman.

This example demonstrates how to use load_table()
to retrieve data from a CSV file and make objects
from that data.
Here is what the CSV looks like:

x,y,diameter,name
160,103,43.19838,Happy
372,137,52.42526,Sad
273,235,61.14072,Joyous
121,179,44.758068,Melancholy
"""
from Bubble import Bubble

# A list of Bubble objects
bubbles = []


def setup():
    size(640, 360)
    load_data()


def draw():
    background(255)
    # Display all bubbles
    for b in bubbles:
        b.display()
        b.rollover(mouse_x, mouse_y)

    text_align(LEFT)
    fill(0)
    text("Click to add bubbles.", 10, height - 10)


def load_data():
    # Load CSV file into a Table object
    global table
    global bubbles
    # "header" option indicates the file has a header row
    table = load_table("data.csv", "header")
    bubbles = []

    for row in table.rows():
        # You can access the fields via their column name (or index)
        x = row.get_float("x")
        y = row.get_float("y")
        d = row.get_float("diameter")
        n = row.get_string("name")
        # Make a Bubble object out of the data read
        bubbles.append(Bubble(x, y, d, n))


def mouse_pressed():
    global table
    # Create a new row
    row = table.add_row()
    # Set the values of that row
    row.set_float("x", mouse_x)
    row.set_float("y", mouse_y)
    row.set_float("diameter", random(40, 80))
    row.set_string("name", "Blah")

    # If the table has more than 10 rows
    if table.get_row_count() > 10:
        # Delete the oldest row
        table.remove_row(0)

    # Writing the CSV back to the same file
    save_table(table, "data/data.csv")
    # And reloading it
    load_data()
