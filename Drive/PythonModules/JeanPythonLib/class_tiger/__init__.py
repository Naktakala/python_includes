""" Class definition for a tiger object """

from . import m_01_roar
from . import m_02_purr

class TigerClass:
    def __init__(self) -> None:
        self.x : int = 1
        self.y : int = 3

    from .m_01_roar import Roar
    from .m_02_purr import Purr