"""
Texture Sphere
by Mike 'Flux' Chang.
Based on code by Toxi.

A 3D textured sphere with simple rotation control.
Note: Controls will be inverted when sphere is upside down.
Use an "arc ball" to deal with this appropriately.
"""

third_width = None
half_height = None
texmap = None

# Sphere detail setting.
sphere_res = 35
rotation_x = 0
rotation_y = 0
velocity_x = 0
velocity_y = 0
globe_radius = 400
push_back = 0

# float lists
cx = []
cz = []
sphere_x = []
sphere_y = []
sphere_z = []
sin_lut = []
cos_lut = []

SinCosPrecision = 0.5
SinCosLength = int(360.0 / SinCosPrecision)


def setup():
    size(640, 360, P3D)
    global third_width, half_height, texmap
    third_width = width * 0.33
    half_height = height * 0.5
    texmap = load_image("world32k.jpg")
    initialize_sphere(sphere_res)


def draw():
    background(0)
    render_globe()


def render_globe():
    global rotation_x, rotation_y, velocity_x, velocity_y
    with push_matrix():
        translate(third_width, half_height, push_back)

        with push_matrix():
            no_fill()
            stroke(255, 200)
            stroke_weight(2)
            smooth()

        lights()

        with push_matrix():
            rotate_x(radians(-rotation_x))
            rotate_y(radians(270 - rotation_y))
            fill(200)
            no_stroke()
            texture_mode(IMAGE)
            textured_sphere(globe_radius, texmap)

    rotation_x += velocity_x
    rotation_y += velocity_y
    velocity_x *= 0.95
    velocity_y *= 0.95

    # Implements mouse control (interaction will be inverted when sphere is
    # upside down).
    if mouse_pressed:
        velocity_x += (mouse_y - pmouse_y) * 0.01
        velocity_y -= (mouse_x - pmouse_x) * 0.01


def initialize_sphere(res):
    global sphere_res
    for i in range(SinCosLength):
        sin_lut.append(sin(radians(i * SinCosPrecision)))
        cos_lut.append(cos(radians(i * SinCosPrecision)))
    delta = SinCosLength / res

    # Calc unit circle in XZ plane.
    for i in range(res):
        cx.append(-cos_lut[int((i * delta) % SinCosLength)])
        cz.append(sin_lut[int((i * delta) % SinCosLength)])

    # Computing Vertex list. Vertex list starts at south pole.
    vert_count = res * (res - 1) + 2
    angle_step = (SinCosLength * 0.5) / res
    angle = angle_step

    # Step along Y axis.
    for i in range(1, res):
        curradius = sin_lut[int(angle % SinCosLength)]
        curr_y = -cos_lut[int(angle % SinCosLength)]
    # Init lists to store vertices.
        for j in range(res):
            sphere_x.append(cx[j] * curradius)
            sphere_y.append(curr_y)
            sphere_z.append(cz[j] * curradius)
        angle += angle_step
    sphere_res = res


# Generic routine to draw textured sphere.
def textured_sphere(radius, texmap):
    radius = (radius + 240) * 0.33

    begin_shape(TRIANGLE_STRIP)
    texture(texmap)
    iu = (texmap.width - 1) / sphere_res
    iv = (texmap.height - 1) / sphere_res
    u = 0
    v = iv
    for i in range(sphere_res):
        vertex(0, -radius, 0, u, 0)
        vertex(sphere_x[i] * radius,
               sphere_y[i] * radius,
               sphere_z[i] * radius,
               u, v)
        u += iu
    vertex(0, -radius, 0, u, 0)
    vertex(sphere_x[0] * radius,
           sphere_y[0] * radius,
           sphere_z[0] * radius,
           u, v)
    end_shape()

    # Middle rings.
    voff = 0
    for i in range(2, sphere_res):
        v1 = voff
        v11 = voff
        voff += sphere_res
        v2 = voff
        u = 0
        begin_shape(TRIANGLE_STRIP)
        texture(texmap)
        for j in range(sphere_res):
            vertex(sphere_x[v1] * radius,
                   sphere_y[v1] * radius,
                   sphere_z[v1] * radius,
                   u, v)
            v1 += 1
            vertex(sphere_x[v2] * radius,
                   sphere_y[v2] * radius,
                   sphere_z[v2] * radius,
                   u, v + iv)
            v2 += 1
            u += iu

        # Close each ring.
        v1 = v11
        v2 = voff
        vertex(sphere_x[v1] * radius,
               sphere_y[v1] * radius,
               sphere_z[v1] * radius,
               u, v)
        vertex(sphere_x[v2] * radius,
               sphere_y[v2] * radius,
               sphere_z[v2] * radius,
               u, v + iv)
        end_shape()
        v += iv
    u = 0

    # Add the northern cap.
    begin_shape(TRIANGLE_STRIP)
    texture(texmap)
    for i in range(sphere_res):
        v2 = voff + i
        vertex(sphere_x[v2] * radius,
               sphere_y[v2] * radius,
               sphere_z[v2] * radius,
               u, v)
        vertex(0, radius, 0, u, v + iv)
        u += iu
    vertex(sphere_x[voff] * radius,
           sphere_y[voff] * radius,
           sphere_z[voff] * radius,
           u, v)
    end_shape()
