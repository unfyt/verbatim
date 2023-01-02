import asyncio
from server import server

#This file will most likely be used to setup any services required for translation and turning the websocket server on.

def setup():
    asyncio.run(server.setup_server())

if __name__ == "__main__":
    setup()


