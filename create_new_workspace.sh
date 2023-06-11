#!/bin/bash

i3-msg "workspace $2; exec kitty -d $1; exec kitty -d $1 nvim"
