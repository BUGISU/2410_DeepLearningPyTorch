import socket
import struct
from PIL import Image
import io


def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Receive the size of the incoming data
        data_size = struct.unpack('>I', conn.recv(4))[0]
        print(f"Expecting {data_size} bytes of data")

        # Receive the image data
        data = b""
        while len(data) < data_size:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet

        print("Image received. Processing...")

        # Convert bytes to image
        image = Image.open(io.BytesIO(data))
        image.show()  # Display the received image (optional)

        # Save the received image
        image.save("ReceivedImage.png")
        print("Image saved as 'ReceivedImage.png'")

        conn.close()

if __name__ == "__main__":
    start_server()

