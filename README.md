# Frogit (Make it French)
>Sublime Text plugin displaying in a popup the translation of the words selected with the multi-cursors. It uses a personnal EN/FR dictionary file that I maintain but you can use your own. I create this tool to help me to quickly find EN/FR translation without the hassle to open/search in a dictionary or personnal notes. Not found translations are added to the dictionary file for later manual translation (automatic translation is planned as the next development)

![click one word + right-click to translate](img/frogit_demo.png)

## Install

1. Copy into the package folder (C:\Users\<username>\AppData\Roaming\Sublime Text 3\Packages\Frogit)
  * frogit.py
  * context.sublime-menu

2. Copy ENGLISH_FRENCH.md in an easy accessible folder (you will often access it to change it and add yours translations...)

# Setup
In Frogit.py, set the path to your dictionary file:
  
```
dictionnary = r'C:\My\ENGLISH_FRENCH.md'
```

## Getting started

From any sublime tab, right-click an english word, then select 'FrogIt' command to get a popup with the french translation.

## License

MIT © [Nicolas Guinet](https://github.com/guinetn/)
