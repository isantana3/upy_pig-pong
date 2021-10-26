import uasyncio
from machine import Pin, PWM
from service.wifi_service import WifiService

class PingPong():
    def __init__(self) -> None:
        self.p = Pin(2, Pin.OUT)
        self.buzzer = PWM(Pin(14), freq=440, duty=512)
        self.pisca = False

    def led_on(self) -> None:
        '''
            Liga o segundo pino de led
        '''
        self.p.on()

    def Led_off(self) -> None:
        '''
            Desliga o segundo pino de led
        '''
        self.p.off()

    async def led_pisca(self, intervalo : float = 0.1) -> None:
        '''
            Faz o segundo pino de led piscar
        '''
        self.pisca = True
        while self.pisca:
            self.on()
            uasyncio.sleep(intervalo)
            self.off()
            uasyncio.sleep(intervalo)

    async def led_para_pisca(self) -> None:
        '''
            Faz o segundo pino de led parar de piscar
        '''
        self.pisca = False
        
    def buzzer_play():
        pass