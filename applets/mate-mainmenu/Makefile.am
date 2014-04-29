APPLET_NAME = mate-mainmenu
APPLET_CFLAGS = $(MATE_MENU_CFLAGS)
include $(top_srcdir)/Makefile.c-applet

applet_LTLIBRARIES = mate-mainmenu.la
mate_mainmenu_la_SOURCES = applet.c
mate_mainmenu_la_LIBADD =		\
	$(AWN_LIBS)		\
	$(MATE_MENU_LIBS)	\
	$(NULL)
mate_mainmenu_la_LDFLAGS = $(APPLET_LINKER_FLAGS)
