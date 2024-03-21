import bpy
import math

bpy.ops.mesh.primitive_cube_add()

cube = bpy.context.active_object

degrees = 90
radians = math.radians(degrees)
start_frame = 1
mid_frame = start_frame * 90
end_frame = mid_frame * 2

cube.keyframe_insert("rotation_euler", frame=start_frame)
# cube.keyfame_insert("rotation_eular")

cube.rotation_euler.z = radians

cube.keyframe_insert("rotation_euler", frame=mid_frame)

cube.rotation_euler.x = radians

cube.keyframe_insert("rotation_euler", frame=end_frame)

  