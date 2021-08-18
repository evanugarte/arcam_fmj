import asyncio

from arcam.fmj import SourceCodes
from arcam.fmj.client import Client
from arcam.fmj.client import ClientContext
from arcam.fmj.state import State

async def run():

    host = '192.168.1.76'
    port = '50000'
    zone = 1

    volume = 5
    source = SourceCodes.PVR

    client = Client(host, port)
    async with ClientContext(client):
        state = State(client, zone)
        # await state.set_power
        # state.set_power
        await state.set_power(False)
        huh = state.get_power()
        print(huh, 'yahoo')
        await state.set_volume(4)
        # await state.set_power(True)
        # await state.set_source(source)

loop = asyncio.get_event_loop()
loop.run_until_complete (run())

