
class Power:
    def connect_device_to_power_outlet(self, device):
        pass


class HDMI:
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class RCA:
    def connect_to_device_via_rca_cable(self, device):
        pass


class Eth:
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class Television(Power, HDMI, RCA):

    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)


class DVDPlayer(Power, RCA):

    def connect_to_device_via_rca_cable(self, television):
        self.connect_to_device_via_rca_cable(television)


class GameConsole(Power, Eth, HDMI):

    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)


class Router(Power, Eth):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)


tv = Television()
dvd = DVDPlayer()
game_console = GameConsole()
router = Router()

tv.connect_to_dvd(dvd)
game_console.connect_to_tv(tv)

router.connect_to_game_console(game_console)
router.connect_to_device_via_ethernet_cable(tv)
