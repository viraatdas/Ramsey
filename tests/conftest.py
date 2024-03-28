import asyncio
import websockets
import json
import pytest


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def handle_gremlin_query(websocket, path):
    async for message in websocket:
        print(f"Received query: {message}")
        response = {"status": "success", "data": "Query result here"}
        await websocket.send(json.dumps(response))


@pytest.fixture(scope="session")
def test_server(event_loop):
    start_server = websockets.serve(handle_gremlin_query, "localhost", 8182)
    server = event_loop.run_until_complete(start_server)
    yield
    server.close()
    event_loop.run_until_complete(server.wait_closed())


@pytest.fixture(scope="session")
def server(event_loop, test_server):
    return "ws://localhost:8182"
