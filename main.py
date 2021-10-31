import Container
import settings
import sys
import time


start = time.time()
settings.fin = open(sys.argv[1], "r")
settings.fout = open(sys.argv[2], "w")
c = Container.Container()
c.read()
c.sort()
c.print()
settings.fin.close()
settings.fout.close()
end = time.time()
print((end - start) * 1000)
