from enum import Enum

class LightState(Enum):
    off='Off'
    on='On'



class LightSwitch:
    def __init__(self):
        self.init_state=LightState.off
    def toggle(self):
        if self.init_state==LightState.off:
            self.init_state=LightState.on
        else:
            self.init_state=LightState.off
    def __str__(self):
        return f"Light is {self.init_state.value}"
    

bulb=LightSwitch()
print(bulb)
bulb.toggle()
print(bulb)