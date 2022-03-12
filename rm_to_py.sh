#!/usr/bin/bash

if [ -n "$1" ]; then
  jupytext --to py $1
  rm -i $1
else
  echo "Parameter not supplied."
fi
