# Not put numbers in formulae


import time
import asyncio


DBG = (0x01)
OFFSET = (0x01)
MONTH = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC',]
m = [f'{OFFSET+(i)}. {MONTH[i]}' for i in range(len(MONTH))]
if DBG: print(m,len(m))


async def fn(delay,msg):
	await asyncio.sleep(delay)
	print(msg,'at',str(time.time()))


async def main():
	print('Create tasks at',str(time.time()))
	sec = (0x02)
	t = [asyncio.create_task(fn(sec,m[i])) for i in range(len(m))]
	if DBG: print(t,len(t))
	print('Started at',str(time.time()))
	print('--------')
	for i in range(len(t)):
		await t[i]
		print('<',i,'>',str(time.time()))
	print('--------')
	print('Finished at',str(time.time()))


if(__name__==('__main__')): asyncio.run(main())
