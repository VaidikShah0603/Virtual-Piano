import serial
import pygame
import time

arduino = serial.Serial('COM5',baudrate=9600, timeout=0.01) 
time.sleep(2)

pygame.mixer.init()


notes = {
    "sa": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\sa.wav"),
    "re": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\re.wav"),
    "ga": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\ga.wav"),
    "ma": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\ma.wav"),
    "pa": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\pa.wav"),
    "dha": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\dha.wav"),
    "ni": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\ni.wav"),
    "sa_high": pygame.mixer.Sound(r"C:\Users\Aryan jain\Downloads\sa_high.wav")
}

def play_note(distance):
    if 5 <= distance < 10:
        notes["sa"].play()
    elif 10 <= distance < 15:
        notes["re"].play()
    elif 15 <= distance < 20:
        notes["ga"].play()
    elif 20 <= distance < 25:
        notes["ma"].play()
    elif 25 <= distance < 30:
        notes["pa"].play()
    elif 30 <= distance < 35:
        notes["dha"].play()
    elif 35 <= distance < 40:
        notes["ni"].play()
    elif 40 <= distance < 45:
        notes["sa_high"].play()

try:
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()
            distance = float(data)
            print(f"Distance: {distance} cm")
            play_note(distance)
            time.sleep(0.05)
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    arduino.close()
