#!/bin/bash
FILENAME="firefox.log.gz.gpg"
for i in {0..756}; do
    VAR=$(date -I -d "2021-01-01 +$i days")
    NEWVAR=$VAR" bigtent"
    HASH=$(echo -n $NEWVAR|sha256sum)
    FINAL=$(echo $HASH | head -c 64)
    echo $NEWVAR
    gpg -d --pinentry-mode loopback --passphrase=$FINAL $FILENAME 
done 