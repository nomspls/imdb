# imdb movie ratings checker

* Script to check IMDB movie ratings with minimal GUI
* No API or scraping - once updated can be used offline
* Doesn't check unpopular titles (<10000 votes) 

![](demo.gif)

## How to use

```
	git clone https://github.com/nomspls/imdb.git
	cd imdb
	pip install -r requirements.txt # Kivy, pandas. (use conda if prefered)
	python update.py # Only needs to be run once or whenever you want to update
```
* Run app

```
	python imdb.py
```

## Built with

* Python 3.7
