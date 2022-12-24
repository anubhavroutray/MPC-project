import numpy as np
import matplotlib.pyplot as plt
import secondary_file as sf
import matplotlib.gridspec as gridspec


support = sf.support_files()
constants = support.constants
#print(constants)

# Loading the constants in this file
Ts = constants[6]
#print(Ts)
outputs = constants[10]
hz = constants[11]
x_dot = constants[12]
time_length = constants[17]
print(time_length)