NULL =

CONDITIONAL_APPLETS =

if CAIRO_MENU_MATE
CONDITIONAL_APPLETS += \
	mate-cairo-menu \
	$(NULL)
endif
if MATE_MENU
CONDITIONAL_APPLETS += \
	mate-mainmenu \
	$(NULL)
endif
if MATE_QUIT
CONDITIONAL_APPLETS += \
	mate-quit \
	$(NULL)
endif
if MATE_YAMA
CONDITIONAL_APPLETS += \
	mate-yama \
	$(NULL)
endif
if MATE_PANEL
CONDITIONAL_APPLETS += \
	mintmenu \
	$(NULL)
endif
# please keep alphabetized
SUBDIRS = \
	$(CONDITIONAL_APPLETS) \
	$(NULL)
# vim: set ts=8 sts=8 sw=8 :
