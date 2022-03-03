import sys
import os 

def CheckModules():
    envar_name = "MY_PYTHON_MODULES"
    my_modules = os.getenv(envar_name)
    if my_modules == None: sys.exit(envar_name + " env var undefined!")
    else: sys.path.append(my_modules)

CheckModules()

import JeanPythonLib

import numpy as np

A = np.matrix([[1, 2],[3,4]],dtype=float)

print(A)
JeanPythonLib.SayHello()
car = JeanPythonLib.CarClass()

print(car.Type())