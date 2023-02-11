#!/bin/bash
l=$1
if ([ "$l" -eq "$l"  -a  $l -gt 0 ]) &> /dev/null
then
while [ $l -gt 0 ]
do
str="$((l%2))$str"
l=$((l/2))
done
echo $str
exit 0
else
echo "Argumentem powinna byc liczba dodatnia" 1>&2
exit 1
fi
