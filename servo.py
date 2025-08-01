import requests
import time
import math

ESP_IP = "http://192.168.0.145"  # IP ESP

# Nazwy serw
LL = "left_leg"
LF = "left_foot"
RL = "right_leg"
RF = "right_foot"

# Pozycje neutralne
LLN = 70
LFN = 92
RLN = 113
RFN = 92

# Słownik pozycji neutralnych
neutral_pos = {
    LL: LLN,
    LF: LFN,
    RL: RLN,
    RF: RFN,
}

# Śledzenie pozycji
current_pos = {
    LL: LLN,
    LF: LFN,
    RL: RLN,
    RF: RFN,
}

def set_servo(nazwa, kat):
    r = requests.get(f"{ESP_IP}/servo", params={"name": nazwa, "pos": kat})
    if r.status_code == 200:
        current_pos[nazwa] = kat
    else:
        print("Error:", r.status_code, r.text)

def move_servo(servos, ends, steps=10, delay_time=0.001):
    starts = [current_pos[servo] for servo in servos]
    diffs = [end - start for start, end in zip(starts, ends)]
    for i in range(steps + 1):
        t = i / steps  
        for idx, servo in enumerate(servos):
            pos = starts[idx] + int(diffs[idx] * t)
            set_servo(servo, pos)
        time.sleep(delay_time)
    for idx, servo in enumerate(servos):
        current_pos[servo] = ends[idx]

def return_to_neutral(servos, steps=10, delay_time=0.001):
    ends = [neutral_pos[servo] for servo in servos]
    move_servo(servos, ends, steps, delay_time)

def stop_swing():
    set_servo(LF, 92)
    set_servo(RF, 92)
    return_to_neutral([LL, RL])

def left_swing():
    move_servo([LL, RL], [105, 180])
    time.sleep(0.2)
    set_servo(LF, 90 + 25)
    time.sleep(0.5)

def right_swing():
    move_servo([LL, RL], [5, 85])
    time.sleep(0.2)
    set_servo(RF, 90 - 20)
    time.sleep(0.5)

def left_walk():
    move_servo([LL, RL], [105, 180])
    time.sleep(0.2)
    set_servo(LF, 90 + 15)
    time.sleep(0.7)
    stop_swing()

def right_walk():
    move_servo([LL, RL], [5, 85])
    time.sleep(0.2)
    set_servo(RF, 90 - 10)
    time.sleep(0.7)
    stop_swing()


# while True:
#     left_walk()
#     time.sleep(0.5)
#     right_walk()
#     time.sleep(0.5)