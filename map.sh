#!/usr/bin/env bash
python3 lang.py
python3 oxford.py
python3 merge_map.py
pron='/home/zpj/code/pronounce'
cp ./map $pron/map
