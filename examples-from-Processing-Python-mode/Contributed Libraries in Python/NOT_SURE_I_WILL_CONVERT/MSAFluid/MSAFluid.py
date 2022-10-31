'''

 Demo of the MSAFluid library (www.memo.tv/msafluid_for_processing)
 Move mouse to add dye and forces to the fluid.
 LEFT mouse turns off fluid rendering, showing only particles and paths.
 RIGHT mouse turns off particles, showing only fluid rendering.
 Demonstrates feeding input into the fluid and reading data back (to update
 the particles).
 Port to processing.py by Ben Alkov, 2014.

'''
# * Copyright (c) 2008, 2009, Memo Akten, www.memo.tv
# * *** The Mega Super Awesome Visuals Company ***
# *  All rights reserved.
# *
# *  Redistribution and use in source and binary forms, with or without
# *  modification, are permitted provided that the following conditions are
# *  met:
# *
# *      * Redistributions of source code must retain the above copyright
# *        notice, this list of conditions and the following disclaimer.
# *      * Redistributions in binary form must reproduce the above copyright
# *        notice, this list of conditions and the following disclaimer in
# *        the documentation and / or other materials provided with the
# *        distribution.
# *      * Neither the name of MSA Visuals nor the names of its contributors
# *        may be used to endorse or promote products derived from this
# *        software without specific prior written permission.
# *
# *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# *  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# *  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# *  PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# *  HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# *  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# *  TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES LOSS OF USE, DATA, OR
# *  PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# *  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# *  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from particle_system import ParticleSystem
add_library('MSAFluid')

FLUID_WIDTH = 120
inv_width = 0
inv_height = 0
fluid_solver = None
particle_system = None
draw_fluid = True
draw_sparks = True
img_fluid = None
aspect_ratio = 0


def setup():
    size(784, 484, OPENGL)
    inv_width = 1.0 / width
    inv_height = 1.0 / height
    aspect_ratio = (width * inv_height) ** 2

    # Create fluid and set options.
    fluid_solver = MSAFluidSolver2D((FLUID_WIDTH),
                                    (FLUID_WIDTH * height / width))
    fluid_solver.enable_rgb(True).set_fade_speed(
        0.003).set_delta_t(0.5).set_visc(0.0001)

    # Create image to hold fluid picture.
    img_fluid = create_image(fluid_solver.get_width(),
                             fluid_solver.get_height(), RGB)
    particle_system = ParticleSystem()


def mouse_moved():
    mouse_norm_x = mouse_x * inv_width
    mouse_norm_y = mouse_y * inv_height
    mouse_vel_x = (mouse_x - pmouse_x) * inv_width
    mouse_vel_y = (mouse_y - pmouse_y) * inv_height
    add_force(mouse_norm_x, mouse_norm_y, mouse_vel_x, mouse_vel_y)


def draw():
    fluid_solver.update()
    if draw_fluid:
        img_fluid.load_pixels()
        for i in range(fluid_solver.get_num_cells()):
            img_fluid.pixels[i] = color(fluid_solver.r[i] * 2,
                                        fluid_solver.g[i] * 2,
                                        fluid_solver.b[i] * 2)
        img_fluid.update_pixels()
        image(img_fluid, 0, 0, width, height)
    if draw_sparks:
        particle_system.update_and_draw(inv_width, inv_height,
                                        draw_fluid, fluid_solver)


def mouse_pressed():
    if mouse_button == LEFT:
        draw_fluid = not draw_fluid
    elif mouse_button == RIGHT:
        draw_sparks = not draw_sparks


# Add force and dye to fluid, and create particles.
def add_force(x, y, dx, dy):

    # Balance the x and y components of speed with the screen aspect ratio.
    speed = dx**2 + (dy**2 * aspect_ratio)
    if speed > 0:
        x = constrain(x, 0, 1)
        y = constrain(y, 0, 1)
        color_mult = 5
        velocity_mult = 30.0
        index = fluid_solver.get_index_for_normalized_position(x, y)
        color_mode(HSB, 360, 1, 1)
        hue = ((x + y) * 180 + frame_count) % 360
        draw_color = color(hue, 1, 1)
        color_mode(RGB, 1)

        fluid_solver.r_old[index] += red(draw_color) * color_mult
        fluid_solver.g_old[index] += green(draw_color) * color_mult
        fluid_solver.b_old[index] += blue(draw_color) * color_mult
        particle_system.add_particles(x * width, y * height, 10)
        fluid_solver.u_old[index] += dx * velocity_mult
        fluid_solver.v_old[index] += dy * velocity_mult
