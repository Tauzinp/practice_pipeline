#!/bin/bash

CHOICE=("id" "seq")

PS3="Souhaitez vous importer depuis une id NCBI ou une séquence personnelle ? "
select IMPORT in "${CHOICE[@]}"; do
  if [ -n "$IMPORT" ]; then
    echo "Vous avez choisi l'import par $IMPORT"

  else
    echo "Choix invalide, réessayez."

  fi

  case "$IMPORT" in
  "id")
    TYPE="id_ncbi"
    read -rp "ID du NCBI : " VAL1
    uv run python tp_egene/script_ncbi.py "$TYPE" "$VAL1"
    break
    ;;

  "seq")
    TYPE="seq"
    read -rp "ID de la séquence : " VAL1
    read -rp "Description de la séquence : " VAL2
    read -rp "Séquence : " VAL3
    uv run python tp_egene/script_seq_brute.py "$TYPE" "$VAL1" "$VAL2" "$VAL3"
    break
    ;;
  esac
done
