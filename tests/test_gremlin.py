import asyncio
import websockets
import json
import pytest


@pytest.mark.asyncio
async def test_gremlin_query_1(server):
    async with websockets.connect(server) as websocket:
        query = {"query": "g.V().count()"}
        await websocket.send(json.dumps(query))
        response = await websocket.recv()
        print(f"Received response: {response}")
        assert json.loads(response) == {
            "status": "success", "data": "Query result here"}


@pytest.mark.asyncio
async def test_gremlin_query_2(server):
    async with websockets.connect(server) as websocket:
        query = {"query": "g.E().count()"}
        await websocket.send(json.dumps(query))
        response = await websocket.recv()
        print(f"Received response: {response}")
        assert json.loads(response) == {
            "status": "success", "data": "Query result here"}
