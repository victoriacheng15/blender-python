import bpy

bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

start_frame = 1
end_frame = 180

cube.keyframe_insert("location", frame=start_frame)

cube.location.z = 5

cube.keyframe_insert("location", frame=end_frame)