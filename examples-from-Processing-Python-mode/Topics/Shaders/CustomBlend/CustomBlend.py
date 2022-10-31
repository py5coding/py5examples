"""
Custom Blend

The OpenGL-based renderers (P2D and P3D) only support some of the
blending modes available in the default renderer. The reason for this
is that the blend equations in OpenGL allow for combinations of the
form dest_factor * dest_color + src_factor * src_color of the source and
destination colors (see this page http://www.opengl.org/wiki/Blending
for an extensive discussion of blending in OpenGL).
Complex blending modes typically available in photo editing tools,
like hard light or dodge, cannot be modeled with those equations.
However, we can implement virtually any blending math directly in the
fragment shader.

This example shows how custom blend shaders can be loaded and used in
Processing.
For detailed information on how to implement Photoshop-like blending modes,
check the following pages (a bit old but still useful):
http://www.pegtop.net/delphi/articles/blendmodes/index.htm
http://mouaif.wordpress.com/2009/01/05/photoshop-math-with-glsl-shaders/
"""

dest_image = None
src_image = None
dodge = None
burn = None
overlay = None
difference = None


def setup():
    global dest_image, src_image
    size(640, 360, P2D)
    dest_image = load_image("leaves.jpg")
    src_image = load_image("moonwalk.jpg")
    init_shaders()


def draw():
    background(0)
    shader(dodge)
    draw_output(0, 0, width / 2, height / 2)
    shader(burn)
    draw_output(width / 2, 0, width / 2, height / 2)
    shader(overlay)
    draw_output(0, height / 2, width / 2, height / 2)
    shader(difference)
    draw_output(width / 2, height / 2, width / 2, height / 2)
    no_loop()


def init_shaders():
    global dodge, burn, overlay, difference
    dodge = load_shader("dodge.glsl")
    burn = load_shader("burn.glsl")
    overlay = load_shader("overlay.glsl")
    difference = load_shader("difference.glsl")
    # The names destination and source come from the OpenGL terminology:
    # destination from the image already in the framebuffer, or "base layer",
    # and source for the image that will be blended into the framebuffer, or
    # "blend layer":
    dodge.set("destSampler", dest_image)
    dodge.set("srcSampler", src_image)
    burn.set("destSampler", dest_image)
    burn.set("srcSampler", src_image)
    overlay.set("destSampler", dest_image)
    overlay.set("srcSampler", src_image)
    difference.set("destSampler", dest_image)
    difference.set("srcSampler", src_image)
    # We set the sizes of de    st and src images, and the rectangular areas
    # from the images that we will use for blending:
    dodge.set("destSize", 640, 360)
    dodge.set("destRect", 100, 50, 200, 200)
    burn.set("destSize", 640, 360)
    burn.set("destRect", 100, 50, 200, 200)
    overlay.set("destSize", 640, 360)
    overlay.set("destRect", 100, 50, 200, 200)
    difference.set("destSize", 640, 360)
    difference.set("destRect", 100, 50, 200, 200)
    dodge.set("srcSize", 640, 360)
    dodge.set("srcRect", 0, 0, 640, 360)
    burn.set("srcSize", 640, 360)
    burn.set("srcRect", 0, 0, 640, 360)
    overlay.set("srcSize", 640, 360)
    overlay.set("srcRect", 0, 0, 640, 360)
    difference.set("srcSize", 640, 360)
    difference.set("srcRect", 0, 0, 640, 360)


def draw_output(x, y, w, h):
    with push_matrix():
        translate(x, y)
        no_stroke()
        with begin_shape(QUAD):
            # Although we are not associating a texture to
            # this shape, the uv coordinates will be stored
            # anyways so they can be used in the fragment
            # shader to access the destination and source
            # images.
            vertex(0, 0, 0, 0)
            vertex(w, 0, 1, 0)
            vertex(w, h, 1, 1)
            vertex(0, h, 0, 1)
