"""
Glossy Fish Eye

A fish-eye shader is used on the main surface and
a glossy specular reflection shader is used on the
offscreen canvas.
"""
fisheye = None
glossy = None
canvas = None
img = None
ball = None
use_fish_eye = True


def setup():
    global fisheye, glossy, canvas, img, ball
    size(640, 640, P3D)
    canvas = create_graphics(width, height, P3D)
    fisheye = load_shader("FishEye.glsl")
    fisheye.set("aperture", 180.0)
    glossy = load_shader("GlossyFrag.glsl", "GlossyVert.glsl")
    glossy.set("AmbientColour", 0.0, 0.0, 0.0)
    glossy.set("DiffuseColour", 0.9, 0.2, 0.2)
    glossy.set("SpecularColour", 1.0, 1.0, 1.0)
    glossy.set("AmbientIntensity", 1.0)
    glossy.set("DiffuseIntensity", 1.0)
    glossy.set("SpecularIntensity", 0.7)
    glossy.set("Roughness", 0.7)
    glossy.set("Sharpness", 0.0)
    ball = create_shape(SPHERE, 50)
    ball.set_stroke(False)


def draw():
    canvas.begin_draw()
    canvas.shader(glossy)
    canvas.no_stroke()
    canvas.background(0)
    canvas.push_matrix()
    canvas.rotate_y(frame_count * 0.01)
    canvas.point_light(204, 204, 204, 1000, 1000, 1000)
    canvas.pop_matrix()
    for x in range(0, width + 100, 100):
        for y in range(0, height + 100, 100):
            for z in range(0, 400, 100):
                canvas.push_matrix()
                canvas.translate(x, y, -z)
                canvas.shape(ball)
                canvas.pop_matrix()
    canvas.end_draw()
    if use_fish_eye:
        shader(fisheye)
    image(canvas, 0, 0, width, height)


def mouse_pressed():
    global use_fish_eye
    use_fish_eye = not use_fish_eye
    if not use_fish_eye:
        reset_shader()
