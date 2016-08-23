#!/usr/bin/python2.7
import urllib2, json
from pprint import pprint

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--pokemon-name", help="list pokemon name, or dex number", dest="pokemon_name")
parser.add_option("-t", "--type-only", help="list only the searched pokemon's type, only works with -p", dest="type_only", action="store_true")
parser.add_option("-m", "--moves-only", help="list only the searched pokemon's type, only works with -p", dest="moves_only", action="store_true")
parser.add_option("-T", "--type-info", help="list info on pokemon type. IE: water, dragons, etc", dest="type_info")
(options, args) = parser.parse_args()

print (options, args)

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
	elif options.moves_only is True:
		print moves_pretty
	else:
		print "Pokemon Name: {} \nPokedex Number: {}\nSprite URL: {}\nElement Types: {}\nMoves Able To Be Learned: {}".format(name, pokedex_id, sprite_url, element_string, moves_pretty)

def type_search(search, options):
	search_query = "http://pokeapi.co/api/v2/type/" + search + "/"
	request = urllib2.Request(search_query)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')
	opener = urllib2.build_opener()
	raw_output = opener.open(request).read()
	json_out = json.loads(raw_output)
	generation_origin = str(json_out['generation']['name'])
	half_from = []
	half_to = []
	none_to = []
	none_from = []
	double_from = []
	double_to = []
	for i in range(0, len(json_out['damage_relations']['half_damage_from'])):
		half_from.append(str(json_out['damage_relations']['half_damage_from'][i]['name']))
	for i in range(0, len(json_out['damage_relations']['half_damage_to'])):
		half_to.append(str(json_out['damage_relations']['half_damage_to'][i]['name']))
	for i in range(0, len(json_out['damage_relations']['no_damage_to'])):
		none_to.append(str(json_out['damage_relations']['no_damage_to'][i]['name']))
	for i in range(0, len(json_out['damage_relations']['no_damage_from'])):
		none_from.append(str(json_out['damage_relations']['no_damage_from'][i]['name']))
	for i in range(0, len(json_out['damage_relations']['double_damage_from'])):
		double_from.append(str(json_out['damage_relations']['double_damage_from'][i]['name']))
	for i in range(0, len(json_out['damage_relations']['double_damage_to'])):
		double_to.append(str(json_out['damage_relations']['double_damage_to'][i]['name']))
	move_damage_class = str(json_out['move_damage_class']['name'])
	moves_for_type = []
	for i in range(0, len(json_out['moves'][i]['name'])):
		moves_for_type.append(str(json_out['moves'][i]['name']))
	pkmn_ofType = []
	for i in range(0, len(json_out['pokemon'])):
		pkmn_ofType.append(str(json_out['pokemon'][i]['pokemon']['name']))
	half_from = ', '.join(map(str, half_from))
	half_to = ', '.join(map(str, half_to))
	none_to = ', '.join(map(str, none_to))
	none_from = ', '.join(map(str, none_from))
	double_from = ', '.join(map(str, double_from))
	double_to = ', '.join(map(str, double_to))
	moves_for_type = ', '.join(map(str, moves_for_type))
	pkmn_ofType = ', '.join(map(str, pkmn_ofType))	
	print "The combat type {} originated in {}\n".format(search, generation_origin)
	print "Damage Multiplier Info as of most current Gen:\nHalf From: {}\nHalf To: {}\nDouble From: {}\nDouble To: {}\nNone From: {}\nNone To: {}\nDamage class for moves: {}\n".format(half_from, half_to, double_from, double_to, none_from, none_to, move_damage_class)
	print "Moves Of {} type: {}\nPokemon Of Type: {}".format(search, moves_for_type, pkmn_ofType)


if options.pokemon_name is not None:
	if options.type_only is True and options.moves_only is True:
		print "Error, only one of -t or -m may be used at a time"
	else:
		pokemon_name(options.pokemon_name, options)
elif options.type_info is not None:
	type_search(options.type_info, options)