from typing import Dict
import network
from model.esp_wifi import EspWifi

class WifiService():
    def __init__(self, esp_wifi : EspWifi = None) -> None:
        self.esp_wifi = esp_wifi
        self.wifi_list = self.listar_redes()

    def esta_ativo(self):
        return self.esp_wifi.wlan_sta.active()

    def ligar_sensor(self):
        if not self.esta_ativo():
            print('Ativando sensor de rede...')
            self.esp_wifi.wlan_sta.active(True)
            print('Sensor de rede ativado')
        else:
            print('Sensor de rede já está ativado...')
    
    def desligar_sensor(self):
        if self.esta_ativo():
            print('Desativando sensor de rede...')
            self.esp_wifi.wlan_sta.active(True)
            print('Sensor de rede desativado')
        else:
            print('Sensor de rede já está desativado...')

    def esta_conectado(self):
        return self.esp_wifi.wlan_sta.isconnected()

    def conectar(self, ssid : str = None, senha : str = None):
        if not self.esta_ativo():
            self.ligar_sensor()

        for wifi in self.wifis:
            if ssid == wifi.ssid:
                break

        try:
            resposta, texto = wifi.conectar_wifi(ssid, senha)
            if resposta:
                self.relogio.reinciar_relogio()
            return resposta, texto
            

        except Exception as e:
            print(e)

    def desconectar():
        pass 

    def listar_redes(self):
        networks = self.esp_wifi.wlan_sta.scan()
        network_wifi = []
        for ssid in sorted(networks, key=lambda x: x[0]):
            network_wifi.append(ssid)
        if len(network_wifi) == 0:
            network_wifi.append("Nenhuma rede wifi encontrada")
        return network_wifi
            
    def status(self):
        print("WIfi connection status: ", (self.esp_wifi.wlan_sta.status()))
        print('network config:', self.esp_wifi.wlan_sta.ifconfig())

