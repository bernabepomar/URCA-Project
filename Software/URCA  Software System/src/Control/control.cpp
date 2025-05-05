#include "control.h"

CONTROL::CONTROL(uint8_t PWMPin, uint16_t minPulse, uint16_t maxPulse,PWMServo *servos[], uint8_t servoCount)
    : _PWMPin(PWMPin), _minPulse(minPulse), _maxPulse(maxPulse), _servos(servos), _servoCount(servoCount) {}

void CONTROL::startup(){
    _servo.attach(_PWMPin); // Activating correct pin
}

void CONTROL::setThrottle(){
    percent= constrain(percent, 0.0f, 100.0f);
    uint16_t pulse = _minPulse + (_maxPulse - _minPulse) * (percent / 100.0f); // Defining the throttle responde based on the float
    _servo.writeMicroseconds(pulse);
}

void CONTROL::idle(){
    _servo.WriteMicroseconds(0); // Set to 0 for idling
}

void CONTROL::arming(){
    _servo.WriteMicroseconds(_minPulse); // Set to minimum value for arming
    delay(2000); // Let it be for 2 seconds to ensure arming
}


