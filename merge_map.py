#!/usr/bin/env python3
map1=open("oxford_map",'r')
map2=open("lang_map",'r')
mmap=open("map",'w')
dic={}
for line in map1:
    line=line.strip('\n')
    if len(line)==0:
        break
    tmp=line.split('\t')
    dic[tmp[0]]=tmp[1]
for line in map2:
    line=line.strip('\n')
    if len(line)==0:
        break
    tmp=line.split('\t')
    if not (tmp[0] in dic):
        dic[tmp[0]]=tmp[1]
for i in dic:
    mmap.write(i+'\t'+dic[i]+'\n')
