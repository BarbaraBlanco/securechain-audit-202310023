#!/bin/bash

DATA=$(date +"%Y%m%d_%H%M%S")

tar -czf backup_$DATA.tar.gz \
../usuarios \
../blockchain \
../auditoria

echo "Backup criado: backup_$DATA.tar.gz"
