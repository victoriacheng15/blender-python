import bpy
import math

offset = 3
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

empty_locations = [
    (0, 0, 0),
    (0, 0, cube.dimensions.z),
    (0, -cube.dimensions.y, cube.dimensions.z),
    (0, -cube.dimensions.y, 0),
]

rotation_animation_length = 15
current_frame = 1
rotation_angle = -90

previous_empty = None

number_of_revolutions = 4

for _ in range(number_of_revolutions):
    for loc in empty_locations:
        bpy.ops.object.empty_add(type="PLAIN_AXES")
        empty = bpy.context.active_object
        empty.location = loc

        if previous_empty:
            # method 1
            # empty.parent = previous_empty
            # empty.matrix_parent_inverse = previous_empty.matrix_world.inverted()
            # method 2
            previous_empty.select_set(True)
            bpy.context.view_layer.objects.active = previous_empty
            bpy.ops.object.parent_set(keep_transform=True)
        else:
            root_empty = empty

        previous_empty = empty

        empty.keyframe_insert("rotation_euler", frame=current_frame)

        empty.rotation_euler.x = math.radians(rotation_angle)

        current_frame += rotation_animation_length
        empty.keyframe_insert("rotation_euler", frame=current_frame)

        empty.rotation_euler.x = 0

cube.parent = previous_empty
cube.location = (cube.dimensions.x / 2, cube.dimensions.y / 2, cube.dimensions.z / 2)

root_empty.location.x = 10
