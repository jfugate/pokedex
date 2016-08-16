#!/usr/bin/python2.7
import urllib2, json
from pprint import pprint

def pokemon_name(search):
	search_query = "http://pokeapi.co/api/v2/pokemon/" + search + "/"
	request = urllib2.Request(search_query)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')
	opener = urllib2.build_opener()
	raw_output = opener.open(request).read()
	json_out = json.loads(raw_output)
	name = str(json_out['name'])
	pokedex_id = str(json_out['id'])
	sprite_url = str(json_out['sprites']['front_default'])
	moves_learned = []
	element_types = []
	for i in range(0, len(json_out['moves'])):
		moves_learned.append(str(json_out['moves'][i]['move']['name']))
	for i in range(0, len(json_out['types'])):
		element_types.append(str(json_out['types'][i]['type']['name']))
	print name, pokedex_id, sprite_url, moves_learned, element_types

pokemon_name('raichu')
