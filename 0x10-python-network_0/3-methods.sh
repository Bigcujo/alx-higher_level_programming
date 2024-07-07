#!/bin/bash
# Displays all the HTTP methods the server of the passed URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
