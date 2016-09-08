#!/usr/bin/python2.7

import sys, json, urllib2

"""this is a function for the text-dex.py
   this will provide the ability search functions
"""

def ability_search(search, options):
	search_query = "http://pokeapi.co/api/v2/ability/" + search + "/"
	request = urllib2.Request(search_query)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')
	opener = urllib2.build_opener()
	raw_output = opener.open(request).read()
	json_out = json.loads(raw_output)
	generation = json_out['generation']['name']
	pkmn_names = []
	is_hidden = []
	effect = json_out['effect_entries'][0]['effect']
	for i in range(0, len(json_out['pokemon'])):
		pkmn_names.append(str(json_out['pokemon'][i]['name']))
		is_hidden.append(str(json_out['pokemon'][i]['is_hidden']))
	hidden_mapping = {}
	for i in range(0, len(pkmn_names)):
		for n in range(0, len(is_hidden)):
			hidden_mapping_add = { i : n }
			hidden_mapping.update(hidden_mapping_add)
	if options.type_only is True:
		print element_string
	elif options.moves_only is True:
		print moves_pretty
	else: