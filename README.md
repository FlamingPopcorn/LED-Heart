# LED-Heart
Use a pi Pico to create a piece of art

# CAD Model
[https://cad.onshape.com/documents/b84acc120d7ee278d5ee1cb3/w/0e59b9b7844e1c5d8672f046/e/7aa8eaa917d771051b3fc39d?renderMode=0&uiState=664d506d8b1fa376254f5ebb](url)

# Wiring
- A 5V power supply should be wired to the VBUS and GND pins and the 5V and GND pins on the LED strip
- Wire the LED strip's DIO in pin to GPIO 28 on the pico

# Flashing the pi pico
1. Install micropython onto your pico with the latest official release
2. Upload the two files to your pico with an IDE like thonny or vsCode with the MicroPico Extension
3. Unplug the pico and power it again. It should be running the program
