#!/bin/bash
# this script gets the bit size of the HTTP response header for  the pass URL.
curl -s "$1" | wc -c
