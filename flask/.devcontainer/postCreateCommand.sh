#!/bin/bash
set -x

git config --global --add safe.directory /workspaces/*

sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="xiong-chiamiov-plus"/' /root/.zshrc \
&& sed -i '/HIST_STAMPS="mm\/dd\/yyyy"/s/^#*//;s/mm\/dd\/yyyy/yyyy-mm-dd/' /root/.zshrc

zsh
