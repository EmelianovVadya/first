import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac_bits=[16,20,21,25,26,17,27,22]
for pin in dac_bits:
    GPIO.setup(dac_bits,GPIO.OUT)
dynamic_range = 3.13

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(value):
   return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            numder = voltage_to_number(voltage)
            predstav = number_to_dac(numder)
            print(f"Число на вход ЦАП:{numder}, биты:{predstav}")
            GPIO.output(dac_bits,predstav)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()