# test_client.py (for testing purposes)
import asyncio
import websockets

async def test_query():
    uri = "ws://localhost:8182"
    async with websockets.connect(uri) as websocket:
        query = "g.V().toList()"  # Example Gremlin query
        await websocket.send(query)
        response = await websocket.recv()
        print(response)

asyncio.run(test_query())
