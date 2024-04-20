import bpy
import math
import random

def generate_colors():
    return (random.random(), random.random(), random.random(), 1.0)

def create_mesh():
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.active_object
    obj.scale = (0.6, 3, 0.2)

    random_rotation = random.uniform(0, 360)
    obj.rotation_euler.z = math.radians(random_rotation)

    bpy.ops.object.transform_apply()

    return obj

def update_obj_transform(obj, current_angle):
    obj.location.z += obj.dimensions.z
    obj.rotation_euler.z = math.radians(current_angle)

def animation_rotation(obj, current_frame, rotation_frame_count, clockwise):
    obj.animation_data_clear()
    obj.keyframe_insert("rotation_euler", frame=current_frame)

    angle = -360 if clockwise else 360

    obj.rotation_euler.z += math.radians(angle)
    frame = current_frame + rotation_frame_count
    obj.keyframe_insert("rotation_euler", frame=frame)

def create_next_layer(current_angle, current_frame, rotation_frame_count, clockwise):
    bpy.ops.object.duplicate(linked=False)
    obj = bpy.context.active_object

    mats = bpy.data.materials.new(name=f"{current_angle}-mats")

    random_color = generate_colors()
    mats.diffuse_color = random_color

    if obj.data.materials:
        obj.data.materials[0] = mats
    else:
        obj.data.materials.append(mats)
    
    update_obj_transform(obj, current_angle)

    animation_rotation(obj, current_frame, rotation_frame_count, clockwise)



def main():
    obj = create_mesh()

    angle_step = 3
    current_angle = angle_step

    current_frame = 1
    frame_step = 1
    rotation_frame_count = 90

    clockwise = True
    animation_rotation(obj, current_frame, rotation_frame_count, clockwise)

    while current_angle <= 360:
        clockwise = not clockwise
        create_next_layer(current_angle, current_frame, rotation_frame_count, clockwise)

        current_angle += angle_step
        current_frame += frame_step

    bpy.context.scene.frame_end = current_frame + rotation_frame_count
main()