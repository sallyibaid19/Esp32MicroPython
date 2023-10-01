import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
sw = machine.Pin(0, machine.Pin.IN)

def handle_interrupt(pin):
    led.value(not led.value())
    
sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)    