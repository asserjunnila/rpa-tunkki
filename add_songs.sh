#!/usr/bin/bash

# set exit immediately after errors
set -e

# print commands and arguments
set -x

# all assignments arguments are palced in the environment
set -k

# mark variables which are modified or created for export
set -a

## 2 args: the synctube room id and youtubeplaylist url
docker run --rm --name synctubeRPAtunkki rpa-tunkki:0.9 $@