#!/usr/bin/env python

# import necessary packages:
from latteapi import cli
import sys

# caffeine description:
description = "Caffeine is CLI Utility for LatteAPI"
print(description)

# get cli arguments:
args = sys.argv
del args[0]

# pass arguments to cli:
cli.setargs(args)