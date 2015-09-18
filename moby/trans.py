#!/usr/bin/env python3
db={
        '(@)':'e',
        '[@]':'ɜː',
        '@r':'ər',
        'aI':'aɪ',
        'Ar':'ɑr',
        'AU':'aʊ',
        'Oi':'ɔɪ'
    }
sg={
        '&' :'æ' ,
        '-' :'',###可能有问题
        '@' :'ə' ,#If emphasized, it should be wedge
        'A' :'ɑː',
        'D' :'ð' ,
        'E' :'ɛ' ,
        'i' :'iː',
        'I' :'ɪ' ,
        'N' :'ŋ' ,
        'O' :'ɔː',
        'S' :'ʃ' ,
        'T' :'θ' ,
        'u' :'uː',
        'U' :'ʊ' ,
        'Z' :'ʒ',
        ',':'ˌ'
    }
def emps(s):
    rsl=s.split('/')
    if(len(rsl)>1):
        if(rsl[1]=='@'):
            rsl[1]='ʌ'
        return '/'.join(rsl)
    return s
def moby2pron(s):
    ll=s.split("'")
    le=[emps(i) for i in ll]
    le[0]=ll[0]
    s="'".join(le)
    for key,value in db.items():
        s=s.replace(key,value)
    for key,value in sg.items():
        s=s.replace(key,value)
    s=s.replace('/','')
    return s
#with open('mobypron.unc','r') as f:
    #for i in f:
        #print(i)
if __name__=='__main__':
    f=open('mobypron.unc','r')
    g=open('moby.prb','w')
    for i in f:
        if len(i)>2:
            l=(i.strip('\n')).split()
            rl=l[1].split('_')
            prl=[moby2pron(j) for j in rl]
            rs=' '.join(prl)
            g.write(l[0]+'\t'+rs+'\n')
    f.close()
    g.close()
