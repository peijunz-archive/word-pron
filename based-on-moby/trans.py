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
def moby2pron(s):
    ll=s.split("'")
    if(len(ll)==1):
        ls=''
        rs=ll[0]
    elif len(ll)==2:
        #print(ll)
        ls=ll[0]
        rs=ll[1]
    else:
        print(s)
        return ''
    #rs=rs.lstrip('/')
    rsl=rs.split('/')
    if(len(rsl)>1):
        if(rsl[1]=='@'):
            rsl[1]='ʌ'
        rs='/'.join(rsl)
        s=ls+"'"+rs
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
    g=open('base','w')
    for i in f:
        if len(i)>2:
            l=(i.strip('\n')).split()
            rl=l[1].split('_')
            prl=[moby2pron(j) for j in rl]
            rs=' '.join(prl)
            g.write(l[0]+'\t'+rs+'\n')
    f.close()
    g.close()
