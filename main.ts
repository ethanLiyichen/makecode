basic.showIcon(IconNames.Happy)
basic.forever(function on_forever() {
    if (mbit_小车类.Line_Sensor(mbit_小车类.enPos.LeftState, mbit_小车类.enLineState.White) && mbit_小车类.Line_Sensor(mbit_小车类.enPos.RightState, mbit_小车类.enLineState.White)) {
        mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_Run, 60)
    } else if (mbit_小车类.Line_Sensor(mbit_小车类.enPos.LeftState, mbit_小车类.enLineState.White) && mbit_小车类.Line_Sensor(mbit_小车类.enPos.RightState, mbit_小车类.enLineState.Black)) {
        mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_SpinRight, 70)
    } else if (mbit_小车类.Line_Sensor(mbit_小车类.enPos.LeftState, mbit_小车类.enLineState.Black) && mbit_小车类.Line_Sensor(mbit_小车类.enPos.RightState, mbit_小车类.enLineState.White)) {
        mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_SpinLeft, 70)
    } else {
        mbit_小车类.CarCtrl(mbit_小车类.CarState.Car_Stop)
    }
    
})
