import bpy
import math
import pprint


def get_circle_vert_corrdinates(vert_count, radius):
    vert_coordinates = list()
    angle_step = math.tau / vert_count

    for i in range(vert_count):
        current_angle = i * angle_step

        x = radius * math.cos(current_angle)
        y = radius * math.sin(current_angle)

        # this is to visualize where are these vertices
        # bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(x, y, 0))
        vert_coordinates.append((x, y, 0))

    return vert_coordinates


def create_circle_obj(vert_count, radius):
    verts = get_circle_vert_corrdinates(vert_count, radius)
    edges = []
    faces = []

    for i in range(vert_count):
        edges.append((i, (i + 1) % vert_count))
    # pprint.pprint(edges)

    mesh_data = bpy.data.meshes.new("circle_data")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new("circle_obj", mesh_data)

    bpy.context.collection.objects.link(mesh_obj)

    return mesh_obj


vert_count = 32
radius = 2
radians = math.radians(90)

first_circle = create_circle_obj(vert_count, radius)
