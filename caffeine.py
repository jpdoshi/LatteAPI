#!/usr/bin/env python

from latteapi import cli
import argparse

desc = "Caffeine is CLI Utility for LatteAPI"
parser = argparse.ArgumentParser(description=desc)

parser.add_argument("-gm", "--model", help="Generate Model")
parser.add_argument("-gc", "--controller", help="Generate Controller")

args = parser.parse_args()

if args.model:
	cli.generate_model(args.model)

if args.controller:
	cli.generate_controller(args.controller)