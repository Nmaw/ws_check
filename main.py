import asyncio
import datetime
import random
import websockets


async def time(websocket, path):
    """
    WS server that sends messages at random intervals
    :param websocket:
    :param path:
    :return:
    """
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        print("Time:", now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "0.0.0.0", 5678)
print("Start Web Socket Server on 0.0.0.0:5678 port")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
