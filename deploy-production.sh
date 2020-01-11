#!/bin/bash

cat docker-login-password.txt | docker login repo.treescale.com --username thomas_michelet --password-stdin
ansible-playbook -i inventories/production deploy.yml