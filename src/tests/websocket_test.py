import asyncio
import unittest
from server import websocket_handler
import websocket

class TestWebsocketHandler(unittest.TestCase):

    def test_validate_message_object(self):
        handler = websocket_handler.WebsocketHandler()

        # test valid message object
        message = '{"action": "translate", "text": "hello"}'
        self.assertTrue(handler.validate_message_object(message=message))

        # test invalid message object (missing action field)
        message = '{"text": "hello"}'
        self.assertFalse(handler.validate_message_object(message=message))

        # test invalid message object (invalid JSON string)
        message = '{"action": "translate", "text": "hello'
        self.assertFalse(handler.validate_message_object(message=message))

if __name__ == '__main__':
    unittest.main()