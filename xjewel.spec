Summary: An X Window System game of falling jewel blocks.
Name: xjewel
Version: 1.6
Release: 11
Copyright: MIT
Group: Amusements/Games
Source: ftp://ftp.x.org/R5contrib/xjewel-1.6.tar.z
Patch0: xjewel-1.6-imake.patch
Patch1: xjewel-1.6-enhance.patch
Patch2: xjewel-1.6-nobr.patch
BuildRoot: /var/tmp/xjewel-root

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
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/var/lib/games

make DESTDIR=$RPM_BUILD_ROOT install install.man

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xjewel <<EOF
xjewel name "xjewel"
xjewel description "Columns Game"
xjewel group Games/Video
xjewel exec "xjewel &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xjewel
%config /var/lib/games/xjewel.scores
/usr/X11R6/man/man1/xjewel.1x
%config /etc/X11/wmconfig/xjewel
