Name:           ocaml-alsa
Version:        0.2.0
Release:        4
Summary:        OCaml bindings for the ALSA library
License:        GPL
Group:          Development/Other
URL:            https://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/project/savonet/ocaml-alsa/%{version}/ocaml-alsa-%{version}.tar.gz
BuildRequires:  pkgconfig(alsa)
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
This OCaml library interfaces the ALSA library libasound to access audio
devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/alsa
make install

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/alsa
%{_libdir}/ocaml/alsa/META
%{_libdir}/ocaml/alsa/*.cma
%{_libdir}/ocaml/alsa/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_libdir}/ocaml/alsa/*.a
%{_libdir}/ocaml/alsa/*.cmxa
%{_libdir}/ocaml/alsa/*.cmx
%{_libdir}/ocaml/alsa/*.mli



%changelog
* Tue Oct 12 2010 Funda Wang <fwang@mandriva.org> 0.2.0-2mdv2011.0
+ Revision: 585098
- rebuild for new ocaml

* Mon Aug 23 2010 Florent Monnier <blue_prawn@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 572244
- updated to last version 0.2.0

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.4-1mdv2010.1
+ Revision: 496279
- update to new version 0.1.4

* Fri Aug 14 2009 Florent Monnier <blue_prawn@mandriva.org> 0.1.3-2mdv2010.0
+ Revision: 416245
- increm mkrel
- corrected buildrequires
- libasound is named libalsa
- BuildRequires libasound2
- import ocaml-alsa

