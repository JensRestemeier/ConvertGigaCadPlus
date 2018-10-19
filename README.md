# ConvertGigaCadPlus

## About Giga Cad Plus
[Giga Cad Plus](https://www.c64-wiki.de/wiki/3D-Konstruktion_mit_GIGA-CAD_Plus_auf_dem_C64/C128) is a simple modelling application for the Commodore 64, written by Stefan Vilsmeier. It was distributed as a Book with Diskette by "Markt und Technik Verlag".  

It allows 3D modelling, and rendering of objects into "high-res" images or short animations.

Unfortunately the only way to get a copy these days is from various second hand markets like eBay.

## Model files
Models are stored in files that begin with "ob." They can be extracted from .d64 disk images, or saved into plain directories with an emulator or a [SD2IEC](https://www.c64-wiki.com/wiki/SD2IEC) interface.

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

![Obj Import Options](images/ObjImportOptions.png)

The model will most likely be too big for the current "far" plane. Open the "View Properties" menu:

![View Menu](https://raw.githubusercontent.com/JensRestemeier/ConvertGigaCadPlus/master//images/ViewMenu.png)

and change the far clip to a larger value:

![View Properties](https://raw.githubusercontent.com/JensRestemeier/ConvertGigaCadPlus/master//images/ViewProperties.png)

You can then explore the model in the main view:

![Ship Model](https://raw.githubusercontent.com/JensRestemeier/ConvertGigaCadPlus/master//images/Schiff.png)
