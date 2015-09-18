#!/usr/bin/env python3
dp={
    'v':'v',
    'vi':'v',
    'vt':'v',
    'n':'n',
    'adj':'aj',
    'adv':'av',
    'interj':'inj',
    'prep':'prp'
}
sg={    'æ':'\\ae ',
        'ə':'@',#If emphasized, it should be wedge
        'ɑ':'A',
        'ð':'D',
        'ɛ':'E',
        'ɪ' :'I',
        'ŋ' :'N' ,
        'ɔ':'O' ,
        'ʃ' :'S' ,
        'θ':'T',
        'u':'u' ,
         'ʊ' :'\\textupsilon ',
        'ʒ':'Z' ,
        'ˌ' :'""',
        "'":'"',
        'ˈ':'"',
        'ː':':',
        'ɜ':'3',
        'ʌ':'2',
        'ɡ':'g',
        'ɒ':'6',
        'Ÿ':'@'
    }
def toascii(s):
    if s in sg:
        return sg[s]
    else:
        #if not ('a'<=s<='z' or 'A'<=s<='Z'):
            #print('Unexpected',s, end='')
        return s
def pron2tex(s):
    ss=[toascii(i) for i in s]
    #print(s)
    return ''.join(ss)
pdic={}
def additems(fname):
    f=open(fname,'r')
    for line in f:
        line=line.strip('\n')
        if len(line)==0:
            break
        wd,mn=line.split('\t')
        if wd not in pdic:
            pdic[wd]=mn
    f.close()
dics=['moby','oxford','langdao']
for i in dics:
    additems(i+'/'+i+'.prb')
def yb(word,pp):
    if pp in dp:
        word2=word+'/'+dp[pp]
        if word2 in pdic:
            return pdic[word2]
    if word in pdic:
        return pdic[word]
    else:
        #print('From ys:',word2)
        return ''
def prpt(s):
    for i in range(6):
        if not 'a'<=s[i]<='z':
            break
    return s[:i]
def ame(s):
    l=s.split(',')
    for i in l:
        if i:
            return i
    return ''
if __name__=='__main__':
    print('hello')