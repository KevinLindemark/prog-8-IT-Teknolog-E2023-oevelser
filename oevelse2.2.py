from machine import Pin, ADC
from time import sleep, ticks_ms

"""
prog #8 E2023 - øvelse 2.2
Prøv at lave en klasse til at blinke LED’er med non-blocking delays med ticks_ms.
Klasen skal tage et Pin objekt som 1. argument og perioden i millisekunder der skal blinkes med som 2. argument.
"""

class LMT84:
    """
    LMT84 class to return temperature, celsius, fahrenheit and kelvin
    """
    def __init__(self, pin_number=35, attenuation=2, alpha = -4.8, beta = 1034, average = 128):
        self.adc = ADC(Pin(pin_number))
        self.adc.atten(attenuation)
        self.alpha = alpha
        self.beta = beta
        self.average = average
        self.ADC_mV = 2048.0 / 4095.0
    
    def millivolts(self):
        return self.adc_average() * self.ADC_mV
    
    def adc_average(self):        
        ADC_value = 0
        if self.average > 1:
            for i in range(self.average):
                ADC_value += self.adc.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.adc.read()
            sleep(1)
        return ADC_value

    def celsius_temperature(self):
        return (self.millivolts() - self.beta) / self.alpha
    
    def fahrenheit_temperature(self):
        return (self.celsius_temperature() * 1.8) + 32
    
    def kelvin_temperature(self):
        return self.celsius_temperature() + 273.15

lmt84 = LMT84()
print(lmt84.celsius_temperature())
print(lmt84.fahrenheit_temperature())
print(lmt84.kelvin_temperature())