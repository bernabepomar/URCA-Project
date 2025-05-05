#ifndef EVENTS_H
#define EVENTS_H

#include <Arduino.h>
#include <ESC.h>


class EVENTS{
    public:
        EVENTS(bool* LaunchState, bool* ServoTestState, bool* ESCTestState,ESC& esc);

        void getLaunch();
        void getServoTest();
        void getESCTest();
        ESC& _esc;
    private:
    bool** LaunchState, bool** ServoTestState, bool** ESCTestState,ESC& esc
};

#endif