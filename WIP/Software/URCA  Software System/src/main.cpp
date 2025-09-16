#include <Arduino.h>
#include <ESC.h>

ESC ESCmanager(5); // set to pin 5

void setup() {
    ESCmanager.startup(); // Attaches to pin 5 
    ESCmanager.idle(); // Good to start the motor, might have to check if it's written correctly
}

void loop() {

}