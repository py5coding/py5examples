# Draws a triangle using low-level OpenGL calls.

import array

from java.nio import ByteBuffer, ByteOrder, IntBuffer
from java.lang import Float

VERT_CMP_COUNT = 4  # vertex component count (x, y, z, w) -> 4
CLR_CMP_COUNT = 4  # color component count (r, g, b, a) -> 4


def allocate_direct_float_buffer(n):
    return (ByteBuffer.allocateDirect(n * Float.SIZE / 8).
            order(ByteOrder.nativeOrder()).as_float_buffer())


attribs = array.array('f', (0,) * 24)
attrib_buffer = allocate_direct_float_buffer(24)


def setup():
    size(640, 360, P3D)

    # Loads a shader to render geometry w/out textures and lights.
    global sh
    sh = load_shader("frag.glsl", "vert.glsl")

    with begin_pgl() as pgl:
        int_buffer = IntBuffer.allocate(1)
        pgl.gen_buffers(1, int_buffer)
        global attrib_vbo_id
        attrib_vbo_id = int_buffer.get(0)


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

        # xyzwrgbaxyzwrgbaxyzwrgba...
        #
        # |v1       |v2       |v3       |...
        # |0   |4   |8   |12  |16  |20  |...
        # |xyzw|rgba|xyzw|rgba|xyzw|rgba|...
        #
        # stride (values per vertex) is 8 floats
        # vertex offset is 0 floats (starts at the beginning of each line)
        # color offset is 4 floats (starts after vertex coords)
        #
        #    |0   |4   |8
        # v1 |xyzw|rgba|
        # v2 |xyzw|rgba|
        # v3 |xyzw|rgba|
        #    |...

        stride = (VERT_CMP_COUNT + CLR_CMP_COUNT) * Float.BYTES
        vertex_offset = 0 * Float.BYTES
        color_offset = VERT_CMP_COUNT * Float.BYTES

        # bind VBO
        pgl.bind_buffer(PGL.ARRAY_BUFFER, attrib_vbo_id)
        # fill VBO with data
        pgl.buffer_data(
            PGL.ARRAY_BUFFER,
            Float.BYTES *
            len(attribs),
            attrib_buffer,
            PGL.DYNAMIC_DRAW)
        # associate currently bound VBO with "vertex" shader attribute
        pgl.vertex_attrib_pointer(
            vert_loc, VERT_CMP_COUNT, PGL.FLOAT, False, stride, vertex_offset)
        # associate currently bound VBO with "color" shader attribute
        pgl.vertex_attrib_pointer(
            color_loc, CLR_CMP_COUNT, PGL.FLOAT, False, stride, color_offset)
        # unbind VBO
        pgl.bind_buffer(PGL.ARRAY_BUFFER, 0)

        pgl.draw_arrays(PGL.TRIANGLES, 0, 3)

        # disable arrays for attributes before unbinding the shader
        pgl.disable_vertex_attrib_array(vert_loc)
        pgl.disable_vertex_attrib_array(color_loc)

        sh.unbind()


def update_geometry():
    # Vertex 1
    attribs[0] = 0
    attribs[1] = 0
    attribs[2] = 0
    attribs[3] = 1

    # Color 1
    attribs[4] = 1
    attribs[5] = 0
    attribs[6] = 0
    attribs[7] = 1

    # Vertex 2
    attribs[8] = width/2
    attribs[9] = height
    attribs[10] = 0
    attribs[11] = 1

    # Color 2
    attribs[12] = 0
    attribs[13] = 1
    attribs[14] = 0
    attribs[15] = 1

    # Vertex 3
    attribs[16] = width
    attribs[17] = 0
    attribs[18] = 0
    attribs[19] = 1

    # Color 3
    attribs[20] = 0
    attribs[21] = 0
    attribs[22] = 1
    attribs[23] = 1

    attrib_buffer.rewind()
    attrib_buffer.put(attribs)
    attrib_buffer.rewind()
