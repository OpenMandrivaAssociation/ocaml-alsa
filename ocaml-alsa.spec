Name:           ocaml-alsa
Version:        0.1.4
Release:        %mkrel 1
Summary:        OCaml bindings for the ALSA library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/project/savonet/ocaml-alsa/%{version}/ocaml-alsa-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  libalsa-devel
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
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/alsa
make install

%clean
rm -rf %{buildroot}

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

