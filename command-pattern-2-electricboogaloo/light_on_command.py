from command import Command

class Light_on_command(Command):

    def __init__(self, light):
        self.light = light


    def execute(self):
        self.light.on()
    
