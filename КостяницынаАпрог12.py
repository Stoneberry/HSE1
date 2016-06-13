import os

# в папке где программа, найти папку, где больше всего файлов

def function0():
    d={}
    for root, dirs, files in os.walk('C:\\Users\\Та\\Desktop\\универр'):
        for i in dirs:
            for root1, dirs1, files1 in os.walk('C:\\Users\\Та\\Desktop\\универр\\' + i):
                d[len(files1)]=i
    return d

def function1(d):
    a1=[]
    for l in sorted(d):
        a1.append(l)
    y=a1[-1]
    print(d[y])


def main():
    vab1 = function0()
    vab2 = function1(vab1)
    
if __name__=='__main__':
    main()
