import socket

print("PORT STATUS CHECKER")

host = input("Enter website name: ")
port = int(input("Enter port number: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    result = s.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED or FILTERED")

    s.close()

except Exception as e:
    print("Error:", e)
