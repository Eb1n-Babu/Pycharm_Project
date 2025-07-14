import threading
import time

def process_data():
    time.sleep(2)
    print("Student data processed.")

def start_processing():
    thread = threading.Thread(target=process_data)
    thread.start()
