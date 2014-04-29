#!/usr/bin/env python2
# Copyright (C) 2010 neelance <mail@richard-musiol.de>
# Copyright (C) 2014 tarakbumba <tarakbumba at tarakbumba dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

# We need to import mintMenu module from non-standart directory
# And the module lays in different paths in different distros
import os
import sys

if os.path.isfile("/usr/lib/linuxmint/mintMenu/mintMenu.py"):
    sys.path.append('/usr/lib/linuxmint/mintMenu')
elif os.path.isfile("/usr/share/mintMenu/mintMenu.py"):
    sys.path.append('/usr/share/mintMenu')

from mintMenu import MenuWin
from awn.extras import awnlib
import mateapplet
import subprocess
import gtk

class MintMenuApplet:
    def __init__(self, applet):
        self.applet = applet
        self.window = self
        self.state = gtk.STATE_NORMAL
        
        menu = self.applet.dialog.menu
        menu_index = len(menu) - 1
        edit_menus_item = gtk.MenuItem(_("_Edit Menus"))
        edit_menus_item.connect("activate", self.show_menu_editor_cb)
        menu.insert(edit_menus_item, menu_index)
        menu.insert(gtk.SeparatorMenuItem(), menu_index + 1)

        MenuWin(self, None)

    def get_orient(self):
        orientation = self.applet.get_pos_type()
        if orientation == gtk.POS_BOTTOM:
            return mateapplet.ORIENT_UP
        elif orientation == gtk.POS_TOP:
            return mateapplet.ORIENT_DOWN
        elif orientation == gtk.POS_RIGHT:
            return mateapplet.ORIENT_LEFT
        elif orientation == gtk.POS_LEFT:
            return mateapplet.ORIENT_RIGHT
        
    def set_size_request(self, width, height):
        pass
    
    def add(self, widget):
        pass
    
    def set_applet_flags(self, flags):
        pass
    
    def connect(self, name, function):
        if name == "button-press-event":
            self.applet.connect("clicked", function)
    
    def get_origin(self):
        icon_x, icon_y = self.applet.window.get_origin()
        orientation = self.applet.get_pos_type()
        if orientation == gtk.POS_BOTTOM:
            return (icon_x, self.applet.get_screen().get_height() - self.applet.get_size() - self.applet.props.offset - 10)
        elif orientation == gtk.POS_TOP:
            return (icon_x, self.applet.props.offset)
        elif orientation == gtk.POS_RIGHT:
            return (self.applet.get_screen().get_width() - self.applet.get_size() - self.applet.props.offset - 10, icon_y)
        elif orientation == gtk.POS_LEFT:
            return (self.applet.props.offset, icon_y)
        return 

    def get_allocation(self):
        return gtk.gdk.Rectangle(0, 0, self.applet.get_size() + 10, self.applet.get_size() + 10)
    
    def set_state(self, state):
        self.state = state
        if state == gtk.STATE_SELECTED:
            self.autohide_cookie = self.applet.inhibit_autohide("showing main menu")
            self.applet.get_icon().set_is_active(True)
        if state == gtk.STATE_NORMAL:
            self.applet.uninhibit_autohide(self.autohide_cookie)
            self.applet.get_icon().set_is_active(False)

    def show_menu_editor_cb(self, widget):
        menu_editor_apps = ("mozo")
        for command in menu_editor_apps:
            try:
                subprocess.Popen(command)
                return
            except OSError:
                pass
        raise RuntimeError("No menu editor found (%s)" % ", ".join(menu_editor_apps))


if __name__ == "__main__":
    awnlib.init_start(MintMenuApplet, {"name": "Mint Menu",
        "short": "mintmenu",
        "version": "1.0.0",
        "description": "Mint Menu for AWN",
        "theme": "distributor-logo",
        "author": "neelance",
        "copyright-year": "2010",
        "author": "tarakbumba",
        "copyright-year": "2014",
        "authors": ["neelance <mail@richard-musiol.de>", "Linux Mint Team <www.linuxmint.com>"],
        "authors": ["tarakbumba <tarakbumba at tarakbumba dot com>"]},
        [])
