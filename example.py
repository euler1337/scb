#!/usr/bin/env python
#-*- coding: utf-8 -*-

from scb import SCB
import json
import ast

def main():
	""" This is an example of how SCB module can be used to access data. 
	"""

	print("Hello world!")
	scb_handle = SCB()
	SCB.get_overview(scb_handle)

	# Navigate to dataset
	SCB.select(scb_handle, 'TK')
	SCB.select(scb_handle, 'TK1001')
	SCB.select(scb_handle, 'TK1001A')
	
	# Use below for a CLI
	#SCB.filter_table(scb_handle, 'PersBilarDrivMedel')

	# Use below for programatic interface:

	# Add desired filters
	#filt = {'Region' : ['00'], 'Drivmedel' : ['120'], 'Tid' : ['2017M09']}
	filt = {'Region' : ['00'], 'Drivmedel' : ['120']}
	
	# Fetch data in json format
	r = SCB.download_table(scb_handle, 'PersBilarDrivMedel','csv', filt)

	# Do magic with data ...
	print r.encoding
	print r.status_code
	print r.headers

	print r.text 

	#TODO: Why does not r.json() Work? because of å/ä/ö in response???

if __name__ == "__main__":
	main()
