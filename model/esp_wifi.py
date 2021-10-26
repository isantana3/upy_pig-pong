import network

class EspWifi():
    def __init__(self) -> None:
        self.wlan_ap = network.WLAN(network.AP_IF)
        self.wlan_sta = network.WLAN(network.STA_IF)