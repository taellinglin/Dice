import os
import random

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, NodePath, Shader
from panda3d.core import LVector3f
import math

configVars = """
win-size 1920 1080
fullscreen 1
show-frame-rate-meter 0
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.disable_mouse()  # Disable mouse navigation of the scene

        # Set up camera with a larger FOV
        self.cam.node().get_lens().set_fov(90)

        # Randomly select shaders for the room and dice
        room_vertex_shader, room_fragment_shader = self.get_random_shaders("shaders")
        dice_vertex_shader, dice_fragment_shader = self.get_random_shaders("shaders")

        # Load a random BAM file for the room
        room_bam_file = self.get_random_file("room", ".bam")

        # Rotate the room along the y-axis (spin horizontally)
        if room_vertex_shader and room_fragment_shader:
            room_shader = Shader.load(Shader.SL_GLSL, vertex=room_vertex_shader, fragment=room_fragment_shader)
            self.room = self.loader.loadModel(room_bam_file)
            self.room.reparentTo(self.render)
            self.room.set_shader(room_shader)
            self.room.set_shader_input("iResolution", (self.win.getXSize(), self.win.getYSize()))
            self.room.set_shader_input("iTime", 0.0)
            self.room.set_shader_input("iMouse", (self.win.getXSize() / 2, self.win.getYSize() / 2))
            self.taskMgr.add(self.rotate_room, "rotate_room")
        else:
            print("Unable to find matching shaders for the room.")

        # Load a random BAM file for the dice
        dice_bam_file = self.get_random_file("dice", ".bam")

        # Load dice model and position it in the center of the room
        if dice_vertex_shader and dice_fragment_shader:
            dice_shader = Shader.load(Shader.SL_GLSL, vertex=dice_vertex_shader, fragment=dice_fragment_shader)
            self.dice = self.loader.loadModel(dice_bam_file)
            self.dice.reparentTo(self.room)
            self.dice.set_pos(0, 0, 0)
            self.dice.set_shader(dice_shader)
            self.dice.set_shader_input("iResolution", (self.win.getXSize(), self.win.getYSize()))
            self.dice.set_shader_input("iTime", 0.0)
            self.dice.set_shader_input("iMouse", (self.win.getXSize() / 2, self.win.getYSize() / 2))
            self.taskMgr.add(self.rotate_dice, "rotate_dice")
        else:
            print("Unable to find matching shaders for the dice.")

        # Calculate the camera position based on the dice model's bounding box
        dice_bounds = self.dice.get_tight_bounds()
        dice_center = (dice_bounds[0] + dice_bounds[1]) / 2  # Calculate the center of the bounding box
        dice_radius = (dice_bounds[1] - dice_bounds[0]).length() / 2  # Calculate the radius of the bounding box
        camera_fov = self.cam.node().get_lens().get_hfov()  # Get the horizontal field of view

        # Adjust the camera distance for a better fit
        camera_distance = dice_radius / math.tan(math.radians(camera_fov / 2))
        camera_distance *= 1.5  # Increase the distance multiplier to adjust the camera offset

        # Set the camera position to look at the dice
        self.cam.set_pos(dice_center - LVector3f(0, -camera_distance, 0))
        self.cam.look_at(dice_center)

        # Variables for camera rolling effect
        self.roll_amplitude = 2  # Amplitude of the roll effect
        self.roll_frequency = 1  # Frequency of the roll effect
        self.roll_phase_offset = 0  # Phase offset of the roll effect
        self.roll_angle = 0  # Current roll angle

        self.accept("aspectRatioChanged", self.win_resize)
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        ft = globalClock.get_frame_time()
        self.room.set_shader_input("iTime", ft)
        self.dice.set_shader_input("iTime", ft)
        return task.cont

    def win_resize(self):
        self.room.set_shader_input("iResolution", (self.win.getXSize(), self.win.getYSize()))
        self.room.set_shader_input("iMouse", (self.win.getXSize() / 2, self.win.getYSize() / 2))
        self.dice.set_shader_input("iResolution", (self.win.getXSize(), self.win.getYSize()))
        self.dice.set_shader_input("iMouse", (self.win.getXSize() / 2, self.win.getYSize() / 2))

    def rotate_room(self, task):
        angle_degrees_per_second = 10
        dt = globalClock.get_dt()
        angle_degrees = angle_degrees_per_second * dt
        self.room.set_h(self.room.get_h() + angle_degrees)
        return task.cont

    def rotate_dice(self, task):
        rotation_speed = LVector3f(0.2, 0.3, 0.1)  # Adjust the rotation speeds as desired
        dt = globalClock.get_dt()
        angles = rotation_speed * dt * 10  # Multiply by a factor to control rotation speed
        self.dice.set_hpr(self.dice.get_hpr() + angles)

        # Update camera roll
        self.roll_angle += self.roll_frequency * dt
        roll_offset = self.roll_amplitude * math.sin(self.roll_angle + self.roll_phase_offset)
        self.cam.set_r(roll_offset)

        return task.cont

    @staticmethod
    def get_random_shaders(directory):
        vertex_files = MyGame.get_files_with_extension(directory, ".vert.glsl")
        fragment_files = MyGame.get_files_with_extension(directory, ".frag.glsl")

        vertex_shader = random.choice(vertex_files) if vertex_files else None
        fragment_shader = random.choice(fragment_files) if fragment_files else None

        return vertex_shader, fragment_shader

    @staticmethod
    def get_files_with_extension(directory, extension):
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_list.append(os.path.join(root, file))
        return file_list

    @staticmethod
    def get_random_file(directory, extension):
        files = MyGame.get_files_with_extension(directory, extension)
        return random.choice(files) if files else None


game = MyGame()
game.run()
