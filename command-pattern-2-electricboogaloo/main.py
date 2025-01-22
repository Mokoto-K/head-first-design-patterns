from simple_remote_control import Simple_Remote_control
from light import Light
from light_on_command import Light_on_command

remote = Simple_Remote_control()
light = Light()
lighton = Light_on_command(light)

remote.set_command(lighton)
remote.button_was_pressed()
