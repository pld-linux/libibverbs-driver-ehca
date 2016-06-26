Summary:	Userspace driver for IBM InfiniBand HCA (ehca)
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla urządzeń IBM InfiniBand HCA (ehca)
Name:		libibverbs-driver-ehca
Version:	1.2.2
%define	snap	20100526
%define	gitref	g69e1a88
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/libehca/libehca-%{version}-0.1.%{gitref}.tar.gz
# Source0-md5:	c27c5dfb3519de7c29d55286f58e05e7
URL:		http://openib.org/
BuildRequires:	libibverbs-devel >= 1.1
# IBM pSeries only
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libehca is a userspace driver for IBM InfiniBand HCA (ehca). It works
as a plug-in module for libibverbs that allows programs to use IBM
InfiniBand HCA hardware directly from userspace.

%description -l pl.UTF-8
libehca to sterownik przestrzeni użytkownika dla urządzeń IBM
InfiniBand HCA (ehca). Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do
sprzętu IBM InfiniBand HCA.

%package static
Summary:	Static version of ehca driver
Summary(pl.UTF-8):	Statyczna wersja sterownika ehca
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of ehca driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika ehca, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libehca-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libehca.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README README
%attr(755,root,root) %{_libdir}/libehca-rdmav2.so
%{_sysconfdir}/libibverbs.d/ehca.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libehca.a
