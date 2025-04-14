#ifndef SERVOSM_H
#define SERVOSM_H

#include <Arduino.h>
#include <PWMServo.h>

class Servosm {
    public:
        Servosm();
        
    private:
        PWMServo** _servos;
        int _servoCount;
};    

#endif