# jsonAnalytic


List all keys & all values in .json; [Windows, Linux, Mac]

## Features
Parsing json files by stdin and URL


[**Download latest version (Windows)**](https://github.com/raylan-oliveira/jsonAnalytic/releases/latest)
## Demo:
![Demon](https://raw.githubusercontent.com/raylan-oliveira/demos/main/demos/jsonAnalytic.gif)


### Dependencies
   ```sh
	pip install -r requeriments.txt
   ```
   
### Run
   ```sh
	python jsonAnalytic.py -f file.json # list all keys in file.json
	python jsonAnalytic.py -f file.json -k name url # list values keys [name, url] in file.json
    cat list_jsons.txt | jsonAnalytic.py # list all json keys from list_jsons.txt
    cat list_jsons.txt | jsonAnalytic.py -k url name # list all json values keys [url, name] from list_jsons.txt
   ```
	
### Compile - Windows & Linux & Mac
   ```sh
	pip install pyinstaller
	pyinstaller jsonAnalytic.py --onefile	   
   ```
