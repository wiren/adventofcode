#! /bin/sh

if [ -z "$1" ]; then
  echo "Please enter day number"
  exit 1
fi

touch day${1}.intest
sed -e "s/X/${1}/" dayX.py > day${1}.py
chmod 755 day${1}.py
