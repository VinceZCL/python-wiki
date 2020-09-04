#! python3

import sys
import webbrowser

url = "https://en.wikipedia.org/wiki/"

if len(sys.argv) == 1:
    wiki_url = url + "Main_Page"

elif len(sys.argv) > 1:
	args = [arg.capitalize() for arg in sys.argv[1:]]
	search = "_".join(args)
	wiki_url = url + search

webbrowser.open(wiki_url)
