APPLET_NAME = mate-cairo-menu
MATE_MENU_BUILDER = mate-menu-builder

APPLET_CFLAGS = $(NULL)
if CAIRO_MENU_MATE
APPLET_CFLAGS += \
     $(CAIRO_MENU_MATE_FLAGS) \
     $(NULL)
endif
APPLET_CFLAGS +=				\
	-std=c99 \
	-D_GNU_SOURCE \
	$(NULL)

include $(top_srcdir)/Makefile.c-applet
include $(top_srcdir)/Makefile.schemas

mate_menu_builderdir = $(appletdir)

applet_LTLIBRARIES = mate-cairo-menu.la
mate_cairo_menu_la_SOURCES =	\
	applet.c				\
	cairo-menu-applet.c        \
	cairo-menu-applet.h        \
	cairo-main-icon.c       \
	cairo-main-icon.h       \
	cairo-aux-icon.c       \
	cairo-aux-icon.h       \
	misc.h                  \
	misc.c                  \
	$(NULL)
mate_cairo_menu_la_LIBADD =	\
	$(AWN_LIBS)				\
        $(NULL)
mate_cairo_menu_la_LDFLAGS = $(APPLET_LINKER_FLAGS)

mate_menu_builder_LTLIBRARIES = mate-menu-builder.la
mate_menu_builder_la_SOURCES =	\
	mate-menu-builder.h      \
	cairo-menu.c            \
	cairo-menu.h            \
	cairo-menu-item.c       \
	cairo-menu-item.h       \
	misc.h                  \
	misc.c                  \
	$(NULL)
mate_menu_builder_la_SOURCES += \
    mate-menu-builder.c \
    $(NULL)
mate_menu_builder_la_LIBADD =	\
    $(AWN_LIBS)				\
    $(NULL)
mate_menu_builder_la_LIBADD +=	\
    $(CAIRO_MENU_MATE_LIBS) \
    $(NULL)
mate_menu_builder_la_LDFLAGS = $(APPLET_LINKER_FLAGS)

