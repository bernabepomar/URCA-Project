#include "events.h"
    
EVENTS::EVENTS(bool *LaunchState, bool *ServoTestState, bool *ESCTestState, ESC &esc)
    : _LaunchState(LauncState),_ServoTestState(ServoTestState), _ESCTestState(ESCTestState), _esc(esc) {}

void EVENTS::getLaunch()
{
}
void EVENTS::getServoTest(){

}

void EVENTS::getESCTest(){
    if ESCTestState==true
        for (float i = 0; i <= 100; i += 10) {
            _esc.setThrottle(i);
            delay(100);
        }

        for (float i = 100; i >= 0; i -= 10) {
            _esc.setThrottle(i);
            delay(100);
        }

}