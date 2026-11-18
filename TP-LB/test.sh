#!/bin/bash
#500 appels  
for i in $(seq 1 500)

do
	curl -s localhost:83
done > resultat.txt

#compter
echo "serveur 1 :"
grep "Hello 1" resultat.txt | wc -l
echo "serveur 2 :"
grep "Hello 2" resultat.txt | wc -l
