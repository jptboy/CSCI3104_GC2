#/usr/bin/env python3
from os import system
import sys
import time
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python3 runAllNetworks.py k")
    exit(1)
k = int(sys.argv[1])
if len(sys.argv) == 3 and sys.argv[1] == "write":
    for i in range(1,2):
        time.sleep(1)
        system("python3 main.py graph%d.net %d write" % (i, k))
        time.sleep(1)
else:
    for i in range(1,5):
        time.sleep(1)
        system("python3 main.py graph%d.net %d" % (i, k))
        time.sleep(1)