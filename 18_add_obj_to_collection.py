import bpy

# location_offset = 3

# for i in range(10):
#     bpy.ops.mesh.primitive_cube_add(location=(i * location_offset, 0, 0))

# for i in range(10):
#     bpy.ops.mesh.primitive_ico_sphere_add(location=(i * location_offset, 0, location_offset))

# for i in range(10):
#     bpy.ops.mesh.primitive_monkey_add(location=(i * location_offset, 0, 2 * location_offset))

# add Suz to monkey collection
# col_name = "monkeys"
# collection = bpy.data.collections["monkeys"]

# scene_collection = bpy.context.scene.collection
# scene_collection.children.link(collection)

# objs = scene_collection.objects

# for obj in objs:
#   if "Suz" in obj.name:
#     collection.objects.link(obj)
#     scene_collection.objects.unlink(obj)

"""
if objects are in specific collection e.g. "Collection"
can refer it as 
bpy.data.collections["Collection"]

to loop through objects
bpy.data.collections["Collection"].objects

additiaonlly, you can get collections under scene collection with
bpy.data.collections
"""

def get_collection(name):
  return bpy.data.collections[name]


col_names = ["monkeys", "spheres", "cubes"]
scene_collection = bpy.context.scene.collection

for col in col_names:
  collection = bpy.data.collections.get(col)
  if not collection:
    collection = bpy.data.collections.new(col)
    scene_collection.children.link(collection)

# excerise 1
# for obj in scene_collection.objects:
#   if "suz" in obj.name.lower():
#     get_collection(col_names[0]).objects.link(obj)
#     scene_collection.objects.unlink(obj)
#   if "sphere" in obj.name.lower():
#     bpy.data.collections[col_names[1]].objects.link(obj)
#     scene_collection.objects.unlink(obj)
#   if "cube" in obj.name.lower():
#     bpy.data.collections[col_names[2]].objects.link(obj)
#     scene_collection.objects.unlink(obj)



# excerise 2
obj_collection = bpy.data.collections["objects"]
if not obj_collection:
  obj_collection = bpy.data.collections.new(name="objects")
  scene_collection.children.link(obj_collection)



for col in col_names:
    obj_collection.children.link(get_collection(col))
    scene_collection.children.unlink(get_collection(col))




