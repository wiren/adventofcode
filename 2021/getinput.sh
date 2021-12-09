#! /bin/sh

SESSION=

if [ -z "$1" ]; then
  echo "Please provide number of day to fetch input for"
  exit 1
fi


curl "https://adventofcode.com/2021/day/$1/input" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://adventofcode.com/2021/day/2' -H 'Connection: keep-alive' -H "Cookie: _ga=GA1.2.1190483045.1638310582; _gid=GA1.2.1299817194.1638310582; session=${SESSION}; _gat=1" -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0' -H 'TE: Trailers' > day${1}.in
