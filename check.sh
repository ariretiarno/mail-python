#!/bin/bash

for i in $(ecs-cli ps --cluster Goteam-production | awk '{print $3}' | grep -vE 'Ports|cron' | cut -d':' -f1 ); do
  echo "================== "
  echo "$i"
  echo "================== "
  FORB=403
  TMP=$(curl -v --silent http://$i --stderr - | grep -Ei "403 Forbidden" | awk '{print $2}')
  if [[ $TMP == *$FORB* ]]; then
    echo $TMP
    docker run -dti --rm -e MAIL=geekseatdevops@gmail.com -e PASS=cSeh3YFusX2Vfo -e RECEIVER=risman.ramadhan@geekseat.com.au -e IP="$i" catalysthub/mail-python
  else
    echo "no threat"
  fi
  echo -e "\n"
done