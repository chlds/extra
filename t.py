import time
import asyncio


async def fn(delay,msg):
	await asyncio.sleep(delay)
	print(msg,'at',str(int(time.time())))


async def main():
	print('Create tasks at',int(time.time()))
	sec = (0x00)
	t1 = asyncio.create_task(fn(sec+3,'Task 1'))
	t2 = asyncio.create_task(fn(sec+2,'Task 2'))
	t3 = asyncio.create_task(fn(sec+1,'Task 3'))
	print('Started at',int(time.time()))
	print('--------')
	await t1
	await t2
	await t3
	print('--------')
	print('Finished at',int(time.time()))


if(__name__==('__main__')): asyncio.run(main())
