bl_info = {
    "name": "Aniuman",
    "author": "Anime By Me",
    "version": (1, 11, 11),
    "blender": (2, 80, 0),
    "location": "3D View > Mixamo> Control Rig",
    "description": "Generate a control rig from the selected Mixamo Fbx skeleton",
    "category": "Animation"}


if "bpy" in locals():
    import importlib
    if "mixamo_rig_prefs" in locals():
        importlib.reload(mixamo_rig_prefs)
    if "mixamo_rig" in locals():
        importlib.reload(mixamo_rig)  
    if "mixamo_rig_functions" in locals():
        importlib.reload(mixamo_rig_functions)  
    if "utils" in locals():
        importlib.reload(utils)  
    if "animation" in locals():
        importlib.reload(animation)  


import bpy
from . import mixamo_rig_prefs
from . import mixamo_rig
from . import mixamo_rig_functions
from . import utils

def register():
    mixamo_rig_prefs.register()
    mixamo_rig.register()
    mixamo_rig_functions.register()

def unregister():
    mixamo_rig_prefs.unregister()
    mixamo_rig.unregister()
    mixamo_rig_functions.unregister()

if __name__ == "__main__":
    register()