Summary:	A Program for calculating many kind of things
Summary(pl):	Program do �atwego wykonywania oblicze� matematycznych
Name:		MathPlanner3
Version:	3.0.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
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
Obs�uguje liczby zespolone, wertory i podstawowe operacje matematyczne
(trygonometria, logarytmy,...). Mog� by� tak�e u�yte liczby ca�kowite
oraz definicje funkcji.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="-I%{_prefix}/X11R6/include/qt" all

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
