#!/usr/bin/env python3
def rsp(s):
    return s.strip().lstrip()
fr=open('lang','r')
fw=open('lang_map','w')
for line in fr:
    tmp=line.split("\t")
    word=tmp[0]
    word2=word.split()
    if len(word2)>=2:
        continue
    if ' [' in tmp[1] and '] ' in tmp[1]:
        eng=tmp[1].split(' [')[1].split('] ')[0]
        fw.write(word+'\t'+eng+'\n')
