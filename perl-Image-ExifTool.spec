#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Image
%define		pnam	ExifTool
Summary:	Perl module for reading and writing image metadata
Summary(pl.UTF-8):	Moduł Perla do czytania i zapisywania metadanych w plikach graficznych
Name:		perl-Image-ExifTool
Version:	12.65
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://exiftool.org/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f5a1368313cb3ab76933e45dd7b3f5b
URL:		https://exiftool.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Encode
%endif
Requires:	perl-Encode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExifTool is a customizable set of Perl modules for reading and writing
meta information in a wide variety of files, including the maker note
information of many digital cameras by various manufacturers such as
Canon, Casio, FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony.

%description -l pl.UTF-8
ExifTool to dostosowywalny zestaw modułów perlowych oraz aplikacja do
czytania i zapisywania metadanych w szerokiej gamie rodzajów plików.
ExifTool odczytuje również informacje dodatkowe o zdjęciach zapisywane
przez aparaty cyfrowe takich firm jak Canon, Casio, FujiFilm, GE, HP,
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo,
Sigma/Foveon i Sony.

%package -n exiftool
Summary:	Program for reading and writing EXIF metadata
Summary(pl.UTF-8):	Program do odczytu i zapisu metadanych Exif
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description -n exiftool
ExifTool is an application for reading and writing meta information in
a wide variety of files, including the maker note information of many
digital cameras by various manufacturers such as Canon, Casio,
FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta,
Nikon, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh,
Samsung, Sanyo, Sigma/Foveon and Sony.

%description -n exiftool -l pl.UTF-8
ExifTool to aplikacja do odczytu i zapisu metadanych w szerokoej gamie
rodzajów plików, w tym informacji dodatkowych o zdjęciach,
zapisywanych przez aparaty cyfrowe takich firm, jak Canon, Casio,
FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta,
Nikon, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh,
Samsung, Sanyo, Sigma/Foveon i Sony.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/File/RandomAccess.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Image/ExifTool{,/*}.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Image/ExifTool/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes html
%{perl_vendorlib}/File/RandomAccess.pm
%{perl_vendorlib}/Image/ExifTool.pm
%dir %{perl_vendorlib}/Image/ExifTool
%{perl_vendorlib}/Image/ExifTool/*.p[lm]
%dir %{perl_vendorlib}/Image/ExifTool/Charset
%{perl_vendorlib}/Image/ExifTool/Charset/*.pm
%dir %{perl_vendorlib}/Image/ExifTool/Lang
%lang(cs) %{perl_vendorlib}/Image/ExifTool/Lang/cs.pm
%lang(de) %{perl_vendorlib}/Image/ExifTool/Lang/de.pm
%lang(en_CA) %{perl_vendorlib}/Image/ExifTool/Lang/en_ca.pm
%lang(en_GB) %{perl_vendorlib}/Image/ExifTool/Lang/en_gb.pm
%lang(es) %{perl_vendorlib}/Image/ExifTool/Lang/es.pm
%lang(fi) %{perl_vendorlib}/Image/ExifTool/Lang/fi.pm
%lang(fr) %{perl_vendorlib}/Image/ExifTool/Lang/fr.pm
%lang(it) %{perl_vendorlib}/Image/ExifTool/Lang/it.pm
%lang(ja) %{perl_vendorlib}/Image/ExifTool/Lang/ja.pm
%lang(ko) %{perl_vendorlib}/Image/ExifTool/Lang/ko.pm
%lang(nl) %{perl_vendorlib}/Image/ExifTool/Lang/nl.pm
%lang(pl) %{perl_vendorlib}/Image/ExifTool/Lang/pl.pm
%lang(ru) %{perl_vendorlib}/Image/ExifTool/Lang/ru.pm
%lang(sk) %{perl_vendorlib}/Image/ExifTool/Lang/sk.pm
%lang(sv) %{perl_vendorlib}/Image/ExifTool/Lang/sv.pm
%lang(tr) %{perl_vendorlib}/Image/ExifTool/Lang/tr.pm
%lang(zh_CN) %{perl_vendorlib}/Image/ExifTool/Lang/zh_cn.pm
%lang(zh_TW) %{perl_vendorlib}/Image/ExifTool/Lang/zh_tw.pm
%{_mandir}/man3/File::RandomAccess.3pm*
%{_mandir}/man3/Image::ExifTool*.3pm*

%files -n exiftool
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exiftool
%{_mandir}/man1/exiftool.1p*
