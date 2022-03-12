#!/usr/bin/bash

if [ -n "$1" ]; then
  jupytext --to notebook $1
  rm -i $1
else
  echo "Parameter not supplied."
fi
