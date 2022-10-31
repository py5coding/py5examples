# Draws a triangle using low-level OpenGL calls.

import array

from java.nio import ByteBuffer, ByteOrder, IntBuffer
from java.lang import Float

VERT_CMP_COUNT = 4  # vertex component count (x, y, z, w) -> 4
CLR_CMP_COUNT = 4  # color component count (r, g, b, a) -> 4


def allocate_direct_float_buffer(n):
    return (ByteBuffer.allocateDirect(n * Float.SIZE / 8).
            order(ByteOrder.nativeOrder()).as_float_buffer())


vertices = array.array('f', (0,) * 12)
colors = array.array('f', (0,) * 12)

vertex_buffer = allocate_direct_float_buffer(12)
color_buffer = allocate_direct_float_buffer(12)


def setup():
    size(640, 360, P3D)

    # Loads a shader to render geometry w/out textures and lights.
    global sh
    sh = load_shader("frag.glsl", "vert.glsl")

    with begin_pgl() as pgl:
        # allocate buffer big enough to get all VBO ids back
        int_buffer = IntBuffer.allocate(2)
        pgl.gen_buffers(2, int_buffer)
        global vertex_vbo_id
        vertex_vbo_id = int_buffer.get(0)

        global color_vbo_id
        color_vbo_id = int_buffer.get(1)


def draw():
    with g.begin_pgl() as pgl:

        background(0)

        # The geometric transformations will be automatically passed
        # to the shader.
        rotate(frame_count * 0.01, width, height, 0)

        update_geometry()

        sh.bind()

        # get "vertex" attribute location in the shader
        vert_loc = pgl.get_attrib_location(sh.gl_program, "vertex")
        # enable array for "vertex" attribute
        pgl.enable_vertex_attrib_array(vert_loc)

        # get "color" attribute location in the shader
        color_loc = pgl.get_attrib_location(sh.gl_program, "color")
        # enable array for "color" attribute
        pgl.enable_vertex_attrib_array(color_loc)

        # BUFFER LAYOUT from updateGeometry()
        #
        # Vertex buffer:
        #
        #   xyzwxyzwxyzw...
        #
        #   |v1  |v2  |v3  |...
        #   |0   |4   |8   |...
        #   |xyzw|xyzw|xyzw|...
        #
        #
        # Color buffer:
        #
        #   rgbargbargba...
        #
        #   |v1  |v2  |v3  |...
        #   |0   |4   |8   |...
        #   |rgba|rgba|rgba|...
        #
        # stride (values per vertex) is 4 floats in both cases
        # vertex offset is 0 floats in both cases

        vertex_stride = VERT_CMP_COUNT * Float.BYTES
        color_stride = CLR_CMP_COUNT * Float.BYTES
        vertex_offset = 0 * Float.BYTES
        color_offset = 0 * Float.BYTES

        # VERTEX
        # bind VBO
        pgl.bind_buffer(PGL.ARRAY_BUFFER, vertex_vbo_id)
        # fill VBO with data
        pgl.buffer_data(
            PGL.ARRAY_BUFFER,
            Float.BYTES *
            len(vertices),
            vertex_buffer,
            PGL.DYNAMIC_DRAW)
        # associate currently bound VBO with "vertex" shader attribute
        pgl.vertex_attrib_pointer(
            vert_loc,
            VERT_CMP_COUNT,
            PGL.FLOAT,
            False,
            vertex_stride,
            vertex_offset)

        # COLOR
        # bind VBO
        pgl.bind_buffer(PGL.ARRAY_BUFFER, color_vbo_id)
        # fill VBO with data
        pgl.buffer_data(
            PGL.ARRAY_BUFFER,
            Float.BYTES *
            len(colors),
            color_buffer,
            PGL.DYNAMIC_DRAW)
        # associate currently bound VBO with "color" shader attribute
        pgl.vertex_attrib_pointer(
            color_loc,
            CLR_CMP_COUNT,
            PGL.FLOAT,
            False,
            color_stride,
            color_offset)

        # unbind VBOs
        pgl.bind_buffer(PGL.ARRAY_BUFFER, 0)

        pgl.draw_arrays(PGL.TRIANGLES, 0, 3)

        # disable arrays for attributes before unbinding the shader
        pgl.disable_vertex_attrib_array(vert_loc)
        pgl.disable_vertex_attrib_array(color_loc)

        sh.unbind()


def update_geometry():
    # Vertex 1
    vertices[0] = 0
    vertices[1] = 0
    vertices[2] = 0
    vertices[3] = 1

    # Color 1
    colors[0] = 1
    colors[1] = 0
    colors[2] = 0
    colors[3] = 1

    # Vertex 2
    vertices[4] = width / 2
    vertices[5] = height
    vertices[6] = 0
    vertices[7] = 1

    # Color 2
    colors[4] = 0
    colors[5] = 1
    colors[6] = 0
    colors[7] = 1

    # Vertex 3
    vertices[8] = width
    vertices[9] = 0
    vertices[10] = 0
    vertices[11] = 1

    # Color 3
    colors[8] = 0
    colors[9] = 0
    colors[10] = 1
    colors[11] = 1

    vertex_buffer.rewind()
    vertex_buffer.put(vertices)
    vertex_buffer.rewind()

    color_buffer.rewind()
    color_buffer.put(colors)
    color_buffer.rewind()
