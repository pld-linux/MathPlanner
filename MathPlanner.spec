Summary:	A Program for calculating many kind of things
Summary(pl):	Program do ³atwego wykonywania obliczeñ matematycznych
Name:		MathPlanner
Version:	3.0.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://koti.mbnet.fi/jarmonik/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-ac_fix.patch
URL:		http://koti.mbnet.fi/jarmonik
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mathdir	%{_datadir}/MathPlanner

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
%setup -q
%patch0 -p0

%build
QTDIR="/usr/X11R6"
export QTDIR

%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/mini,%{_applnkdir}/Scientific}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install icons/mini/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/mini
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS Doc.htm Doc examples
%attr(755,root,root) %{_bindir}/*
%dir %{_mathdir}
%{_mathdir}/*.txt
%{_mathdir}/pixmaps/*
%{_pixmapsdir}/*.xpm
%{_pixmapsdir}/mini/*.xpm
%{_applnkdir}/Scientific/*.desktop
