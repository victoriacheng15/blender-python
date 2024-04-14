import bpy
import random

# corrdinates = []

# cordinate_count = 10
# for _ in range(cordinate_count):
#   x = random.uniform(-5,5)
#   y = random.uniform(-5,5)
#   z = random.uniform(-5,5)
#   corrdinates.append((x, y, z))

# for i in range(len(corrdinates)):
#   coord = corrdinates[i]

#   bpy.ops.mesh.primitive_ico_sphere_add(radius=1, location=coord)


# for coord in corrdinates:
#   bpy.ops.mesh.primitive_ico_sphere_add(radius=1, location=coord)

# object_count = 5

# def random_coord():
#   return random.uniform(-5,5)

# for _ in range(object_count):
#   x = random_coord()
#   y = random_coord()
#   z = random_coord()
#   bpy.ops.mesh.primitive_ico_sphere_add(radius=1, location=(x, y, z))


# for _ in range(object_count):
#   x = random_coord()
#   y = random_coord()
#   z = random_coord()
#   bpy.ops.mesh.primitive_cube_add(location=(x, y, z))


# for _ in range(object_count):
#   x = random_coord()
#   y = random_coord()
#   z = random_coord()
#   bpy.ops.mesh.primitive_cone_add(location=(x, y, z))

# # replace cubes with monkeys
# cube_objects = []

# for obj in bpy.data.objects:
#   if "cube" in obj.name.lower():
#       cube_objects.append(obj)


# for cube in cube_objects:
#    location = cube.location
#    bpy.ops.mesh.primitive_monkey_add(location=location)
#    bpy.data.objects.remove(cube)


colors = [
    [0.888, 0.515, 0.016, 1.0],
    [0.03, 0.376, 0.521, 1.0],
    [0.694, 0.019, 0.019, 1.0],
    [0.888, 0.03, 0.03, 1.0],
    [1.0, 0.22, 0.631, 1.0],
    [0.016, 0.491, 0.497, 1.0],
    [0.001, 0.694, 0.041, 1.0],
]
# add a plane
bpy.ops.mesh.primitive_plane_add()
plane_object = bpy.context.active_object

# create a new material
material = bpy.data.materials.new(name=f"random_diffuse_material")
material.diffuse_color = random.choice(colors)

# add material to object
plane_object.data.materials.append(material)