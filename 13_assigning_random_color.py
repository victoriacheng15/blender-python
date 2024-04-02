import bpy
import bmesh
from random import random

bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=1)
ico_sphere = bpy.context.active_object

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all()

ico_bmesh = bmesh.from_edit_mesh(ico_sphere.data)

for face in ico_bmesh.faces:
    red = random()
    green = random()
    blue = random()
    alpha = 1.0
    color = (red, green, blue, alpha)

    mat = bpy.data.materials.new(f"face_{face.index}")
    mat.diffuse_color = color

    ico_sphere.data.materials.append(mat)

    ico_sphere.active_material_index = face.index

    face.select = True
    bpy.ops.object.material_slot_assign()
    face.select = False

bpy.ops.object.editmode_toggle()