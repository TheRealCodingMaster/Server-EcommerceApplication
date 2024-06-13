import subprocess
import sys

def start_server():
    try:
        subprocess.run([sys.executable, 'run_application.py'])
    except Exception as e:
        print(f"Error starting server: {e}")

def stop_server():
    try:
        subprocess.run(["pkill", "-f", "python run_application.py"])
        print("Server stopped successfully.")
    except Exception as e:
        print(f"Error stopping server: {e}")

if __name__ == '__main__':
    action = sys.argv[1] if len(sys.argv) > 1 else None

    if action == 'start':
        start_server()
    elif action == 'stop':
        stop_server()
    else:
        print("Usage: python toggle_server.py [start|stop]")
