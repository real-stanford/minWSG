from wsg import WSG
import numpy as np
from time import sleep

if __name__ == "__main__":
    wsg = WSG()
    wsg.home()
    for position in np.arange(110, 0, -10):
        wsg.move(position)
    wsg.home()
    input("Place an objet between wsg fingers and press enter ...")
    wsg.grip(40)
    sleep(5)
    wsg.release()
    