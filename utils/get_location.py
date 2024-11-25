import asyncio
import aiohttp


async def get_full_address(longitude, latitude):
    """This is open source map api to get full address, if it does not work return False"""
    await asyncio.sleep(1)
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('display_name')
            return False
