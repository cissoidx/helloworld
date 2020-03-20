#! /bin/bash

for ((i=1;i<=$num;i++))
do
    echo iterating number $i/$num
    echo preparing experiment ... 
    python3 tests/test.py
    echo cleaning experiment ...
    echo
done
