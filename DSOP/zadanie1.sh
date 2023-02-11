#!/bin/bash
if [ $# -eq 0 ]; then exit 1; fi
wynik = "x"
while [ $# -ge 1 ]
do
    wynik="$1 $wynik"
    shift
done

echo $wynik
