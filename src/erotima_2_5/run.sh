#!/bin/bash

#open socat connection as a different process
#NOTE: we firstly install tor through the terminal (sudo apt install tor) and then connect with socat to the onion server through port 9050
socat tcp4-LISTEN:4242,reuseaddr,fork,keepalive,bind=127.0.0.1 SOCKS4a:127.0.0.1:zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion:80,socksport=9050 &
pid=$(echo "$!")
#attack for the 3rd query
echo "3rd QUERY"
bash ./hack3.sh 512 512 336 325
#attack for the 4th query
echo "4th QUERY"
python3 hack4.py

echo "5th QUERY"
#attack for the 5th query
python3 hack5.py

echo -e "\nAttacks done!"
kill $pid