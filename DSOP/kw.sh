#!/bin/bash
k=0
for i in $* 
do
k=$((($i*$i)+$k))
done
echo $k
