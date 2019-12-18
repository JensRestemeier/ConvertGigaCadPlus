# ConvertGigaCadPlus

## About Giga CAD Plus
[Giga Cad Plus](https://www.c64-wiki.de/wiki/3D-Konstruktion_mit_GIGA-CAD_Plus_auf_dem_C64/C128) is a simple modelling application for the Commodore 64, written by Stefan Vilsmeier. It was distributed as a Book with included Diskette by "Markt und Technik Verlag".  

It allows 3D modelling, and rendering into high-res images and short animations.

Unfortunately the only way to get a copy these days is on various second hand markets like eBay.

## Model files
Models are stored in files that begin with "ob." They can be extracted from .d64 disk images, or saved into plain directories with an emulator or a SD2IEC sd-card interfaced.

## Converting a model file
```console
$ python3 gigaCadToObj.py <model>
```
This will open a model file and write out an equivalent Wavefront .OBJ file.

For example
```console
$ python3 gigaCadToObj.py ob.schiff.seq
```
will convert ob.schiff.seq to schiff.obj.

## How to import converted files into Blender
During import I found best results by setting -Z as "up" vector:
[[/images/ObjImportOptions.png|Obj Import Options]]

The model will most likely be too big for the current "far" plane. Open the "View Properties" menu:
[[/images/ViewMenu.png|View Menu]]
and change the far plane to a larger value:
[[/images/ViewProperties.png|View Properties]]

You can then explore the model in the main view:
[[/images/Schiff.png|Ship Model]]

## CPC Giga CAD
There is a similar application called [Giga CAD](http://www.hutter1.net/gigacad/gigacad.htm) for Amstrad CPC that 
was published in [Happy Computer](http://www.cpcwiki.eu/index.php/CPC_Giga-CAD) magazine.

You can convert models with cpcGigaCadToObj
```console
$ python3 cpcGigaCadToObj.py <model>
```

For example
```console
$ python3 gigaCadToObj.py BRUECKE.OBJ
```
will convert BRUECKE.OBJ to BRUECKE_wf.obj.

## Other tools
There is another tool for Giga CAD written in C [giga-cad-obj](https://github.com/mrjoso/giga-cad-obj)
