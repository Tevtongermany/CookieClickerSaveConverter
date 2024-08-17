import datetime

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

class CCSaveMobile:
    def __init__(self,data:dict) -> None:
        self.raw = data
        self.time = data.get("time")
        self.settings = data.get("settings")
        self.runstarted = data.get("runStart")
        self.gamestarted = data.get("gameStart")
        self.seed = data.get("seed")
        self.currentcookies = data.get("cookies")

    def _milliseconds_to_seconds(self, timestamp):
        if isinstance(timestamp, (int, float)) and timestamp > 1_000_000_000:
            return timestamp / 1000.0
        return timestamp
    
    @property
    def get_time(self) -> datetime.datetime:
        """Gets the last time the player logged in"""
        time = self._milliseconds_to_seconds(self.time)
        return datetime.datetime.fromtimestamp(time)
    
    @property
    def get_settings(self) -> CCSaveMobileSettings:
        """Gets settings"""
        return CCSaveMobileSettings(self.settings)

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

    @property
    def get_seed(self) -> str:
        return self.seed
    
