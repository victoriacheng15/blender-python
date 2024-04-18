import bpy
from random import random, uniform


# def create_plane_with_color(color, location):
#     bpy.ops.mesh.primitive_plane_add()
#     plane_object = bpy.context.active_object
#     plane_object.location = location

#     material = bpy.data.materials.new(name=f"diffuse_material")
#     material.diffuse_color = color

#     plane_object.data.materials.append(material)

# my_colors = {
#     "Brick Red": (0.4019, 0.068478, 0.0578054, 1.0),
#     "Neon Red": (1.0, 0.0307132, 0.0307135, 1.0), 
#     "Pastel Red": (0.955973, 0.351532, 0.351533, 1.0),
#     "randomized_color": (random(), random(), random() , 1.0)
# }

# color = my_colors.get("randomized_color")
# create_plane_with_color(color, location=(0, 0, 0))

# create_plane_with_color(my_colors["Neon Red"], location=(0, 3, 0))


# list_of_keys = list(my_colors.keys())

# # select a random key
# random_key = random.choice(list_of_keys)

# color = my_colors[random_key]
# create_plane_with_color(color, location=(0, 6, 0))



# example 2
# object_count = 10
# for _ in range(object_count):
#     x = uniform(-5, 5)
#     y = uniform(-5, 5)
#     z = uniform(-5, 5)
#     bpy.ops.mesh.primitive_ico_sphere_add(radius=1, location=(x, y, z))

# # add cubes into the scene
# for _ in range(object_count):
#     x = uniform(-5, 5)
#     y = uniform(-5, 5)
#     z = uniform(-5, 5)
#     bpy.ops.mesh.primitive_cube_add(location=(x, y, z))

# # add cones into the scene
# for _ in range(object_count):
#     x = uniform(-5, 5)
#     y = uniform(-5, 5)
#     z = uniform(-5, 5)
#     bpy.ops.mesh.primitive_cone_add(location=(x, y, z))


cube_key = "cubes"
ico_key = "spheres"
cone_key = "cones"

# create a dict of mesh lists
mesh_objects = {
    cube_key: list(),
    ico_key: list(),
    cone_key: list(),
}

for obj in bpy.data.objects:
    if "Cube" in obj.name:
        mesh_objects[cube_key].append(obj)
        continue

    if "Ico" in obj.name:
        mesh_objects[ico_key].append(obj)
        continue

    if "Cone" in obj.name:
        mesh_objects[cone_key].append(obj)


# create a dict of locations
mesh_z_locations = {
    cube_key: 0,
    ico_key: -5,
    cone_key: 5,
}

# loop over the meshes
for key, value in mesh_objects.items():
    for mesh_obj in value:
        mesh_obj.location.z = mesh_z_locations[key]