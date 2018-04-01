#! python3
# mcb.pyw - Saves and loads piece of text to the clipboard
# Usage - py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#   py.exe mcb.pyw - Loads <keyword>
#   py.exe mcb.pyw list - Loads all <keywords> to the clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
#TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
#TODO: List keywords and load content

mcbShelf.close()
