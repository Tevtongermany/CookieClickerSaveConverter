import datetime
from .ccmobilebuildings import *

class CCSaveMobileSettings:
    def __init__(self,data:dict) -> None:
        self._fancy = bool(data.get("fancy", 0))
        self._particles = bool(data.get("particles", 0))
        self._cookiepops = bool(data.get("cookiepops", 0))
        self._cookiewobble = bool(data.get("cookiewobble", 0))
        self._lowMotion = bool(data.get("lowMotion", 0))
        self._cursors = bool(data.get("cursors", 0))
        self._diagnostic = bool(data.get("diagnostic", 0))
        self._debug = bool(data.get("debug", 0))
        self._sound = bool(data.get("sound", 0))
        self._pan = bool(data.get("pan", 0))
        self._dislodge = bool(data.get("dislodge", 0))
        self._shadows = bool(data.get("shadows", 0))
        self._milk = bool(data.get("milk", 0))
        self._notScary = bool(data.get("notScary", 0))
    # Way too lazy to write allat 😭🙏
    @property
    def fancy(self):
        return self._fancy

    @property
    def particles(self):
        return self._particles

    @property
    def cookiepops(self):
        return self._cookiepops

    @property
    def cookiewobble(self):
        return self._cookiewobble

    @property
    def lowMotion(self):
        return self._lowMotion

    @property
    def cursors(self):
        return self._cursors

    @property
    def diagnostic(self):
        return self._diagnostic

    @property
    def debug(self):
        return self._debug

    @property
    def sound(self):
        return self._sound

    @property
    def pan(self):
        return self._pan

    @property
    def dislodge(self):
        return self._dislodge

    @property
    def shadows(self):
        return self._shadows

    @property
    def milk(self):
        return self._milk

    @property
    def notScary(self):
        return self._notScary

class CCSaveMobileBuildings:
    def __init__(self,data:dict) -> None:
        self.cursor = Cursor(data.get("Cursor"))
        self.grandma = Grandma(data.get("Grandma"))
        self.farm = Farm(data.get("Farm"))
        self.mine = Mine(data.get("Mine"))
        self.factory = Factory(data.get("Factory"))
        self.bank = Bank(data.get("Bank"))
        self.temple = Temple(data.get("Temple"))
        self.wizard_tower = WizardTower(data.get("Wizard tower"))
        self.shipment = Shipment(data.get("Shipment"))
        self.alchemy_lab = AlchemyLab(data.get("Alchemy lab"))
        self.portal = Portal(data.get("Portal"))
        self.time_machine = TimeMachine(data.get("Time machine"))
        self.antimatter_condenser = AntimatterCondenser(data.get("Antimatter condenser"))
        self.prism = Prism(data.get("Prism"))
        self.chancemaker = Chancemaker(data.get("Chancemaker"))
        self.fractal_engine = FractalEngine(data.get("Fractal engine"))
        self.javascript_console = JavascriptConsole(data.get("Javascript console"))
        self.idleverse = Idleverse(data.get("Idleverse"))
        self.cortex_baker = CortexBaker(data.get("Cortex baker"))
        self.you = You(data.get("You"))
        
        


class CCSaveMobile:
    def __init__(self,data:dict) -> None:
        self.raw = data
        self.time = data.get("time")
        self.settings = data.get("settings")
        self.runstarted = data.get("runStart")
        self.gamestarted = data.get("gameStart")
        self.seed = data.get("seed")
        self.currentcookies = data.get("cookies")
        self.earnedcookies = data.get("cookiesEarned")
        self.totalcookies = data.get("cookiesTotal")
        self.handmadecookies = data.get("cookiesHandmade")
        self.cookieclicks = data.get("cookieClicks")
        self.buildings = data.get("buildings")

    def _milliseconds_to_seconds(self, timestamp):
        if isinstance(timestamp, (int, float)) and timestamp > 1_000_000_000:
            return timestamp / 1000.0
        return timestamp
    

    @property
    def get_settings(self) -> CCSaveMobileSettings:
        """Gets settings"""
        return CCSaveMobileSettings(self.settings)
    
    # timestamps and all that stuff
    @property
    def get_time(self) -> datetime.datetime:
        """Gets the last time the player logged in"""
        time = self._milliseconds_to_seconds(self.time)
        return datetime.datetime.fromtimestamp(time)
    
    @property
    def get_run_started(self) -> datetime.datetime:
        """Gets the time when the run started"""
        runStartTime = self._milliseconds_to_seconds(self.runstarted)
        return datetime.datetime.fromtimestamp(runStartTime)

    @property
    def get_game_started(self) -> datetime.datetime:
        """Gets the time when the user started the game for the first time"""
        gameStartTime = self._milliseconds_to_seconds(self.gamestarted)
        return datetime.datetime.fromtimestamp(gameStartTime)
    # ze seed

    @property
    def get_seed(self) -> str:
        return self.seed
    
    # Cookies
    @property
    def get_cookies(self) -> float:
        """Gets the current cookie amount that the player has"""
        return self.currentcookies
    
    @property
    def get_total_cookies(self) -> float:
        """Gets all total backed cookies"""
        return self.totalcookies
    
    @property
    def get_earned_cookies(self) -> float:
        """Tbh I have no idea what this is lol"""
        return self.earnedcookies
    
    @property
    def get_clicked_cookies(self) -> int:
        """Gets how much the player clicked the cookie"""
        return self.cookieclicks

    @property
    def get_buildings(self) -> CCSaveMobileBuildings:
        return CCSaveMobileBuildings(data=self.buildings)


