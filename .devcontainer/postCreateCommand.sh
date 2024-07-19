#!/usr/bin/env bash

set -eou pipefail

########################################################################
# TODO: Give this script some proper hardening.  Probably don't need to
# go Google Bash Template, but certainly the basics.
########################################################################

# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

RED='\033[0;31m'
GREEN='\033[0;32m'
END='\033[0m'


echo -e "${GREEN}== ${RED}PostCreateCommand${GREEN} ==${END}"
env | sort
echo -e "${GREEN}================================================================================${END}"

# ==============================================================================
# Debugging passing variables into the script from the devcontainer.json
#
# From a terminal:
#  $ bash -c '.devcontainer/postCreateCommand.sh $@' scriptname one two three
#
# From the devcontainer.json:
# "postCreateCommand": [
#   "bash", "-c", "./.devcontainer/postCreateCommand.sh $*",
#   "<ignored>",
#   "${localWorkspaceFolder}"
#   "${containerWorkspaceFolder}"
#   "${localWorkspaceFolderBasename}"
#   "${containerWorkspaceFolderBasename}"
# ]
# ------------------------------------------------------------------------------
# Both of the above examples work with the logic below.  For more info about how
# arguments are passed and parsed from the devcontainer.json commands, see:
#   https://containers.dev/implementors/json_reference/#formatting-string-vs-array-properties
#
# In the postCreateCommand example above using $* vs. "$*", $@, or "$@" have
# differet behaviors.  Notice the terminal command example uses single qotes
# around the script and the postCreateCommand does not.
# ==============================================================================
echo -e "nArgs: $#"
echo -e "localWorkspaceFolder = ${1-<Missing>}"
echo -e "containerWorkspaceFolder = ${2-<Missing>}"
echo -e "localWorkspaceFolderBasename = ${3-<Missing>}"
echo -e "containerWorkspaceFolderBasename = ${4-<Missing>}"

echo -e "[${GREEN}*${END}] ${RED}All your postCreateCommand are belong to us${END}!"
