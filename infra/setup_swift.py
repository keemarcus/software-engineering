from server import Server

host = "3.135.18.121"

server = Server(host=host, user="ubuntu", key_filename="/home/greg/.ssh/lightsail-ohio.pem")

stdout, stderr = server.run("ls -la")

print(stdout)