import numpy as np
import matplotlib.pyplot as plt 

class support_files:
    "For interracting with the primary file"

    def __init__(self) -> None:
        "Adding the constants"

        g = 9.81
        m = 1500
        I = 3000        #Mass moment of inertia
        cor_f = 19000   #Front wheel cornering stiffness
        cor_r = 30000   #Rear wheel cornering stiffness
        lf = 2          #Distance of front axle from CM
        rf = 3          #Distance of rear axle from CM
        Ts = 0.01



        # Matrix weights for the cost function
        Q = np.matrix('100 0;0 1')  #Weight for O/P
        #print(Q)
        S = np.matrix('100 0;0 1')  #Weigh for final horizon period O/P
        R = np.matrix('100')        #Weight for input (only 1 in this case)
        #print(R)

        outputs = 2                 #No of outputs
        hz = 30                     #Horizon period
        x_dot = 15                  #Longitudinal velocity
        lane_width = 5              # in [m]
        lane_nos = 5                # in [m]

        ## Trjectory - Eq- y= r*sin(2pi*f*t)
        r = 4                       #amplitude for sinusoidal functions
        f = 0.01                    #frequncy(small means flat)
        TL = 12                   # in [s] - duration for maneouver

        trajectory = 1 #choose between 1 and 2

        ## This array stores all the above constants and can be called easily at other locations.
        self.constants = [m, I, cor_f, cor_r, lf, rf, Ts, Q, S, R, outputs, hz,
        x_dot, lane_width, lane_nos, r, f, TL, trajectory]

        return None




        