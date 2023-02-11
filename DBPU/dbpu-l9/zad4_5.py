import time

nums1 = []
nums2 = []
nums3 = []

start = time.time()

for i in range(100):
    nums1.append(i * 2)

for i in range(100):
    nums2.append(i * 3)

for i in range(100):
    nums3.append((nums1[i]*nums2[i])%30)

stop = time.time()

suma = (stop-start)*1000000000

print ("Wykonanie w Pythonie: %.0f nanosekund" % suma)
