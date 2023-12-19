from Tire.tire import tire
import array as arr

class OctoprimeTire(Tire):
    def __init__(self, tArray):
        self.tArray = tArray

    def needs_service(self):
        if arr.tArray[0] + arr.tArray[1] +arr.tArray[0] + arr.tArray[1] >= 3:
            return True
        else:
            return False