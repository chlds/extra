import hashlib
import time


def main():
	print("time.localtime():",time.localtime())
	print("time.mktime(time.localtime()):",time.mktime(time.localtime()))
	print("time.gmtime():",time.gmtime())
	print("time.ctime():",time.ctime())
	print("time.time():",time.time())
	t = time.localtime()
	print(f"Current: {t.tm_hour}:{t.tm_min}:{t.tm_sec} {t.tm_mday} {t.tm_mon} {t.tm_year}")


if(__name__==("__main__")): main()
