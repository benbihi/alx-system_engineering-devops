#!/usr/bin/env bash
# puppet script

file {
ensure  => present,
content => "
#ssh config file
host*
IdentityFile ~/.ssh/school
PasswordAuthentication no
"
}
