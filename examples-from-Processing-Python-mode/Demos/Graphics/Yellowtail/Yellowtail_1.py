"""
 * Yellowtail
 * by Golan Levin (www.flong.com).
 * Translated to Python by Jonathan Feinberg.
 *
 * Click, drag, and release to create a kinetic gesture.
 *
 * Yellowtail (1998-2000) is an interactive software system for the gestural
 * creation and performance of real-time abstract animation. Yellowtail repeats
 * a user's strokes end-over-end, enabling simultaneous specification of a
 * line's shape and quality of movement. Each line repeats according to its
 * own period, producing an ever-changing and responsive display of lively,
 * worm-like textures.
 """

from gesture import Gesture

n_gestures = 36    # Number of gestures
min_move = 3       # Minimum travel for a point
gesture_array = []


def setup():
    global gesture_array, current_gesture_id
    size(1024, 768, P2D)
    background(0, 0, 0)
    no_stroke()
    for _ in range(n_gestures):
        gesture_array.append(Gesture(width, height))
    current_gesture_id = -1
    clear_gestures()


def draw():
    background(0)
    update_geometry()
    fill(255, 255, 245)
    for gesture in gesture_array:
        render_gesture(gesture, width, height)


def mouse_pressed():
    global current_gesture_id
    current_gesture_id = (current_gesture_id + 1) % n_gestures
    gesture = gesture_array[current_gesture_id]
    gesture.clear()
    gesture.clear_polys()
    gesture.add_point(mouse_x, mouse_y)


def mouse_dragged():
    if current_gesture_id >= 0:
        gesture = gesture_array[current_gesture_id]
        if gesture.dist_to_last(mouse_x, mouse_y) > min_move:
            gesture.add_point(mouse_x, mouse_y)
            gesture.smooth()
            gesture.compile()


def key_pressed():
    if key in ('+', '='):
        if current_gesture_id >= 0:
            th = gesture_array[current_gesture_id].thickness
            gesture_array[current_gesture_id].thickness = min(96, th + 1)
            gesture_array[current_gesture_id].compile()
    elif key == '-':
        if current_gesture_id >= 0:
            th = gesture_array[current_gesture_id].thickness
            gesture_array[current_gesture_id].thickness = max(2, th - 1)
            gesture_array[current_gesture_id].compile()
    elif key == ' ':
        clear_gestures()


def render_gesture(gesture, w, h):
    if not gesture.exists:
        return
    if gesture.n_polys <= 0:
        return
    with begin_shape(QUADS):
        for i, p in enumerate(gesture.polygons):
            xpts = p.xpoints
            ypts = p.ypoints
            vertices(tuple(zip(p.xpoints, p.ypoints)))
            cr = gesture.crosses[i]
            if cr > 0:
                if (cr & 3) > 0:
                    vertices((
                        (xpts[0] + w, ypts[0]),
                        (xpts[1] + w, ypts[1]),
                        (xpts[2] + w, ypts[2]),
                        (xpts[3] + w, ypts[3]),
                        (xpts[0] - w, ypts[0]),
                        (xpts[1] - w, ypts[1]),
                        (xpts[2] - w, ypts[2]),
                        (xpts[3] - w, ypts[3]),
                        ))
                if (cr & 12) > 0:
                    vertices((
                        (xpts[0], ypts[0] + h),
                        (xpts[1], ypts[1] + h),
                        (xpts[2], ypts[2] + h),
                        (xpts[3], ypts[3] + h),
                        (xpts[0], ypts[0] - h),
                        (xpts[1], ypts[1] - h),
                        (xpts[2], ypts[2] - h),
                        (xpts[3], ypts[3] - h),
                        ))
                # I have knowingly retained the small flaw of not
                # completely dealing with the corner conditions
                # (the case in which both of the above are True).


def update_geometry():
    for i in range(n_gestures):
        gesture = gesture_array[i]
        if not gesture.exists:
            continue
        if (i != current_gesture_id or not is_mouse_pressed):
            advance_gesture(gesture)


def advance_gesture(gesture):
    # Move a Gesture one step
    if (not gesture.exists) or (gesture.n_points < 1):
        return
    jx = gesture.jump_dx
    jy = gesture.jump_dy
    path = gesture.path
    for i in range(gesture.n_points - 1, 0, -1):
        path[i].x = path[i - 1].x
        path[i].y = path[i - 1].y
    path[0].x = path[gesture.n_points - 1].x - jx
    path[0].y = path[gesture.n_points - 1].y - jy
    gesture.compile()


def clear_gestures():
    for g in gesture_array:
        g.clear()
