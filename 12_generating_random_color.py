import bpy
import random

bpy.ops.mesh.primitive_plane_add()
plane = bpy.context.active_object


red = random.random()
green = random.random()
blue = random.random()
alpha = 1.0
color = (red, green, blue, alpha)

material = bpy.data.materials.new("radnom_material")
material.diffuse_color = color

plane.data.materials.append(material)
