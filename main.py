import Container
import settings


settings.fin = open("test1.txt", "r")
settings.fout = open("out1.txt", "w")
c = Container.Container()
c.read()
c.sort()
c.print()
settings.fin.close()
settings.fout.close()
