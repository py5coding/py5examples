def draw():
    pass

def key_pressed(e):
    if key == CODED:
        for attr  in dir(e):
            if attr.startswith('is'):
                print(attr, getattr(e, attr)())
        print(e.get_native().getKeyText(e.get_key_code())) 
    else:
        print("key " + key)

# from collections import defaultdict
# from java.awt.event import KeyEvent
# from java.lang.reflect import Modifier
# 
# key_names = defaultdict(lambda: 'UNKNOWN')
# for f in KeyEvent.getDeclaredFields():
#     if Modifier.isStatic(f.get_modifiers()):
#         name = f.get_name()
#         if name.startswith("VK_"):
#             key_names[f.get_int(None)] = name[3:]
# 
# def keyPressed():
#     if key == CODED:
#         print(key_names[keyCode])