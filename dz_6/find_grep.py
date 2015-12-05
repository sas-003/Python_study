# coding: utf-8
import os, sys, argparse

parser = argparse.ArgumentParser(description='Find files and search strings.')
parser.add_argument("path", type=str,
                    help="Where to find?")
parser.add_argument("mask", type=str,
                    help="What file type to find?")
parser.add_argument("string", type=str,
                    help="What content to find?")
args = parser.parse_args()

path = args.path
mask = args.mask
string = args.string

def find(spath, smask):
	for file in os.listdir(spath):
		if file.endswith(smask):
			for i, line in enumerate(open(file)):
				yield file, i, line

def grep(sgen, sstring):
	for file, i, line in sgen:
		if line.count(sstring):
			yield file, i, line

gen = find(path,mask)

for a in grep(gen, string):
	print(a)