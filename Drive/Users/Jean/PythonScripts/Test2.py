import sys
import os 

def CheckModules():
    envar_name = "MY_PYTHON_MODULES"
    my_modules = os.getenv(envar_name)
    if my_modules == None: sys.exit(envar_name + " env var undefined!")
    else: sys.path.append(my_modules)

CheckModules()

import JeanPythonLib

car = JeanPythonLib.CarClass()

print(car.Type())