import json
import websocket
import asyncio
import random, time
import ast
from . views import get_strain_data


ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/graph/')

while True:

    data = get_strain_data
    #print(data)
    data.decode('utf-8')
    value=str(data.decode('utf-8'))
    print(value)

    result = ast.literal_eval(value)

    time.sleep(5)

    ws.send(json.dumps({'value':result}))

