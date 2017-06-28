#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Gather our code in a main() function
def main():
  with open(sys.argv[1]) as f:
  	data = f.read()
  	data = data.replace('他','tmp')
  	data = data.replace('她','他')
  	data = data.replace('tmp','她')
  	data = data.replace('女','tmp')
  	data = data.replace('男','女')
  	data = data.replace('tmp','男')
  	print data
  


if __name__ == '__main__':
  main()