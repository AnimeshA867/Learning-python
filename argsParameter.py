class myClass : 
    def __init__(self,*args):
        self.arr=args;




    def sum(self):
        self.sum=0;
        for arg in self.arr:
            self.sum+=arg;

        return self.sum

    def print(self):
        print(self.sum);


def check (*args,**kargs):
    print(args,type(args));
    print(kargs,type(kargs));

check(10,20,20,name='Animesh',surname="Acharya")

newClass=myClass(10,20,30,40)
newClass.sum();
newClass.print();