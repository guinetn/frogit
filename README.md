# SublimeTranslator
>Sublime plugin that prefix selected words with their translation (EN->FR), then use ctrl-z to hide translation. It uses a FR/EN mapping file that a maintain. It help me to improve my translations.

## Install

Install `STH` with [Package Control](https://packagecontrol.io) and restart Sublime.

## Getting started

From any sublime tab, select some words to translate then CTRL+E+E or choose `lang_etof` in the Command Palette *(Cmd+Shift+P)*. This will then run the command in the active tab. 

### Keyboard shortcut

You can also set up a keyboard shortcut to run the command by opening up "Preferences > Key Bindings - User" and adding your shortcut with the `lang_etof` command.

Example:

```json
[
	{
		"keys": ["ctrl+e+e"],
		"command": "lang_etof"
	}
]
```

## License

MIT © [Nicolas Guinet](https://nicolasguinet.com)
