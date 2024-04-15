import RPi.GPIO as GPIO
import time

# Constants for the GPIO mode and pin setup
GPIO_MODE = GPIO.BCM
ROW_PINS = [2, 3, 4, 17, 24, 22, 10, 18]
COLUMN_PINS = [25, 5, 6, 13, 8, 26, 27, 9]

# Setup GPIO pins
def initialize_gpio():
    GPIO.setmode(GPIO_MODE)
    for pin in ROW_PINS + COLUMN_PINS:
        GPIO.setup(pin, GPIO.OUT)

# Clear the LED matrix
def reset_matrix():
    for row_pin in ROW_PINS:
        GPIO.output(row_pin, GPIO.LOW)
    for col_pin in COLUMN_PINS:
        GPIO.output(col_pin, GPIO.HIGH)

# Function to display letters sequentially
def display_character(pattern):
    for row_index in range(8):
        reset_matrix()
        GPIO.output(ROW_PINS[row_index], GPIO.HIGH)
        
        for col_index in range(8):
            if pattern[row_index] & (1 << (7 - col_index)):
                GPIO.output(COLUMN_PINS[col_index], GPIO.LOW)
            else:
                GPIO.output(COLUMN_PINS[col_index], GPIO.HIGH)
        
        time.sleep(0.001)

# Define patterns for different characters
CHARACTER_A = [
    0b00111100,
    0b00111100,
    0b01100110,
    0b01100110,
    0b01111110,
    0b01100110,
    0b01100110,
    0b00000000,
]

CHARACTER_B = [
    0b01111000,
    0b01111110,
    0b01100110,
    0b01111000,
    0b01111000,
    0b01100110,
    0b01111110,
    0b01111000,
]

def main():
    initialize_gpio()
    try:
        while True:
            for _ in range(200):
                display_character(CHARACTER_A)
            for _ in range(200):
                display_character(CHARACTER_B)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
