basic.show_icon(IconNames.HAPPY)

def on_forever():
    if mbit_小车类.Line_Sensor(mbit_小车类.enPos.LEFT_STATE, mbit_小车类.enLineState.WHITE) and mbit_小车类.Line_Sensor(mbit_小车类.enPos.RIGHT_STATE, mbit_小车类.enLineState.WHITE):
        mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_RUN, 60)
    elif mbit_小车类.Line_Sensor(mbit_小车类.enPos.LEFT_STATE, mbit_小车类.enLineState.WHITE) and mbit_小车类.Line_Sensor(mbit_小车类.enPos.RIGHT_STATE, mbit_小车类.enLineState.BLACK):
        mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_SPINRIGHT, 70)
    elif mbit_小车类.Line_Sensor(mbit_小车类.enPos.LEFT_STATE, mbit_小车类.enLineState.BLACK) and mbit_小车类.Line_Sensor(mbit_小车类.enPos.RIGHT_STATE, mbit_小车类.enLineState.WHITE):
        mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_SPINLEFT, 70)
    else:
        mbit_小车类.car_ctrl(mbit_小车类.CarState.CAR_STOP)
basic.forever(on_forever)
