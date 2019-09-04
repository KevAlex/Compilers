fle= open("carac.txt", "r")
sign = ["+",'-','*','/','=','(',')', ';']

#fles = open ('test.cpp','r')
r=5 # avoid general terms used in cpp sintaxis such as #include and so on
lst =[]

for ln in fle:
    lst.append(ln)
    
'''while(r < len(lst)):
    for d in lst[r].split():
        if(d in sign):
            print 'sign :', d
        else:
            print 'word:', d
        #print d
    
    r+=1
'''
print lst

while(r < len(lst)):
    
    for d in lst[r].split('='):  # more than one parameter
        print d
        for p in d.split('-'):
            print p

    r+=1
