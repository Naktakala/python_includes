# python_includes
Basic tutorial and reference for python scripts/modules in different directories.

## 1 Synopsis

Suppose your name is Jean and you have a python script `Test1.py` in a folder associated with you as a user (i.e. `.../Users/Jean/PythonScripts/Test1.py`). Now also suppose you have a library of python scripts called `JeanPythonLib` in some other folder.

```
/Drive
  -PythonModules/
    -JeanPythonLib/
  -Users/
    -Jean/
      -PythonScripts/
        Test1.py
    -Marv/
```

How would you use your library?

## 2 Requirements on python scripts needing the library

All scripts needing a library needs to add the following to the top of the script:

```python
import sys
import os 

def CheckModules():
    envar_name = "MY_PYTHON_MODULES"
    my_modules = os.getenv(envar_name)
    if my_modules == None: sys.exit(envar_name + " env var undefined!")
    else: sys.path.append(my_modules)

CheckModules()
```

Hereafter you can import your library and have access to the items within it. For example:

```python
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
```

## 3 Requirements on python libraries

The folder that contains your library equipment needs to have the equivalent of a C++ header file. This is called the init-file and literally has to be named `__init__.py`.

```
/Drive
  -PythonModules/
    -JeanPythonLib/
      __init__.py           <------ You have to have this file
  -Users/
    -Jean/
      -PythonScripts/
        Test1.py
    -Marv/
```

The contents of this file might look like this:

```python
""" This is Jean's library """
def SayHello():
    print("Happy Hello")
```

Here the function `SayHello` is available in the calling script as `JeanPythonLib.SayHello()`.

### 3.1 Adding a single-file object-class to your library
Let's suppose we wanted to add a python `class` to the library and call it `CarClass`, and we want to tuck it into its own neat little file called `class_car.py`.

```
/Drive
  -PythonModules/
    -JeanPythonLib/
      __init__.py           
      class_car.py              <------ Create the car class in this file
  -Users/
    -Jean/
      -PythonScripts/
        Test1.py
    -Marv/
```

In this case `class_car.py` would look like this:

```python
""" This is car class """

class CarClass:
    def __init__(self) -> None:
        """ Constructor with no arguments """
        self.type : str = "Happy"

    def Type(self) -> str:
        return self.type
```

And we use this class as shown in `Test2.py`:

```python
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
```

### 3.2 Adding a multi-file class to your library
Sometimes the methods of an object-class can get really hairy, prompting us to split them amongst multiple files. Let's see how this is done on the hand of `TigerClass`.

First we create the folder `class_tiger` and an `__init__.py` within it:

```
/Drive
  -PythonModules/
    -JeanPythonLib/
      class_tiger/
        __init__.py
      __init__.py           
      class_car.py              
  -Users/
    -Jean/
      -PythonScripts/
        Test1.py
    -Marv/
```

```python
""" Class definition for a tiger object """

from . import m_01_roar
from . import m_02_purr

class TigerClass:
    def __init__(self) -> None:
        self.x : int = 1
        self.y : int = 3

    from .m_01_roar import Roar
    from .m_02_purr import Purr
```

Then we create two method-containing files `m_01_roar.py` and `m_02_purr.py`.

```
/Drive
  -PythonModules/
    -JeanPythonLib/
      class_tiger/
        __init__.py
        m_01_roar.py
        m_02_purr.py
      __init__.py           
      class_car.py              
  -Users/
    -Jean/
      -PythonScripts/
        Test1.py
    -Marv/
```

`m_01_roar.py` looks like this

```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import TigerClass

def Roar(self: "TigerClass") -> None:
    print("RAAAWWWRRRR!!!", self.x)
```

and `m_02_purr.py` looks like this

```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import TigerClass

def Purr(self: "TigerClass") -> None:
    print("MMMM PRRRRRRRRR")
```

These methods used the `typing` module to allow their `self`-arguments to be typed. This allows autocomplete to function well.

## Making VSCode autocomplete your library
In my VSCode I use the PyLance-extension as the autocomplete or linter and I just adjusted the setttings by adding the library path to Python>Analysis>Extra Paths.
