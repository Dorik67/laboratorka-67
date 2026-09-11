#!/bin/bash
read N
cd Desktop
mkdir tips
a=1
while [ $a -le N ];
do 
	touch file$N.txt > tips
	a=$RANDOM
	b=$RANDOM
	echo $a + $b = $(( $a + $b )) > file$N.txt
	a=$(( $a + 1 ))
done
