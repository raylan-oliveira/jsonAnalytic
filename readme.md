# jsonAnalytic


List all keys & all values in .json; [Windows, Linux, Mac]

## Features
Parsing json files by stdin and URL; Create a cache.json file from several parsed .json files


[**Download latest version (Windows)**](https://github.com/raylan-oliveira/jsonAnalytic/releases/latest)
## Demo:
![Demon](https://raw.githubusercontent.com/raylan-oliveira/demos/main/demos/jsonAnalytic.gif)

## Demo Cache:
![Demon](https://raw.githubusercontent.com/raylan-oliveira/demos/main/demos/jsonAnalytic_cache.gif)

### Dependencies
   ```sh
	pip install -r requeriments.txt
   ```
   
### Run
   ```sh
	python jsonAnalytic.py -i file.json # list all keys in file.json & create _file_cache.json
	python jsonAnalytic.py -i "https://aws.random.cat/meow?ref=apilist.fun" # list all keys in URL response & create _aws.random.cat_cache.json
	python jsonAnalytic.py -i file.json -k name url # list values keys [name, url] in file.json & create _name_url_cache.json
    cat list_jsons.txt | python jsonAnalytic.py -p # list all json keys from list_jsons.txt & create _stdin_cache.json
    cat list_jsons.txt | python jsonAnalytic.py -p -k url name # list all json values keys [url, name] from list_jsons.txt & create _stdin_cache.json
    cat list_urls_jsons.txt | python jsonAnalytic.py -p # list, using requests, all json keys from list_urls_jsons.txt & create _stdin_cache.json
    python jsonAnalytic.py -i _stdin_cache.json # list all keys in _stdin_cache.json // not using requests, not create cache 
   ```
	
### Compile - Windows & Linux & Mac
   ```sh
	pip install pyinstaller
	pyinstaller jsonAnalytic.py --onefile	   
   ```
