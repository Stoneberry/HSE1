import re

def function0():
    f=open('C:\\Users\\Та\\Desktop\\forprog1.txt', 'r', encoding = 'utf-8')
    array = f.read()
    f.close()
    return array

def searchfor(array):
    d={}
    x='([1-9][0-9]?-?[1-9]?[0-9]? ?(?:до н.э.|н.э)?) век(?:а|е|ах|у)? ?(?:до н.э.|н.э)?'
    res = re.findall( x, array)
    for word in res:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d

    
def searchfor1(array):
    d1={}
    y='([1-9]?[0-9]? (?:феврял(?:ь|я|е)|марта?|апрел(?:ь|я|е)|ма(?:йе?|а)|июн(?:ь|я|е)|июл(?:ь|я|е)|август(?:е|а)?|октябр(?:ь|я|е)|ноябр(?:ь|я|е)|сентябр(?:ь|я|е)|декабр(?:ь|я|е)|январ(?:ь|я|е)) [1-9][0-9]{3} (?:год(?:а|ах|е|у)?)?)'
    res = re.findall( y, array)
    for word in res:
        if word in d1:
            d1[word]+=1
        else:
            d1[word]=1
    return d1

def searchfor2(array):
    d2={}
    y='([0-9][0-9]\.[0-9][0-9]\.[1-9][0-9]{3})'
    res = re.findall( y, array)
    for word in res:
        if word in d2:
            d2[word]+=1
        else:
            d2[word]=1
    return d2

def final(d,d1,d2):
    fw=open('C:\\Users\\Та\\Desktop\\name1.txt','w',encoding='utf-8')
    for i in d:
        y=str(d[i])
        fw.write(i+'    '+y+'\n')
    for l in d1:
        z=str(d1[l])
        fw.write(l+'    '+z+'\n')
    for k in d2:
        b=str(d2[k])
        fw.write(k+'    '+b+'\n')
    fw.close()
    return fw


def main():
    vab1 = function0()
    vab2 = searchfor(vab1)
    vab3 = searchfor1(vab1)
    vab4 = searchfor2(vab1)
    vab5 = final(vab2, vab3, vab4)


if __name__=='__main__':
    main()

        

                                        
