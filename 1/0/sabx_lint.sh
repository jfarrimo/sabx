#! /bin/bash

xmllint --noout --schema /home/jay/sabikerides/src/sabx/namespace/1/0/sabx.xsd $*
xmllint --noout --dtdvalid /home/jay/sabikerides/src/sabx/namespace/1/0/sabx.dtd $*
