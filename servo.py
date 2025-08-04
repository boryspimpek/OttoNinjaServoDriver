import socket
import time

# Konfiguracja UDP
UDP_IP = "192.168.0.144"  # Adres IP ESP8266
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definicje serw i pozycji neutralnych
LL = "LL"  # Left Leg (standardowe)
LF = "LF"  # Left Foot (ciągłe 360°)
RL = "RL"  # Right Leg (standardowe)
RF = "RF"  # Right Foot (ciągłe 360°)

LLN = 70    # neutralny kąt dla LL
LFN = 90    # neutralna prędkość (stop) dla LF
RLN = 113   # neutralny kąt dla RL
RFN = 90    # neutralna prędkość (stop) dla RF

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
    """
    Wysyła komendę do robota
    Dla standardowych serw: {"LL": 90} lub {"LL": (90, 'a')}
    Dla serw ciągłych: {"LF": (90, 's')} gdzie 90=stop, 0-180 to prędkość
    """
    command_parts = []
    
    for servo, value in servos_angles.items():
        if isinstance(value, tuple):
            angle_speed, value_type = value
            command_parts.append(f"{servo}:{angle_speed}{value_type}")
        else:
            # Automatyczne rozpoznanie typu serwa
            value_type = 's' if servo in ['LF', 'RF'] else 'a'
            command_parts.append(f"{servo}:{value}{value_type}")
            # Aktualizacja current_pos
            if value_type == 'a':
                current_pos[servo] = value
            else:
                current_pos[servo] = value  # dla serw ciągłych też zapisujemy
    
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
    """Przesuwa wszystkie serwa do pozycji/stanów neutralnych"""
    move_servo({
        LL: (LLN, 'a'),  # standardowe serwo - kąt
        LF: (LFN, 's'),  # serwo ciągłe - stop
        RL: (RLN, 'a'),  # standardowe serwo - kąt
        RF: (RFN, 's')   # serwo ciągłe - stop
    })
    
    # Aktualizacja current_pos
    global current_pos
    current_pos = {
        LL: LLN,
        LF: LFN,
        RL: RLN,
        RF: RFN
    }

def walk(stop_flag=None):
    return_to_neutral()

    for i in range(4):
        if stop_flag and stop_flag.is_set():
            break
        left_walk_forward()
        time.sleep(0.1)
        if stop_flag and stop_flag.is_set():
            break
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

