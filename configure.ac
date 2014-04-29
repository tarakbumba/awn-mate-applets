AC_PREREQ(2.53)
AC_INIT([awn-mate-applets],
        [0.1.0],
        [https://github.com/tarakbumba/awn-mate-applets/issues])

AM_INIT_AUTOMAKE([-Wno-portability 1.8 tar-ustar])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR(applets)
AM_CONFIG_HEADER(config.h)
AM_MAINTAINER_MODE

AC_ISC_POSIX
AC_PROG_CC
AC_STDC_HEADERS
AC_PROG_LIBTOOL
DOLT

dnl ==============================================
dnl translation support
dnl ==============================================

GETTEXT_PACKAGE=awn-mate-applets
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE", [Gettext package])
ALL_LINGUAS="af ar ast bg ca cs csb da de en_CA en_GB en_US@piglatin es eu fi fr he hu id it ja ko lt ms nb nl nn pl pt pt_BR ru sk sv sv_SE th tr uk vi zh_CN zh_TW"

IT_PROG_INTLTOOL([0.34])
AM_GLIB_GNU_GETTEXT

INTLTOOL_SCHEMA_INI_RULE='%.schema-ini:	%.schema-ini.in $(INTLTOOL_MERGE) $(wildcard $(top_srcdir)/po/*.po) ; LC_ALL=C $(INTLTOOL_MERGE) -d -u -c $(top_builddir)/po/.intltool-merge-cache $(top_srcdir)/po $< [$]@'
AC_SUBST(INTLTOOL_SCHEMA_INI_RULE)

dnl
dnl Python script installation
dnl

AM_PATH_PYTHON(2.7)

dnl
dnl library support
dnl

AC_CHECK_LIB(m, round)

dnl
dnl package support
dnl

AC_ARG_WITH([gconf], AS_HELP_STRING([--without-gconf],[Disable building/installing applets that need GConf]),,[with_gconf=yes])
AC_ARG_WITH([mate-mainmenu], AS_HELP_STRING([--without-mate-mainmenu],[Disable building/installing Mate MainMenu applet]),,[with_mate_mainmenu=yes])
AC_ARG_WITH([mintmenu], AS_HELP_STRING([--without-mintmenu],[Disable building/installing MintMenu applet]),,[with_mintmenu=no])
AC_ARG_WITH([mate-cairo], AS_HELP_STRING([--without-mate-cairo],[Disable building/installing Mate Cairo Menu applet]),,[with_mate_cairo=yes])
AC_ARG_WITH([mate-yama], AS_HELP_STRING([--without-mate-yama],[Disable building/installing Mate Yama Menu applet]),,[with_mate_yama=yes])
AC_ARG_WITH([mate-yama], AS_HELP_STRING([--without-mate-quit],[Disable building/installing Mate Quit Desktop applet]),,[with_mate_quit=yes])
AM_CONDITIONAL(GCONF, test "$with_gconf" != "no")
AM_CONDITIONAL(MATE_MENU, test "$with_mate_mainmenu" != "no")
AM_CONDITIONAL(MATE_PANEL, test "$with_mintmenu" != "no")
AM_CONDITIONAL(CAIRO_MENU_MATE, test "$with_mate_cairo" != "no")
AM_CONDITIONAL(MATE_YAMA, test "$with_mate_yama" != "no")
AM_CONDITIONAL(MATE_QUIT, test "$with_mate_quit" != "no")

# all
PKG_CHECK_MODULES(AWN, [awn >= 0.3.9])
# mate-cairo-menu
PKG_CHECK_MODULES(LIBNOTIFY, [libnotify])
libsexy_required=no
url_label_module="gtk+-2.0 >= 2.17.1"
icon_entry_module="gtk+-2.0 >= 2.15.0"
if test "$with_gconf" != "no"; then
  PKG_CHECK_MODULES(GCONF, [gconf-2.0])
  gconf=gconf-2.0
fi

# mate-cairo-menu (IconEntry)
PKG_CHECK_EXISTS([$icon_entry_module],
                 [AC_DEFINE([HAVE_GTK_ICON_ENTRY], 1,
                            [Defined if GTK+ has support for icons in GtkEntrys])],
                 [libsexy_required=yes;icon_entry_module="libsexy"])
if test "$libsexy_required" != "no"; then
    PKG_CHECK_MODULES(LIBSEXY, [libsexy])
fi

if test "$with_mate_mainmenu" != "no"; then
# mate-mainmenu
PKG_CHECK_MODULES(MATE_MENU, [libmate-menu],
		  AM_CONDITIONAL(MATE_MENU,true),
		  AM_CONDITIONAL(MATE_MENU,false))

fi

if test "$with_mintmenu" != "no"; then
# mintmenu
PKG_CHECK_MODULES(MATE_PANEL, [libmatepanelapplet-4.0],
		  AM_CONDITIONAL(MATE_PANEL,true),
		  AM_CONDITIONAL(MATE_PANEL,false))
#AC_PATH_PROG(MINTMENU, mintmenu, no)
#    if test x"$MINTMENU" = xno; then
#        AC_MSG_ERROR([mintmenu executable not found in your path - should be installed])
#    fi
fi

# mate-cairo menu
if test "$with_mate_cairo" != "no"; then
PKG_CHECK_MODULES(CAIRO_MENU_MATE,
		  [$gconf libmate-menu libnotify $icon_entry_module],
		  AM_CONDITIONAL(CAIRO_MENU_MATE,true),
		  AM_CONDITIONAL(CAIRO_MENU_MATE,false))
fi

dnl
dnl Determine the location of lda-schema-to-gconf
dnl

LDA_BINDIR=`$PKG_CONFIG --variable=exec_prefix desktop-agnostic`/bin
AC_SUBST(LDA_BINDIR)

dnl
dnl Check the D-BUS version.
dnl

AC_MSG_CHECKING([dbus version])
DBUS_VERSION=`$PKG_CONFIG --modversion dbus-1`
DBUS_MAJOR_VER=`echo $DBUS_VERSION | cut -d. -f 1`
DBUS_MINOR_VER=`echo $DBUS_VERSION | cut -d. -f 2`
DBUS_MICRO_VER=`echo $DBUS_VERSION | cut -d. -f 3`

AC_MSG_RESULT($DBUS_VERSION)
AC_DEFINE_UNQUOTED(DBUS_MAJOR_VER, $DBUS_MAJOR_VER, [D-BUS major version.])
AC_DEFINE_UNQUOTED(DBUS_MINOR_VER, $DBUS_MINOR_VER, [D-BUS minor version.])
AC_DEFINE_UNQUOTED(DBUS_MICRO_VER, $DBUS_MICRO_VER, [D-BUS micro version.])

AC_DEFINE_UNQUOTED(DBUS_API_SUBJECT_TO_CHANGE, ,DBUS API is subject to change)

appletsdir="$datarootdir/avant-window-navigator/applets"

AS_AC_EXPAND(APPLETSDIR, $appletsdir)
AS_AC_EXPAND(SYSCONFDIR, $sysconfdir)
AS_AC_EXPAND(LIBDIR, $libdir)
AS_AC_EXPAND(datadir_intermediate, $datadir)
AS_AC_EXPAND(DATADIR, $datadir_intermediate)
AS_AC_EXPAND(LIBEXECDIR, $libexecdir)
AS_AC_EXPAND(localedir_intermediate, $localedir)
AS_AC_EXPAND(LOCALEDIR, $localedir_intermediate)

AC_DEFINE_UNQUOTED(APPLETSDIR, "$APPLETSDIR",
                   [The base directory for applet data and Python applets.])
AC_SUBST(APPLETSDIR)
AC_DEFINE_UNQUOTED(LOCALEDIR, "$LOCALEDIR", [Locale directory])
AC_SUBST(LOCALEDIR)
AC_DEFINE_UNQUOTED(LIBDIR, "$LIBDIR", [Lib directory])
AC_SUBST(LIBDIR)

DBUS_SERVICES_DIR=`$PKG_CONFIG --variable=session_bus_services_dir dbus-1`
AC_SUBST(DBUS_SERVICES_DIR)

if test "x$GCC" = "xyes"; then
        GCC_FLAGS="-g -Wall"
fi

AC_SUBST(GCC_FLAGS)

dnl ==============================================
dnl GConf
dnl ==============================================

AM_GCONF_SOURCE_2
if test "$enable_schemas_install" != "no"; then
  AC_PATH_PROG(GCONFTOOL, gconftool-2, no)
  if test x"$GCONFTOOL" = xno; then
    AC_MSG_ERROR([gconftool-2 executable not found in your path - should be installed with GConf])
  fi
fi

dnl Please keep in alphabetical order (directory, not applet)
AC_OUTPUT([
Makefile
applets/Makefile
applets/mate-cairo-menu/Makefile
applets/mate-cairo-menu/mate-cairo-menu.desktop.in
applets/mate-mainmenu/Makefile
applets/mate-mainmenu/mate-mainmenu.desktop.in
applets/mate-quit/Makefile
applets/mate-yama/Makefile
applets/mintmenu/Makefile
po/Makefile.in
shared/python/__init__.py
shared/python/Makefile
])

dnl -----------------------------------------------
dnl Result
dnl -----------------------------------------------
AC_MSG_RESULT([Configure finished
---------------------- summary -------------------------
         locales                : ${LOCALEDIR}
         appletsdir             : ${APPLETSDIR}
install gconf support           : $with_gconf
install mate mainmenu applet    : $with_mate_mainmenu
install mintmenu applet         : $with_mintmenu
install mate cairo menu applet  : $with_mate_cairo
install mate yama menu applet   : $with_mate_yama
install mate quit applet        : $with_mate_quit
---------------------------------------------------------])

echo
echo " Now type 'make' then 'make install' as root or 'make DESTDIR=/tmp install'"
echo

dnl -----------------------------------------------
dnl eof
