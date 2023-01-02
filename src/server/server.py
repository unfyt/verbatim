import asyncio
import websockets

from server.websocket_handler import WebsocketHandler

async def setup_server():
    handler = WebsocketHandler()
    server = await websockets.serve(handler.handle, "localhost", 8080)
    print("Listening for connections on ws://localhost:8080...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(setup_server())