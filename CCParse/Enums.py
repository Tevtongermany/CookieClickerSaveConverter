from enum import Enum, auto


class SaveType(Enum):
    MOBILE = auto()
    PC = auto()
    AUTODETECT = auto()

class UpgradeAvailability(Enum):
    NOTAVAILABLE = auto()
    AVAILABLE = auto()
    BOUGHT = auto()