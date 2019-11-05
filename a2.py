import time
import asyncio


async def fn(delay,msg):
	await asyncio.sleep(delay)
	print(msg,'and output at',str(int(time.time())))


async def main():
	sec = (0x00)
	print('Started at',int(time.time()))
	await fn(sec+2,'The 1st call at '+str(int(time.time())))
	await fn(sec+1,'The 2nd call at '+str(int(time.time())))
	print('Finished at',int(time.time()))


if(__name__==('__main__')):
	print('Created at',str(int(time.time())))
	asyncio.run(main())
