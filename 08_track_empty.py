import bpy

cube_count = 10
location_offset = 3
frame_count = 300

bpy.context.scene.frame_end = frame_count

for i in range(cube_count):
  bpy.ops.mesh.primitive_cube_add(size=2, location=(0, i * location_offset, 0))

bpy.ops.object.empty_add() 
empty = bpy.context.active_object

empty.keyframe_insert("location", frame=1)
empty.location.y = cube_count * location_offset
empty.keyframe_insert("location", frame=frame_count)

bpy.ops.object.camera_add()
camera = bpy.context.active_object
camera.location.x = 15
camera.location.y = cube_count * location_offset / 2
camera.location.z = 2

bpy.ops.object.constraint_add(type='TRACK_TO')
camera.constraints["Track To"].target = empty

# excerise 1 
# empty.keyframe_insert("location", frame=1)
# empty.location.y = cube_count * location_offset
# empty.keyframe_insert("location", frame=frame_count)

# bpy.ops.object.camera_add()
# camera = bpy.context.active_object
# camera.location.x = 15
# camera.location.z = 2

# camera.keyframe_insert("location", frame=1)
# camera.location.y = cube_count * location_offset
# camera.keyframe_insert("location", frame=frame_count)

# bpy.ops.object.constraint_add(type='TRACK_TO')
# camera.constraints["Track To"].target = empty

# excerise 2 
# empty.location.y = cube_count * location_offset / 2

# bpy.ops.object.camera_add()
# camera = bpy.context.active_object
# camera.location.x = 15
# camera.location.z = 2

# camera.keyframe_insert("location", frame=1)
# camera.location.y = cube_count * location_offset
# camera.keyframe_insert("location", frame=frame_count)

# bpy.ops.object.constraint_add(type='TRACK_TO')
# camera.constraints["Track To"].target = empty

