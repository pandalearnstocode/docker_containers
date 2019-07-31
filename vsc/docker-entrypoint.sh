#!/bin/bash
set -e

if [ $# -eq 0 ]
  then
    code-server1.1156-vsc1.33.1-linux-x64/code-server --allow-http --no-auth --data-dir /data /code
  else
    exec "$@"
fi