#!/usr/bin/env python

import argparse

desc = "Caffeine is CLI Utility for LatteAPI"
parser = argparse.ArgumentParser(description=desc)

parser.add_argument("-m", "--model", help="Generate Model")
parser.add_argument("-c", "--controller", help="Generate Controller")

args = parser.parse_args()

if args.model:
	print("Adding Model:" + args.model)

if args.controller:
	print("Adding Model:" + args.controller)