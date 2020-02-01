class graphix():
    def __init__(self,x,y):
        self.xlen = x
        self.ylen = y
        row = []
        visu = []
        counter = 0
        while counter != self.ylen:
            for i in range(self.xlen):
                if len(row) != x:
                    row.append('0 ')
                else:
                    visu.append(row)
                    row = []
                    counter += 1
        self.visu = visu
    def clearprint(self):
        temp = self
        temp.cleargraphix()
        temp.printgraphix()
        #sleep(0.5)
    def printgraphixlab(self):
        disp = ' '
        xlab = '   '
        xlab2= '   '
        cntr = 0
        for i in range(self.xlen):
            if len(str(i)) == 1:
                xlab += '{0} '.format(i)
                xlab2+= '  '
            else:
                xlab += str(i)[0] + ' '
                xlab2+= str(i)[1] + ' '
        print(xlab)
        print(xlab2)
        for i in self.visu:
            for h in i:
                disp += h
            if len(str(cntr)) == 1:
                cnt = '{0} '.format(str(cntr))
            else:
                cnt = str(cntr)
            print(cnt + disp)
            cntr += 1
            disp = ' '
    def printgraphix(self):
        disp = ''
        cntr = 0
        for i in self.visu:
            for h in i:
                disp += h
            print(disp)
            cntr += 1
            disp = ''
        print(disp)
    def togglecell(self,x,y):
        if self.visu[y][x] == '1 ':
            self.visu[y][x] = '0 '
        else:
            self.visu[y][x] = '1 '
    def togglevert(self,x):
        for i in self.visu:
            if i[x] == '1 ':
                i[x] = '0 '
            else:
                i[x] = '1 '
    def togglehori(self,y):
        counter = 0
        row = []
        for i in self.visu[y]:
            if i == '1 ':
                row.append('0 ')
            else:
                row.append('1 ')
        self.visu[y] = row
    def cleargraphix(self):
        for i in range(self.ylen):
            for a in range(self.xlen):
                if self.visu[i][a] == '0 ':
                    self.visu[i][a] = '  '

def codemaker(x,y,name):
    temp = graphix(x,y)
    lines = []
    temp.printgraphixlab()
    while True:
        x1, y1 = [int(x) for x in input("Enter: 'x y' ('500 500' to stop) ").split()]
        if x1 == 500 and y1 == 500:
            print('{0} = graphix({1}, {2})'.format(name,x,y))
            for i in lines:
                print(i)
            print('{0}.clearprint()'.format(name))
            break
        temp.togglecell(x1,y1)
        temp.printgraphixlab()
        x1 = str(x1)
        y1 = str(y1)
        lines.append('{0}.togglecell({1}, {2})'.format(name,x1,y1))
