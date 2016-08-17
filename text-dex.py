#!/usr/bin/python2.7
import urllib2, json
from pprint import pprint

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--pokemon-name", help="list pokemon name, or dex number", dest="pokemon_name")
parser.add_option("-t", "--type-only", help="list only the searched pokemon's type, only works with -p", dest="type_only", action="store_true")
parser.add_option("-m", "--moves-only", help="list only the searched pokemon's type, only works with -p", dest="moves_only", action="store_true")
(options, args) = parser.parse_args()

#print (options, args)

def pokemon_name(search, options):
#	print "these are the function inherited options: {}".format(options)
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
	element_string = ', '.join(map(str, element_types))
	moves_pretty = '\n'.join(map(str, moves_learned))
	if options.type_only is True:
		print element_string
	if options.moves_only is True:
		print moves_pretty
	else:
		print "Pokemon Name: {} \nPokedex Number: {}\nSprite URL: {}\nElement Types: {}\nMoves Able To Be Learned: {}".format(name, pokedex_id, sprite_url, element_string, moves_pretty)

