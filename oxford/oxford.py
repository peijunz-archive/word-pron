#!/usr/bin/env python3
def rsp(s):
    return s.strip().lstrip()
fr=open('oxford.txt','r')
fw=open('oxford.prb','w')
for line in fr:
    tmp=''.join(line.split(' • '))
    tmp=tmp.split("\t")
    word=tmp[0]
    root=(tmp[1].split())[0]
    word2=word.split()
    word=word2[0]
    if word != root:
        #找到这个单词后，从这个单词后面开始进行类似计算
        continue
    if len(word2)>=2:
        continue
    tmpword=tmp[1].split('/')
    if ('BrE' in tmpword[1]) and ('NAmE' in tmpword[1]) and (';' in tmpword[1]):
        tmp2=tmpword[1].split(';')
        if len(tmp2)>1:
            if len(tmp2[0].split('BrE'))>=2:
                eng=rsp(tmp2[0].split('BrE')[1])
            else:
                eng=''
            if len(tmp2[1].split('NAmE'))>=2:
                ame=rsp(tmp2[1].split('NAmE')[1])
            else:
                ame='0'
    elif len(tmpword)>=4:
        eng=rsp(tmpword[1])
        ame=rsp(tmpword[3])
    else:
        continue
    if (' ' in eng) or (' ' in ame):
        continue
    if eng==ame:
        if len(eng) != 0:
            fw.write(word+'\t'+ame+'\n')
    else:
        fw.write(word+'\t'+ame+', '+eng+'\n')
