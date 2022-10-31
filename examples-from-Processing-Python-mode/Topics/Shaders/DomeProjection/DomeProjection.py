"""
DomeProjection

This sketch uses use environmental mapping to render the output
on a full spherical dome.

Based on the FullDomeTemplate code from Christopher Warnow:
https://github.com/mphasize/FullDome
"""

import java.nio._int_buffer
cubemap_shader = None
dome_sphere = None
fbo = None
rbo = None
env_map_texture_id = None
env_map_size = 1024


def setup():
    size(640, 640, P3D)
    init_cube_map()


def draw():
    background(0)
    draw_cube_map()


def draw_scene():
    background(0)
    stroke(255, 0, 0)
    stroke_weight(2)
    for i in range(-width, 2 * width, 50):
        line(i, -height, -100, i, 2 * height, -100)
    for i in range(height, 2 * height, 50):
        line(-width, i, -100, 2 * width, i, -100)
    lights()
    no_stroke()
    translate(mouse_x, mouse_y, 200)
    rotate_x(frame_count * 0.01)
    rotate_y(frame_count * 0.01)
    box(100)


def init_cube_map():
    sphere_detail(50)
    dome_sphere = create_shape(SPHERE, height / 2.0)
    dome_sphere.rotate_x(HALF_PI)
    dome_sphere.set_stroke(False)
    pgl = begin_pgl()
    env_map_texture_id = IntBuffer.allocate(1)
    pgl.gen_textures(1, env_map_texture_id)
    pgl.bind_texture(PGL.TEXTURE_CUBE_MAP, env_map_texture_id.get(0))
    pgl.tex_parameteri(
        PGL.TEXTURE_CUBE_MAP, PGL.TEXTURE_WRAP_S, PGL.CLAMP_TO_EDGE)
    pgl.tex_parameteri(
        PGL.TEXTURE_CUBE_MAP, PGL.TEXTURE_WRAP_T, PGL.CLAMP_TO_EDGE)
    pgl.tex_parameteri(
        PGL.TEXTURE_CUBE_MAP, PGL.TEXTURE_WRAP_R, PGL.CLAMP_TO_EDGE)
    pgl.tex_parameteri(
        PGL.TEXTURE_CUBE_MAP, PGL.TEXTURE_MIN_FILTER, PGL.NEAREST)
    pgl.tex_parameteri(
        PGL.TEXTURE_CUBE_MAP, PGL.TEXTURE_MAG_FILTER, PGL.NEAREST)
    for i in range(
            PGL.TEXTURE_CUBE_MAP_POSITIVE_X,
            PGL.TEXTURE_CUBE_MAP_POSITIVE_X + 6):
        pgl.tex_image2_d(
            i,
            0,
            PGL.RGBA8,
            env_map_size,
            env_map_size,
            0,
            PGL.RGBA,
            PGL.UNSIGNED_BYTE,
            null)
    # Init fbo, rbo
    fbo = IntBuffer.allocate(1)
    rbo = IntBuffer.allocate(1)
    pgl.gen_framebuffers(1, fbo)
    pgl.bind_framebuffer(PGL.FRAMEBUFFER, fbo.get(0))
    pgl.framebuffer_texture2_d(
        PGL.FRAMEBUFFER,
        PGL.COLOR_ATTACHMENT0,
        PGL.TEXTURE_CUBE_MAP_POSITIVE_X,
        env_map_texture_id.get(0),
        0)
    pgl.gen_renderbuffers(1, rbo)
    pgl.bind_renderbuffer(PGL.RENDERBUFFER, rbo.get(0))
    pgl.renderbuffer_storage(
        PGL.RENDERBUFFER, PGL.DEPTH_COMPONENT24, env_map_size, env_map_size)
    # Attach depth buffer to FBO
    pgl.framebuffer_renderbuffer(
        PGL.FRAMEBUFFER, PGL.DEPTH_ATTACHMENT, PGL.RENDERBUFFER, rbo.get(0))
    end_pgl()
    # Load cubemap shader.
    cubemap_shader = load_shader("cubemapfrag.glsl", "cubemapvert.glsl")
    cubemap_shader.set("cubemap", 1)


def draw_cube_map():
    pgl = begin_pgl()
    pgl.active_texture(PGL.TEXTURE1)
    pgl.enable(PGL.TEXTURE_CUBE_MAP)
    pgl.bind_texture(PGL.TEXTURE_CUBE_MAP, env_map_texture_id.get(0))
    regenerate_env_map(pgl)
    end_pgl()
    draw_dome_master()
    pgl.disable(PGL.TEXTURE_CUBE_MAP)
    pgl.bind_texture(PGL.TEXTURE_CUBE_MAP, 0)


def draw_dome_master():
    camera()
    ortho(0, width, 0, height)
    reset_matrix()
    shader(cubemap_shader)
    shape(dome_sphere)
    reset_shader()

# Called to regenerate the envmap


def regenerate_env_map(pgl):
    # bind fbo
    pgl.bind_framebuffer(PGL.FRAMEBUFFER, fbo.get(0))
    # generate 6 views from origin(0, 0, 0)
    pgl.viewport(0, 0, env_map_size, env_map_size)
    perspective(90.0 * DEG_TO_RAD, 1.0, 1.0, 1025.0)
    for face in range(
            PGL.TEXTURE_CUBE_MAP_POSITIVE_X,
            PGL.TEXTURE_CUBE_MAP_NEGATIVE_Z):
        reset_matrix()
        if face == PGL.TEXTURE_CUBE_MAP_POSITIVE_X:
            camera(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -1.0, 0.0)
        elif face == PGL.TEXTURE_CUBE_MAP_NEGATIVE_X:
            camera(0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0)
        elif face == PGL.TEXTURE_CUBE_MAP_POSITIVE_Y:
            camera(0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0)
        elif face == PGL.TEXTURE_CUBE_MAP_NEGATIVE_Y:
            camera(0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
        elif face == PGL.TEXTURE_CUBE_MAP_POSITIVE_Z:
            camera(0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.0)
        scale(-1, 1, -1)
        translate(-width * 0.5, -height * 0.5, -500)
        pgl.framebuffer_texture2_d(
            PGL.FRAMEBUFFER,
            PGL.COLOR_ATTACHMENT0,
            face,
            env_map_texture_id.get(0),
            0)
        draw_scene()  # Draw objects in the scene
        # Make sure that the geometry in the scene is pushed to the GPU
        flush()
        no_lights()  # Disabling lights to avoid adding many times
        pgl.framebuffer_texture2_d(
            PGL.FRAMEBUFFER, PGL.COLOR_ATTACHMENT0, face, 0, 0)
