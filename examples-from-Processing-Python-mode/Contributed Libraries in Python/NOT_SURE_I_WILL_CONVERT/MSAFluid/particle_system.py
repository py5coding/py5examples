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

from javax.media.opengl import GL
from particle import Particle


class ParticleSystem(object):
    def __init__(self, max_particles=5000):
        self.max_particles = max_particles
        self.cur_index = 0
        self.particles = [Particle() for _ in range(self.max_particles)]

    def _fade_to_color(self, gl2, red, green, blue, speed):
        gl2.gl_blend_func(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        gl2.gl_color4f(red, green, blue, speed)
        gl2.gl_begin(gl2.gl_quads)
        gl2.gl_vertex2f(0, 0)
        gl2.gl_vertex2f(width, 0)
        gl2.gl_vertex2f(width, height)
        gl2.gl_vertex2f(0, height)
        gl2.gl_end()

    def update_and_draw(self, inv_width, inv_height, draw_fluid, fluid_solver):
        with begin_pgl() as pgl:
            gl2 = pgl.gl.get_gl2()
            gl2.gl_enable(GL.GL_BLEND)  # Enable blending.
            if not draw_fluid:
                self._fade_to_color(gl2, 0, 0, 0, 0.05)

            # Additive blending (ignore alpha).
            gl2.gl_blend_func(gl2.gl_one, GL.GL_ONE)

            # Make points round.
            gl2.gl_enable(gl2.gl_line_smooth)
            gl2.gl_line_width(1)

            # Start drawing points.
            gl2.gl_begin(gl2.gl_lines)
            for particle in self.particles:
                if particle.alpha > 0:
                    particle.update(inv_width, inv_height, fluid_solver)
                    # Use oldschool rendering.
                    particle.draw_old_school(gl2)
            gl2.gl_end()
            gl2.gl_disable(GL.GL_BLEND)

    def add_particle(self, x, y):
        self.particles[self.cur_index].init(x, y)
        self.cur_index += 1
        if self.cur_index >= self.max_particles:
            self.cur_index = 0

    def add_particles(self, x, y, count):
        for _ in range(count):
            self.add_particle(x + random(-15, 15), y + random(-15, 15))
