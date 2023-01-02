import asyncio
import websockets
import json
from language_processor import define

class WebsocketHandler:
    # List of valid commands
    commands = ["translate", "define", "synonyms", "antonyms"]

    async def handle(self, websocket, path):
        # Async loop to iterate over incoming messages
        async for message in websocket:
            # Check if message is a valid command object
            if self.validate_message_object(websocket, message):
                # TODO: Handle command here
                message_object = json.loads(message)
                await websocket.send(message_object["action"])
                if message_object["action"] == "translate":
                    await websocket.send(str(define.define_word(input_language=message_object["input_language"], word=message_object["word"])))
            else:
                # Check if message is a predefined command
                if message == "hello":
                    await self.handle_hello(websocket, message)
                elif message == "goodbye":
                    await self.handle_goodbye(websocket, message)
                else:
                    await self.handle_default(websocket, message)

    async def handle_hello(self, websocket, message):
        await websocket.send("Hello, world!")

    async def handle_goodbye(self, websocket, message):
        await websocket.send("Goodbye, world!")

    async def handle_default(self, websocket, message):
        await websocket.send("I don't understand this message.")

    def validate_message_object(self, websocket = None, message = None):
        """Validates a message object by checking if it is a valid JSON object with a valid 'action'"""
        try:
            message_object = json.loads(message)
            if 'action' in message_object and message_object['action'] in WebsocketHandler.commands:
                return True
        except json.JSONDecodeError:
            return False
        
        return False