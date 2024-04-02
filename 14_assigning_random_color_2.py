import bpy
import bmesh
from random import random, randint

def get_random_color():
    red = random()
    green = random()
    blue = random()
    # alpha = random()
    alpha = 1.0
    return (red, green, blue, alpha)


def generate_random_color_materials(obj, count):
    for i in range(count):
        color = get_random_color()
        mat = bpy.data.materials.new(f"material_{i}")
        mat.diffuse_color = color

        obj.data.materials.append(mat)


def add_ico_sphere():
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=1)
    return bpy.context.active_object


def assign_materials_to_faces(obj):
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all()

    bmesh_obj = bmesh.from_edit_mesh(obj.data)

    for face in bmesh_obj.faces:
        obj.active_material_index = randint(0, material_count)

        face.select = True
        bpy.ops.object.material_slot_assign()
        face.select = False

    bpy.ops.object.editmode_toggle()


material_count = 30
ico_sphere = add_ico_sphere()

generate_random_color_materials(ico_sphere, material_count)

assign_materials_to_faces(ico_sphere)