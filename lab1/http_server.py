import socket 

host = '0.0.0.0'
port =  8080

server_http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_http.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
server_http.bind((host , port))
# Allow 10 in queue so the server doesnt crash due to errconref
server_http.listen(10)
print('HTTP Server running on port:',port)

while True:
    client_connection , client_ip = server_http.accept()
    http_request = client_connection.recv(4096).decode('utf-8')
    print('HTTP Request:', http_request)
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

    final_http_response = http_header.encode('utf-8')
    final_http_response += http_response
    print('HTTP Response:', final_http_response)
    client_connection.send(final_http_response)
    client_connection.close()

