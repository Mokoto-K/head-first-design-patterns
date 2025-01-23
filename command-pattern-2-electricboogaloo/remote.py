from command import Command 

class Remote:
    
    def __init__(self):
        self.oncommand = []
        self.offcommand = []
         
        no_command = Command
        for i in range(7):
            self.oncommand.append(no_command)
            self.offcommand.append(no_command) 
        
    
    def set_command(self, slot, on_command, off_command):
        self.oncommand[slot] = on_command
        self.offcommand[slot] = off_command


    def on_button_pushed(self, slot):
        self.oncommand[slot].execute()


    def off_button_pushed(self, slot):
        self.offcommand[slot].execute()


    def __str__(self) -> str:
        output = f"\n-----Remote Control-----\n"

        for i in range(len(self.oncommand)):
            output = f"{output} [slot {i}] {self.oncommand[i].__class__.__name__}    {self.offcommand[i].__class__.__name__}\n" 

        return output 

