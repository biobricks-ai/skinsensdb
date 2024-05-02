#!/bin/bash

# read links from cache/01_invalidate/links.txt
links=$(cat cache/00_invalidate/links.txt)

# download files
for link in $links; do
    wget -P cache/01_download/ $link
done