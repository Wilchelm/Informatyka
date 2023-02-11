#!/bin/bash
#
# Podaje najwiekszy wspolny dzielnik liczb $1 i $2.
# Stosuje algorytm Euklidesa.

# Sprawdzenie, czy podany jest pierwszy argument
if [ -z "$1" ] ; then
	echo "Syntax: $0 liczba1 [liczba2]" >& 2
	exit 1
fi

# Sprawdzenie, czy podany jest drugi argument
if [ -z "$2" ] ; then
	echo "NWD( $1 , $1 ) = $1"
	exit 0
fi

# Gdy podane sa dwa argumenty
A=$1
B=$2
while [ $A -ne $B ]
do
	if [ $A -gt $B ] ; then
		let "A=A-B"
	else
		let "B=B-A"
	fi
done
echo "NWD( $1 , $2 ) = $A"
exit 0
