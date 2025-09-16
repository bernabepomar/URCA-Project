#ifndef CONTROL_H
#define CONTROL_H

#include <Arduino.h>
#include <PWMServo.h>

class ESC{
    public:
    ESC(uint8_t PWMPin, uint16_t minPulse = 1000, uint16_t maxPulse = 2000, PWMServo* servos[], uint8_t servoCount); // Set the In variables as the corresponding pin, and max and min pulse of the ESC
    // The pulses may be later set to a standard value

    void startup();
    void setThrottle(float percent); // 0.0 to 100.0 in floating point for the throttle
    void idle(); // Idle the motor with value 0
    void arming(); // Needed for certain ESCs and it looks cool
    
private:
    uint8_t _PWMPin;
    uint16_t _minPulse;
    uint16_t _maxPulse;
    PWMServo** _servos;
    uint8_t _servoCount;
};

#endif