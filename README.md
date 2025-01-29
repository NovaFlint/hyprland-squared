# Hyprland squared

regular tiling window management is too cramped. i need one hundred workspaces. in a grid.

i gave it modal keyboard interaction, code templating, and a bit of visual flavor. they're pretty nice too.

this is made as a semi-flexible hyprland configuration.

## use

i made this for myself and decided to publish it. it is not maintained. you'll have to read and edit the code in order to use it.

you can pretty nicely add things to the source and rebuild it, or add things to the result.

*possibly* you can take some of this code outside of the structure it has here.

you will want a status bar that shows dynamic workspaces and current submap [such as waybar].

## dependencies
* hyprland
* ripgrep
* python [recent-ish]

## setup

```bash
cd <project-dir>
mkdir source result
git clone https://github.com/NovaFlint/hyprland-squared.git source
python source/build.py
Hyprland -c result/hyprland.conf
```
