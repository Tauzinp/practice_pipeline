#!/bin/bash

echo "Script bash lancé"

ID_SEQ=$1
DESC=$2
SEQ=$3

echo "Voici la séquence qu'on va transformer : $SEQ"

mkdir -p tp_egene/files

PLACE=tp_egene/files/$ID_SEQ.fasta
touch "$PLACE"

echo "> $ID_SEQ   $DESC" >"$PLACE"
echo "$SEQ" >>"$PLACE"
