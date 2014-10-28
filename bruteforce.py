import hashlib
import itertools
import time
from multiprocessing import Pool
start_time = time.time()

def findPassword1(hashed):
	salt = hashed[0] + hashed[1]
	hashed = hashed.lower()
	# salt = hashed[len(hashed)-2] + hashed[len(hashed)-1]
	for x in range(10000): 
		pw = ""
		pw = pw + str(x)
		while len(pw) < 4:
			pw = "0" + pw
		
		# print h
		if h == hashed[2:len(hashed)]:
		# if h == hashed[0:len(hashed)-1]:
			print(pw)
			break

def findPassword2(hashed):
	salt = hashed[0] + hashed[1]
	hashed = hashed.lower()
	symbols = "abcdefghijklmnopqarstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXWZ1234567890!@#$%^&*()_+-="
	results = itertools.product(symbols, repeat=6)
	count = 0
	temp = 10000000
	for result in results:
		pw = "".join(result)
		h = hashlib.sha1(salt+pw).hexdigest()
		#test
		#if h == "04a46f52a7ce320f291cdfdd3eca0bbca03ae303":
		if h == hashed[2:len(hashed)]:
			print("CRACKED PASSWORD: " + pw)
			break
		count += 1
		if count == temp:
			print pw
			print(str(time.time() - start_time) + " seconds")
			count = 0

if __name__ == "__main__":
	# findPassword1("cSDFFDA3739F00B966F692D145EF4946762AC1B379")
	findPassword2("FTBCE5A668FEAD98B7A9823487F537AF709F215A3E")
	print(str(time.time() - start_time) + " seconds")