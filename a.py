import time
import asyncio


async def main():
	print('Hello',str(int(time.time())))
	await asyncio.sleep(1)
	print('World!',str(int(time.time())))


if(__name__==('__main__')): asyncio.run(main())
