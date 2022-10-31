# Particles, by Daniel Shiffman.
from particle_system import ParticleSystem


def setup():
    global ps
    size(512, 384, P2D)
    sprite = load_image("sprite.png")
    ps = ParticleSystem(10000, sprite)
    # Writing to the depth buffer is disabled to avoid rendering
    # artifacts due to the fact that the particles are semi-transparent
    # but not z-sorted.
    hint(DISABLE_DEPTH_MASK)


def draw():
    background(0)
    ps.update()
    ps.display()
    ps.set_emitter(mouse_x, mouse_y)
    fill(255)
    text_size(16)
    text("Frame rate: " + str(int(get_frame_rate())), 10, 20)
