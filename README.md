## Socket TCP Communication and Concurrency Management in Python 

### About:
This project explores the native `socket` library in Python and manages concurrency using `threading`. I implemented **Object-Oriented Programming (OOP)** to ensure the logic is modular and reusable for future networking projects.

## This is a practice of concurrency management and communication between processes via TCP Sockets.

### Project Structure
* **`/client_server_code`**: Core logic for `client_class.py` and `server_class.py`.
* **`/functions`**: Helper functions to keep the class logic clean.
* **`test_server.py` & `test_client.py`**: Entry points to initialize the communication.

### Features
* **Object-Oriented Programming**: High encapsulation to make the socket logic easily scalable.
* **Concurrency via Threading**: Uses the `threading` library to handle multiple simultaneous client connections without blocking the server.
* **Robust Error Management**: Includes auto-reconnection logic for clients and exception handling for broken pipes or connection timeouts.
* **Reusable Architecture**: Designed as a library/module structure for easy integration into other software.

### Requirements
* **Python 3.x**
* **OS**: Linux/macOS (Windows users may need to adjust pathing if running via shell scripts).

### Setup & Execution
1. **Clone the repo**
```bash
git clone [https://github.com/SadCloud03/chat-sockets-tcp.git](https://github.com/SadCloud03/chat-sockets-tcp.git)
cd chat-sockets-tcp
```
2. **Run the Server (terminal 1)**
```bash
python3 test_server.py
```

3. **Run the Clients (Other Terminals)**
```bash
python3 test_client1.py
python3 test_client2.py
```