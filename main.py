import Container


fin = open("test1.txt", "r")
fout = open("out1.txt", "w")
c = Container.Container(fin, fout)
c.read()
c.sort()
c.print()
fin.close()
fout.close()
