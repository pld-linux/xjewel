Summary:	An X Window System game of falling jewel blocks
Summary(de):	Game von der Art von Segas COLUMNS 
Summary(fr):	Jeu du style Columns de Sega
Summary(tr):	Sega'n�n columns'una benzer oyun
Name:		xjewel
Version:	1.6
Release:	14
License:	MIT
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://ftp.x.org/R5contrib/%{name}-%{version}.tar.z
Source1:	xjewel.desktop
Source2:	xjewel.png
Patch0:		xjewel-imake.patch
Patch1:		xjewel-enhance.patch
Patch2:		xjewel-nobr.patch
Patch3:		xjewel-select.patch
Icon:		xjewel.gif
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xjewel is an X Window System game much like Domain/Jewelbox, Sega's
Columns and/or Tetris. The point of the game is to move or rotate the
blocks as they fall, to get jewels in patterns of three when they come
to rest.

%description -l de
Jewel hat gro�e �hnlichkeit mit Domain/Jewelbox, einem Puzzle-Game in
der Tetris-Manier. Die Aufgabe besteht darin, die Bewegung der Bl�cke
zu steuern, die vom oberen Bildschirmrand nach unten fallen. Man kann
sie nach links und nach rechts bewegen und die Segmente drehen. Der
Spieler versucht, m�glichst viele Punkte einzuheimsen, bevor sein
Lebensfaden abgezwackt wird.

%description -l fr
jewel est un jeu comme Domain/Jewelbox qui est un jeu de puzzle de
style Tetris.

On y joue en contr�lant le d�placement des blocs qui tombent du haut
de l'�cran. On peut les d�placer � droite et � gauche et les faire
tourner. Le but est d'avoir le plus de points possible avant que la
Faucheuse n'y mette un terme.

%description -l tr
Jewel, Domain/Jewelbox ya da Tetris benzeri bir bulmaca oyunudur. Ama�
d��en bloklar� sa�a/sola �evirerek ya da d�nd�rerek uygun bi�imde
yerle�tirmektir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
xmkmf
make	CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	HSCORE_FILE=/var/lib/games/xjewel.scores

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT/var/lib/games

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	HSCORE_FILE=/var/lib/games/xjewel.scores

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

#strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xjewel
%{_mandir}/man1/xjewel.1x.gz
%config /var/lib/games/xjewel.scores
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
