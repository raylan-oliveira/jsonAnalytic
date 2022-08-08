import requests									# pip install requests
import concurrent.futures
import argparse
import re
import sys
from collections import deque
from os.path import exists
fila = deque()

import json
from time import sleep

from os import mkdir

def dict_or_list(name_file,list_all, test_isinstance, all_keys_or_keys_search):
	
	if isinstance(test_isinstance, dict):	
		
		# for parse keys
		for key in test_isinstance.keys():
			
			if all_keys_or_keys_search == 'all_keys':
				if key not in list_all:
					print(key)
					list_all.append(key)
					value = test_isinstance[key]
					# insert_banco(name_file, key, value)
			elif key in all_keys_or_keys_search:
				dict_armazenar = {}
				dict_armazenar[key] = test_isinstance[key]
				if dict_armazenar not in list_all:
					print(test_isinstance[key])
					list_all.append(dict_armazenar)
			if isinstance(test_isinstance[key], dict) or isinstance(test_isinstance[key], list):
				if test_isinstance[key] not in fila:
					fila.append(test_isinstance[key])
				
	
	elif isinstance(test_isinstance, list):
		
		for item in test_isinstance:
			
			if isinstance(item, dict):
				
				for key in item.keys():
					
					if all_keys_or_keys_search == 'all_keys':
						if key not in list_all:
							print(key)
							value = item[key]
							# insert_banco(name_file, key, value)
							list_all.append(key)
					elif key in all_keys_or_keys_search:
						dict_armazenar = {}
						dict_armazenar[key] = item[key]
						if dict_armazenar not in list_all:	
							print(item[key])
							list_all.append(dict_armazenar)
					if isinstance(item[key], dict) or isinstance(item[key], list):
						if item[key] not in fila:
							fila.append(item[key])
						
			if isinstance(item, list):
				
				for item_list in item:
					
					if isinstance(item_list, dict):
						
						for key in item_list.keys():
							
							if all_keys_or_keys_search == 'all_keys':
								if key not in list_all:
									print(key)
									value = item_list[key]
									# insert_banco(name_file, key, value)
									list_all.append(key)
							elif key in all_keys_or_keys_search:
								dict_armazenar = {}
								dict_armazenar[key] = item_list[key]
								if dict_armazenar not in list_all:	
									print(item_list[key])
									list_all.append(dict_armazenar)									
							
	return list_all	
	
def show_all_keys(name_file,js):
	list_all_keys = []
	fila.append(js)	
	
	while len(fila) > 0:		
		
		element_fila = fila.popleft()		
		
		dict_or_list(name_file,list_all_keys, element_fila, 'all_keys')	

def show_all_values(name_file,js, list_keys_search):
	list_all_values = []
	fila.append(js)	
	
	while len(fila) > 0:
		
		element_fila = fila.popleft()
		dict_or_list(name_file,list_all_values, element_fila, list_keys_search)		

def ler_json(file):
	try:
		with open(file, 'r', encoding='utf8') as f:
			return json.load(f)
	except Exception as e:
		print(f'Error read file: {file}\n\tError: {e}')
		return 0

def file_or_url(argv, line_stdin, js):
	if len(argv) == 1:
		
		if js != 0:
			print(f'File: {line_stdin} - All Keys:')
			show_all_keys(line_stdin, js)
		else:
			pass
	
	else:
		if ('-k' in argv or '--keys_search' in argv):
			
			if js != 0:
				cont = 1
				for arg in argv:
					
					if '-k' in arg:
						cont_k = 0
						list_keys_search = []
						for arg_miss in range( len(argv) - cont ):
							list_keys_search.append(argv[cont + cont_k])
							
							cont_k += 1
						show_all_values(line_stdin,js, list_keys_search)				
						
						
					cont += 1
			else:
				pass
if __name__ == "__main__":	

	if '-f' not in sys.argv and '--file' not in sys.argv and '--help' not in sys.argv and '-h' not in sys.argv:
		
		for line_stdin in sys.stdin:
			
			line_stdin = line_stdin.replace('\n', '')
			# download url with json
			if re.search(r'^http', line_stdin):
				headers = {				
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
				}

				js = requests.get(line_stdin, headers=headers)
				
				file_or_url(sys.argv, line_stdin, js.json())
				
			else:
				js = ler_json(line_stdin)
				file_or_url(sys.argv, line_stdin, js)
	
	else:
		parser = argparse.ArgumentParser(description='jsonAnalytic - List all keys & all values in json')
		parser.add_argument("-f", "--file", help='File .json', required=True, type=str)
		parser.add_argument('-k', '--keys_search', help='keys search', required=False, type=str, default=None,  nargs='+')
		parser.add_argument('-a' , '--all_keys', help='show all keys', required=False, type=bool, default=True)
		
		args = parser.parse_args()			
		
		js = ler_json(args.file)
		if js != 0: 
			
			if args.keys_search != None:
				
				name_file = args.file
				show_all_values(name_file,js, args.keys_search)
			else:
				name_file = args.file
				show_all_keys(name_file,js)
		else:
			print(f'[{args.file}] - key not found')
			
			
		