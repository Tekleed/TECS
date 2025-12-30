import time

import ECS
from ECS import Systems

def Update(Delta: float):
    Systems.Update(Delta)

def Void():

    FPS = 60
    Delta = 1 / FPS
    Last = time.perf_counter()
    Running = True

    while Running:

        Stamp = time.perf_counter()
        Elapsed = Stamp - Last
        Last = Stamp

        Update(Elapsed)

        

