Summary:	A General environment for the treatment of Discrete Problems
Summary(pl):	¦rodowisko do rozwi±zywania problemów dyskretnych
Name:		getdp
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://geuz.org/getdp/src/%{name}-%{version}-source.tgz
# Source0-md5:	5ed9b143d2205a7bbe5a13c91065593c
URL:		http://www.geuz.org/getdp/
BuildRequires:	gcc-g77
BuildRequires:	gsl-devel
BuildRequires:	texinfo
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GetDP is a scientific software environment for the numerical solution
of integro-differential equations, open to the coupling of physical
problems (electromagnetic, thermal, mechanical, etc) as well as of
numerical methods (finite element method, integral methods, etc). It
can deal with such problems of various dimensions (1D, 2D, 2D
axisymmetric or 3D) and time states (static, transient or harmonic).
The main feature of GetDP is the closeness between the organization of
data defining discrete problems (written by the user in ASCII data
files) and the symbolic mathematical expressions of these problems.

Install GetDP if you need a finite element solver for multiphysic
problems.

%description -l pl
GetDP jest naukowym ¶rodowiskiem do numerycznego rozwi±zywania równañ,
otwartym na ró¿ne fizyczne problemy(elektromagnetyczne, termiczne,
mechaniczne...), podobnie jak na metody numeryczne (metoda elementów
skoñczonych, metody ca³kowania...). Mo¿e rozwi±zywaæ problemy w ró¿nej
liczbie wymiarów (1D, 2D, 2D asymetryczne lub 3D), i ró¿nych stanach
czasu (statyczne, transakcyjne lub harmoniczne). G³ówn± w³asno¶ci±
GetDP jest blisko¶æ pomiêdzy organizacj± danych definiuj±cych problem
dyskretny (zapisane przez u¿ytkownika w plikach tekstowych) i
symbolicznymi wyra¿eniami matematycznymi tego problemu.

Warto zainstalowaæ GetDP je¿eli potrzebujemy narzêdzie do
obliczania elementów skoñczonych dla problemów fizycznych.

%prep
%setup -q

%build
%configure
%{__make}
%{__make} doc-info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_infodir}}

install -m 755 bin/getdp $RPM_BUILD_ROOT%{_bindir}/getdp
install doc/getdp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/texinfo/getdp.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/VERSIONS doc/FAQ doc/CREDITS demos
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_infodir}/%{name}*
