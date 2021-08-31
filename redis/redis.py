from redis import Redis

server = Redis(host="localhost", port=6379)
server.set("cle1", "kghmsdlkjghmsdgh")
print(server.get('cle1'))