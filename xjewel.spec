Summary:	An X Window System game of falling jewel blocks.
Name:		xjewel
Version:	1.6
Release:	11
Copyright:	MIT
Group:		Amusements/Games
Source:		ftp://ftp.x.org/R5contrib/%{name}-%{version}.tar.z
Patch0:		xjewel-1.6-imake.patch
Patch1:		xjewel-1.6-enhance.patch
Patch2:		xjewel-1.6-nobr.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xjewel is an X Window System game much like Domain/Jewelbox, Sega's
Columns and/or Tetris.  The point of the game is to move or rotate the
blocks as they fall, to get jewels in patterns of three when they come
to rest.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" \
	HSCORE_FILE=/var/state/games/xjewel.scores

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT/var/state/games

make install install.man DESTDIR=$RPM_BUILD_ROOT \
	HSCORE_FILE=/var/state/games/xjewel.scores

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xjewel <<EOF
xjewel name "xjewel"
xjewel description "Columns Game"
xjewel group Games/Video
xjewel exec "xjewel &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xjewel
%{_mandir}/man1/xjewel.1x.gz
%config /var/state/games/xjewel.scores
%config /etc/X11/wmconfig/xjewel
