class Read:
    def __init__(self, test = True, s=None):
        self.test = test
        self.s = s
        self.i = 0
        if(s != None and test == True):
            l = s.split('\n')
            l = list(filter(lambda x:len(x)>0, l))
            self.l = l
    def read(self):
        if(self.test == False):
            return input()
        i = self.i
        l = self.l
        if i == len(l):
            print('Warn: relocate i')
            self.i = 0
            return self.read()
        self.i = i + 1
        return l[i]

read = Read(True, """
10 10 10 20
7467038376 5724769290 292794712 2843504496 3381970101 8402252870 249131806 6310293640 6690322794 6082257488
1873977926 2576529623 1144842195 1379118507 6003234687 4925540914 3902539811 3326692703 484657758 2877436338
4975681328 8974383988 2882263257 7690203955 514305523 6679823484 4263279310 585966808 3752282379 620585736
""").read

# read = input

# use read instead of input