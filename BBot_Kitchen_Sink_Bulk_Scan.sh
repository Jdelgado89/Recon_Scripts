#!/bin/bash


# Get the File of Subdomains
read -e -p  "Where is the list of Subdomains?" file

Sub_Domains="$file"



if test -f "$Sub_Domains"; then
  echo "File exists."
else
  echo "File  Does not Exist"
  exit 1
fi

# Get the location of where you want to store the file
read -e -p  "Where do you want to save?" location


if test -d "$location"; then
  echo "Directory exists."
else
  echo "Does path does not exist."
  exit
fi

#Running BBOT
#Running BBOT

NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'



for I in  $(cat "$Sub_Domains"); do

    clear 
    echo -e  "\e[1;31m$I\e[0m"
    sleep 5
    bbot -t bbot -t $I -v -c modules.shodan_dns.api_key="HibJl2I1L6BwKmPICt3nrk7OgEHa0MAK" modules.hunterio.api_key="ed9496edd8dc09c6d9009bbf9c83bc710325113a" modules.censys.api_key="175314c3-06a4-4b18-a201-fbe41e5e052c" modules.censys.api_key="RZi66NUeDTX9G9zMZQxxBtDEPJOD9kbm" -p kitchen-sink -ef aggressive > "$location/$I_BBot.txt";

done


