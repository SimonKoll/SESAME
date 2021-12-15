import RPi.GPIO as GPIO
import time

servoPIN = 17  # der Servomotor wurde an den GPIO Pin 18 angeschlossen
# moegliche Servopositionen fuer dieses Beispiel
servoPositions = [2, 5,10]

# Funktion zum setzen eines Winkels
# als Parameter wird die Position erwartet


def setServoCycle(p, position):
    p.ChangeDutyCycle(position)
    # eine Pause von 0,5 Sekunden
    time.sleep(1)

# versuche
try:
    # damit wir den GPIO Pin ueber die Nummer referenzieren koennen
    GPIO.setmode(GPIO.BCM)
    # setzen des GPIO Pins als Ausgang
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO als PWM mit 50Hz
    # Initialisierung mit dem ersten Wert aus unserer Liste
    p.start(servoPositions[0])
    # fuer jeden Wert in der Liste, mache...
    for pos in servoPositions:
        # setzen der Servopostion
        setServoCycle(p, pos)
        print(pos)

# wenn das Script auf dem Terminal / der Konsole abgebrochen wird, dann...
except KeyboardInterrupt:
    p.stop()
    # alle Pins zuruecksetzen
    GPIO.cleanup()

finally:
    p.stop()
    GPIO.cleanup()
