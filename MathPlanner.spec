Summary:	A Program for calculating many kind of things
Summary(pl):	Program do ³atwego wykonywania obliczeñ matematycznych
Name:		MathPlanner
Version:	3.0.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://koti.mbnet.fi/jarmonik/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-opt.patch
URL:		http://koti.mbnet.fi/jarmonik
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MathPlanner is mathematical design and publishing tool. MathPlanner
supports complex numbers, vectors, and basic math operations like
trigonometry, log, ln... Also integers and functions definations can
be used.

%description -l pl
MathPlanner jest matematycznym programem do tworzenia i publikacji.
Obs³uguje liczby zespolone, wertory i podstawowe operacje matematyczne
(trygonometria, logarytmy,...). Mog± byæ tak¿e u¿yte liczby ca³kowite
oraz definicje funkcji.

%prep
%setup -q -n %{name}3-install
%patch0 -p1
%patch1 -p1

%build
CFLAGS="-I%{_prefix}/X11R6/include/qt"
LDFLAGS="-L/usr/X11R6/lib/qt/plugins-mt/styles/ -lqplatinumstyle -lqmotifstyle"
export LDFLAGS CFLAGS
%{__make} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" build

%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/usr/bin
#mkdir -p $RPM_BUILD_ROOT/opt/MathPlanner3

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install -s -m 755 MathPlanner3 $RPM_BUILD_ROOT/usr/bin/MathPlanner3
#cp -R Data/* $RPM_BUILD_ROOT/opt/MathPlanner3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Data/{Changes.txt,Doc.htm,MPLConfig.txt}
#/opt/MathPlanner3
#/usr/bin/MathPlanner3
