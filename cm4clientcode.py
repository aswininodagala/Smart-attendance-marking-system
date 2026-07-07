from picamera2 import Picamera2
import cv2, socket, struct, pickle, time

SERVER_IP = "192.168.137.1"   # WSL IP
SERVER_PORT = 8000

# Initialize cameras
camL = Picamera2(0)
camR = Picamera2(1)

cfgL = camL.create_preview_configuration(main={"size": (640, 640), "format": "RGB888"})
cfgR = camR.create_preview_configuration(main={"size": (640, 640), "format": "RGB888"})

camL.configure(cfgL)
camR.configure(cfgR)
camL.start()
camR.start()

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print(f"?? Connected to server at {SERVER_IP}:{SERVER_PORT}")

count = 0

try:
    while True:
        # Capture frames
        frameL_bgr = camL.capture_array()
        frameR_bgr = camR.capture_array()

        # Encode and send
        data = pickle.dumps({
            "left": cv2.imencode(".jpg", frameL_bgr)[1].tobytes(),
            "right": cv2.imencode(".jpg", frameR_bgr)[1].tobytes(),
            "timestamp": time.time(),
            "index": count
        })
        message_size = struct.pack(">Q", len(data))  # Q = unsigned long long (8 bytes), big-endian
        client.sendall(message_size + data)

        print(f"?? Captured & sent frame pair {count}")
        count += 1

        time.sleep(0.05)  # small delay to avoid flooding

except KeyboardInterrupt:
    print("\n?? Streaming stopped manually.")

finally:
    camL.stop()
    camR.stop()
    client.close()