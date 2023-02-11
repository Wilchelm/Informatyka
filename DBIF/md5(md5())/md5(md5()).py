import hashlib
import time

def md5xmd5(s, b=128): #md5(md5(s))
	m = hashlib.md5(s.encode('utf-8'))
	n = hashlib.md5(m.digest())
	return n.hexdigest()[0:b//4]

def f(x, b):
	return "A!a" + md5xmd5(x,b)

bits = 56
base_string = "A!a"
turtle = hare = base_string
loop_couter = 0
start_time = time.time()

while True:
	turtle = f(turtle, bits)
	hare = f(f(hare, bits), bits)

	if turtle == hare:
		print("> ",turtle, hare)
		print(md5xmd5(turtle), md5xmd5(hare),"\n------------\n")
		print("done in: ",time.time() - start_time, "seconds")
		break
	if loop_couter % 10000 == 0:
		print(loop_couter)

	loop_couter += 1

turtle = base_string

while not md5xmd5(turtle, bits) == md5xmd5(hare, bits):
	turtle = f(turtle,bits)
	hare = f(hare,bits)
print (turtle, " - H: ", md5xmd5(turtle))
print (hare, " - H: ", md5xmd5(hare),"\n")
print(time.time() - start_time, "seconds in total")

file = open('./score md5(md5())', 'w')
x = "Done second loop in: "
x+=str(time.time() - start_time)
x+=" seconds in total\n"
file.write(x)	
y="md5(md5("
y+=str(turtle)
y+="))=0x"
y+=str(md5xmd5(turtle, 128))
y+="\n"
file.write(y)
z="md5(md5("
z+=str(hare)
z+="))=0x"
z+=str(md5xmd5(hare, 128))
z+="\n"
file.write(z)
file.close()
