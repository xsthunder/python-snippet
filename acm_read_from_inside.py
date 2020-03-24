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
            print('Warning: relocate i')
            self.i = 0
            return self.read()
        self.i = i + 1
        return l[i]
read = Read(True, """
6 4
-10 8 2 1 2 6
""").read
input = read

# in your code
read = input 
rn = lambda :list(map(int, read().split()))
