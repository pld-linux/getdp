Summary:	A General environment for the treatment of Discrete Problems
Summary(pl.UTF-8):	Środowisko do rozwiązywania problemów dyskretnych
Name:		getdp
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Applications/Engineering
Source0:	http://geuz.org/getdp/src/%{name}-%{version}-source.tgz
# Source0-md5:	5f5d7cdaeaeea3dcd15ba900e9f7e896
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

%description -l pl.UTF-8
GetDP jest naukowym środowiskiem do numerycznego rozwiązywania równań,
otwartym na różne fizyczne problemy(elektromagnetyczne, termiczne,
mechaniczne...), podobnie jak na metody numeryczne (metoda elementów
skończonych, metody całkowania...). Może rozwiązywać problemy w różnej
liczbie wymiarów (1D, 2D, 2D asymetryczne lub 3D), i różnych stanach
czasu (statyczne, transakcyjne lub harmoniczne). Główną własnością
GetDP jest bliskość pomiędzy organizacją danych definiujących problem
dyskretny (zapisane przez użytkownika w plikach tekstowych) i
symbolicznymi wyrażeniami matematycznymi tego problemu.

Warto zainstalować GetDP jeżeli potrzebujemy narzędzie do
obliczania elementów skończonych dla problemów fizycznych.

%prep
%setup -q

%build
%configure
%{__make}
%{__make} doc-info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_infodir}}

install bin/getdp $RPM_BUILD_ROOT%{_bindir}/getdp
install doc/getdp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/texinfo/getdp.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/VERSIONS doc/FAQ doc/CREDITS demos README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_infodir}/%{name}*
