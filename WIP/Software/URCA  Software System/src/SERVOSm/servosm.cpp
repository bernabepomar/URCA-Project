#include "servosm.h"

Servosm::Servosm(PWMServo *servos[], int servoCount)
    : _servos(servos), _servoCount(servoCount) {}