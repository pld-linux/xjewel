Summary:	An X Window System game of falling jewel blocks
Summary(de):	Game von der Art von Segas COLUMNS
Summary(fr):	Jeu du style Columns de Sega
Summary(pl):	Gra pod X Window System - spadaj±ce bloki
Summary(tr):	Sega'nýn columns'una benzer oyun
Name:		xjewel
Version:	1.6
Release:	21
License:	MIT
Group:		X11/Applications/Games
Source0:	ftp://ftp.x.org/R5contrib/%{name}-%{version}.tar.z
# Source0-md5:	b6448726269ec158c5db6eb54864bdfe
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-imake.patch
Patch1:		%{name}-enhance.patch
Patch2:		%{name}-nobr.patch
Patch3:		%{name}-select.patch
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xjewel is an X Window System game much like Domain/Jewelbox, Sega's
Columns and/or Tetris. The point of the game is to move or rotate the
blocks as they fall, to get jewels in patterns of three when they come
to rest.

%description -l de
Jewel hat große Ähnlichkeit mit Domain/Jewelbox, einem Puzzle-Game in
der Tetris-Manier. Die Aufgabe besteht darin, die Bewegung der Blöcke
zu steuern, die vom oberen Bildschirmrand nach unten fallen. Man kann
sie nach links und nach rechts bewegen und die Segmente drehen. Der
Spieler versucht, möglichst viele Punkte einzuheimsen, bevor sein
Lebensfaden abgezwackt wird.

%description -l fr
jewel est un jeu comme Domain/Jewelbox qui est un jeu de puzzle de
style Tetris.

On y joue en contrôlant le déplacement des blocs qui tombent du haut
de l'écran. On peut les déplacer à droite et à gauche et les faire
tourner. Le but est d'avoir le plus de points possible avant que la
Faucheuse n'y mette un terme.

%description -l pl
Xjewel jest gr± pod X Window System podobn± do Domain/Jewelbox,
Columns znanej z Segi lub Tetrisa. Celem gry jest przesuwanie lub
rotacja bloków podczas spadania, aby u³o¿yæ sk³adaj±ce siê na nie
klejnoty w trójki w celu usuniêcia.

%description -l tr
Jewel, Domain/Jewelbox ya da Tetris benzeri bir bulmaca oyunudur. Amaç
düþen bloklarý saða/sola çevirerek ya da döndürerek uygun biçimde
yerleþtirmektir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	HSCORE_FILE=/var/games/xjewel.scores

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/var/games}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	HSCORE_FILE=/var/games/xjewel.scores

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(2755,root,games) %{_bindir}/xjewel
%{_mandir}/man1/xjewel.1x*
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/xjewel.scores
%{_desktopdir}/xjewel.desktop
%{_pixmapsdir}/*
