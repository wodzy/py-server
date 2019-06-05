import http.server

port = 8080
server_address = ("localhost", port)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler

handler.cgi_directories = ["web/"]
print("listening on the port", port)

httpd = server(server_address, handler)
httpd.serve_forever()
