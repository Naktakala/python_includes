from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import TigerClass

def Roar(self: "TigerClass") -> None:
    print("RAAAWWWRRRR!!!", self.x)