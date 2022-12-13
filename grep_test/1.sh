#!      /usr/bin/bash

egrep  -r '.*?<\s*(to)[^>]*>\s*([A-Z][a-z]+)\s*<\s*/\1>\s*' 1.txt |
sed -r 's/<\s*(to)[^>]*>\s*([A-Z][a-z]+)\s*<\s*\/\1>/\2/g' |
sort -k 1 | 
uniq -c | 
sort -nr