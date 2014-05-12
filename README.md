=== AWN MATE APPLETS README FILE ===
====================================

These applets loosly based on awn-extras package applets and MintMenuAwn applet.
I have only modified necessary parts to use on MATE Desktop.

All credits should go to their respective authors. See AUTHORS file.

There are four applets in the package. Each applet has its own folder, and you
just need to enter it and do the usual:

./autogen.sh && make && sudo make install

By default, all applets, except mintmenu applet, will be installed.
You can exclude one of them from installation by issuing
	--without-FEATURE
command to ./autogen.sh script.

Currently mintmenu applet won't work. It should be migrated from pygtk to gi.

Note that i'm neither a programmer nor a bug hunter. I'm releasing this to share
with community but without WARRANTY.

Atilla ÖNTAŞ <tarakbumba> 2014
