#!/bin/bash

read -p "Id de la séquence :" ID_SEQ

REGEX="^[A-Z]{2}_[0-9]{6,}\.[0-9]+$"

if [[ $ID_SEQ =~ $REGEX ]]; then
  echo "format d'ID valide. Lancement du script"

  uv run script.py --id "$ID_SEQ"

else
  echo "Format d'ID invalide."
  exit 1

fi
