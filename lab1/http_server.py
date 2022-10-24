import json
import socket
from threading import Thread

# server's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002 # port we want to use

# initialize list/set of all connected client's sockets
client_sockets = set()
socket_address_book = {}
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs, ca):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            http_request = cs.recv(1024).decode()
            print('http_request: ', http_request)
            http_headers = http_request.split(' ')
            http_request_method = http_headers[0]

            try:
                request_url = http_headers[1]
                route = request_url.split('?')[0]
                route = route.lstrip('/')
            except Exception as e:
                print("Error raised:", e)
    
            if(route == ''):
                route = 'html/index.html'

            try:
                if(route.endswith('.jpg')):
                    route = 'public/images/' + route
                    open_file = open(route , 'rb')
                    http_response = open_file.read()
                    open_file.close()
                    http_header = 'HTTP/1.1 200 OK\n'
                    http_header_content_type = 'image/jpg'
                elif(route.endswith('.pdf')):
                    route = 'public/pdf/' + route
                    open_file = open(route , 'rb')
                    http_response = open_file.read()
                    open_file.close()
                    http_header = 'HTTP/1.1 200 OK\n'
                    http_header_content_type = 'application/pdf'
                elif(route.endswith('.webp')):
                    route = 'public/images/' + route
                    open_file = open(route , 'rb')
                    http_response = open_file.read()
                    open_file.close()
                    http_header = 'HTTP/1.1 200 OK\n'
                    http_header_content_type = 'image/webp'
                else:
                    open_file = open(route , 'rb')
                    http_response = open_file.read()
                    open_file.close()
                    http_header = 'HTTP/1.1 200 OK\n'
                    http_header_content_type = 'text/html'

                http_header += 'Content-Type: '+ str(http_header_content_type) +'\n\n'
                final_http_response = http_header.encode('utf-8')
                final_http_response += http_response
                socket_address_book[ca].send(final_http_response)
                print('HTTP Response:', final_http_response)

            except Exception as e:
                print("Error raised:", e)
                http_header = 'HTTP/1.1 404 Not Found\n\n'
                http_response = '''
                    <html>
                        <head>
                            <title>Not Found</title>
                        </head>
                        <body>
                            <h1>Error 404</h1>
                            <h4>File Not Found<h4>
                        </body>
                    </html>
                    '''.encode('utf-8')
            
            
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            cs.close()
            client_sockets.remove(cs)
        #else:
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            # iterate over all connected sockets
            # if json_msg['dst'] in socket_address_book:
            #     socket_address_book[json_msg['dst']].send(msg.encode())
            # else:
            #     if json_msg['dst'] == 'kernel':
            #         print()
            #     else:    
            #         print('Error, destination does not exist, closing connection...')
            #         client_sockets.remove(cs)
        
while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print('client_socket: ', client_socket, 'client_address: ', client_address)
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket, client_address))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    socket_address_book[client_address] = client_socket
    print('socket_address_book: ', socket_address_book)


# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()