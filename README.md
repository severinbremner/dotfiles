dotfiles
========

Config files from ~/

## Installation

```
cd dotfiles
./install
```

This script will backup your old dotfiles to ~/dotfiles-$DATE and create
symbolic links in your home directory to these config files.

## Notes

If you're new to tmux from screen and miss:
```
  screen -DRR
```
use:
```
  tmux -2 a -d || tmux -2 new
```
(-2 forces 256 colors)

" vim:ft=mkd
