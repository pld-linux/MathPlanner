Summary:	A Program for calculating many kind of things
Summary(pl):	Program do ³atwego wykonywania obliczeñ matematycznych
Name:		MathPlanner
Version:	3.1.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://koti.mbnet.fi/jarmonik/%{name}-%{version}.tar.gz
# Source0-md5:	803a8de68056a4ec2e4c456b1ba9b320
Source1:	%{name}.desktop
Patch0:		%{name}-no_qstyles.patch
URL:		http://koti.mbnet.fi/jarmonik/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0

%build
QTDIR="%{_prefix}"
export QTDIR
cd src
for i in *.moc; do
	moc `basename $i .moc`.h >$i;
done
cd ..

rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/{mini,hicolor/{32x32,64x64}/mimetypes/},%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_datadir}/mimelnk/application/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/64x64/apps/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
install icons/64x64/mimetypes/*.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/64x64/mimetypes/
install icons/32x32/mimetypes/*.png $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/mimetypes/
install mpl2.desktop $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS Doc.htm Doc examples
%attr(755,root,root) %{_bindir}/*
%dir %{_mathdir}
%{_mathdir}/*.txt
%{_mathdir}/pixmaps/*
%{_mathdir}/ts/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/hicolor/*/mimetypes/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/*.desktop
