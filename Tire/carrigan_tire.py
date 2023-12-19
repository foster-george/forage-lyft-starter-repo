from Tire.tire import tire
import array as arr

class CarriganTire(Tire):
    def __init__(self, tArray):
        self.tArray = tArray

    def needs_service(self):
        for x in tArray:
            if x >= 0.9: 
                return True

        return False