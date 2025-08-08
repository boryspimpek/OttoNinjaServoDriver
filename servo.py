import socket
import time
import random

UDP_IP = "10.0.0.100"  # Adres IP ESP8266
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

LL = "LL"  # Left Leg 
LF = "LF"  # Left Foot
RL = "RL"  # Right Leg
RF = "RF"  # Right Foot

LLN = 70    
LFN = 90    
RLN = 113   
RFN = 90    

neutral_pos = {
    LL: (LLN, 'a'),
    LF: (LFN, 's'),
    RL: (RLN, 'a'),
    RF: (RFN, 's')
}

current_pos = {
    LL: LLN,
    LF: LFN,
    RL: RLN,
    RF: RFN
}

def move_servo(servos_angles):
    command_parts = []
    
    for servo, value in servos_angles.items():
        if isinstance(value, tuple):
            angle_speed, value_type = value
            command_parts.append(f"{servo}:{angle_speed}{value_type}")
        else:
            value_type = 's' if servo in ['LF', 'RF'] else 'a'
            command_parts.append(f"{servo}:{value}{value_type}")
            if value_type == 'a':
                current_pos[servo] = value
            else:
                current_pos[servo] = value  
    
    command = ",".join(command_parts)
    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
    print(f"Wysłano komendę: {command}")

def set_speed(servo, speed):
    """Ustawia prędkość serwa ciągłego (0-180)"""
    assert servo in ['LF', 'RF'], "Tylko LF i RF są serwami ciągłymi"
    assert 0 <= speed <= 180, "Prędkość musi być między 0 a 180"
    move_servo({servo: (speed, 's')})
    current_pos[servo] = speed

def return_to_neutral():
    move_servo({
        LL: (LLN, 'a'),  
        LF: (LFN, 's'),  
        RL: (RLN, 'a'),  
        RF: (RFN, 's')   
    })
    
    global current_pos
    current_pos = {
        LL: LLN,
        LF: LFN,
        RL: RLN,
        RF: RFN
    }

def walk():
    for i in range(4):
        left_walk_forward()
        time.sleep(0.1)
        right_walk_forward()
        time.sleep(0.1)
    return_to_neutral()
    
def left_swing():
    move_servo({LL: 105, RL: 180})  
    time.sleep(0.2)
    move_servo({LF: 102})            
    time.sleep(0.5)

def right_swing():
    move_servo({LL: 5, RL: 85}) 
    time.sleep(0.2)
    move_servo({RF: 81})
    time.sleep(0.5)

def left_walk_forward():
    move_servo({LL: 105, RL: 180})  
    time.sleep(0.2)
    move_servo({LF: 102})            
    time.sleep(1)
    return_to_neutral()

def right_walk_forward():
    move_servo({LL: 5, RL: 85}) 
    time.sleep(0.2)
    move_servo({RF: 81})
    time.sleep(1)
    return_to_neutral()

def left_walk_back():
    move_servo({LL: 105, RL: 180})  
    time.sleep(0.2)
    move_servo({LF: 81})            
    time.sleep(1)
    return_to_neutral()

def right_walk_back():
    move_servo({LL: 5, RL: 85}) 
    time.sleep(0.2)
    move_servo({RF: 102})
    time.sleep(1)
    return_to_neutral()

def moonwalk(delay=0.4):
    move_servo({LL: 105, RL: 180})  
    time.sleep(delay)
    move_servo({RL: 85})
    time.sleep(delay)
    move_servo({RL: 180})
    time.sleep(delay)
    move_servo({LL: 5, RL: 85}) 
    time.sleep(delay)
    move_servo({LL: 102})
    time.sleep(delay)
    move_servo({LL: 5})
    time.sleep(delay)
    return_to_neutral()


def steps(delay=0.5):
    for i in range(3):
        move_servo({LL: 35, RL: 80})
        time.sleep(delay)  
        move_servo({LL: 105, RL: 145})
        time.sleep(delay)
    
    return_to_neutral()

def waddle(delay=0.5):
    for i in range(3):
        move_servo({LL: 105, RL: 180})  
        time.sleep(delay)
        move_servo({LL: 5, RL: 85}) 
        time.sleep(delay)
    return_to_neutral()

def balerina():
    move_servo({LL: 105, RL: 180})  
    time.sleep(0.2)
    
    for i in range(4):
        move_servo({RL: 100, LF: 102})
        time.sleep(0.4)
        move_servo({RL: 180, LF: 102})
        time.sleep(0.4)
    return_to_neutral()
    time.sleep(0.2)

    move_servo({LL: 5, RL: 85})
    time.sleep(0.2)

    for i in range(4):
        move_servo({LL: 80, RF: 81})
        time.sleep(0.4)
        move_servo({LL: 5, RF: 81})
        time.sleep(0.4)
    return_to_neutral()
    time.sleep(0.2)

def weird(iterations=5):
    for _ in range(iterations):
        lf_speed = random.choice([72, 112])
        rf_speed = random.choice([72, 112])
        move_servo({LF: lf_speed, RF: rf_speed})
        time.sleep(1)
    return_to_neutral()

def boogie(delay=0.3):
    left_walk_forward()
    time.sleep(delay)
    right_walk_back()
    time.sleep(delay)
    left_walk_back()
    time.sleep(delay)
    right_walk_forward()
    time.sleep(delay)
    return_to_neutral()

def drink(delay=1):
    move_servo({LL: 35, RL: 80})
    time.sleep(0.2)
    move_servo({LF: 112})
    time.sleep(delay)

    move_servo({LL: 105, RL: 145})
    time.sleep(0.2)
    move_servo({RF: 72})
    time.sleep(0.2)

    move_servo({LL: 35, RL: 80})
    time.sleep(0.2)
    move_servo({LF: 78})
    time.sleep(delay)

    move_servo({LL: 105, RL: 145})
    time.sleep(0.2)
    move_servo({RF: 132})
    time.sleep(0.1)

    move_servo({LL: 105, RL: 80})
    time.sleep(0.2)
    move_servo({RF: 78})
    time.sleep(delay)

    move_servo({LL: 35, RL: 80})
    time.sleep(0.2)
    move_servo({RF: 78})
    time.sleep(delay)

    move_servo({LL: 105, RL: 145})
    time.sleep(0.2)
    move_servo({RF: 72})
    time.sleep(0.2)


    return_to_neutral()

def circles():
    move_servo({LL: 170, RL: 25})  
    time.sleep(0.5)

    move_servo({LF: 122, RF: 82})
    time.sleep(2.5)

    move_servo({LF: 102, RF: 67})
    time.sleep(3)

    return_to_neutral()