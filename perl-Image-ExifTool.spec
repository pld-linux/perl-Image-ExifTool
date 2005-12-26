#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	ExifTool
Summary:	Perl module for reading and writing image metadata
Summary(pl):	Modu³ Perla do czytania i zapisywania metadanych w plikach graficznych
Name:		perl-Image-ExifTool
Version:	5.87
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe0934e8994b9dbef82eb6dd2ef62954
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExifTool is a highly customizable set of Perl libraries plus an
application script for reading and writing meta information in images.

ExifTool reads EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile,
Photoshop IRB and ID3 meta information from JPG, JP2, TIFF, GIF, BMP,
PICT, QTIF, PNG, MNG, JNG, MIFF, PPM, PGM, PBM, XMP, EPS, PS, AI, PDF,
PSD, DCM, ACR, THM, CRW, CR2, MRW, NEF, PEF, ORF, RAF, SRF, MOS, X3F
and DNG images, MP3 and WAV audio files, and AVI, MOV and MP4 videos.
ExifTool also extracts information from the maker notes of many
digital cameras by various manufacturers including Canon, Casio,
FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and
Sigma/Foveon.

ExifTool writes EXIF, GPS, IPTC, XMP and MakerNotes meta information
to JPEG, TIFF, GIF, PPM, PGM, PBM, PNG, MNG, JNG, CRW, THM, CR2, MRW,
NEF, PEF, MOS and DNG images.

See html/index.html for more details about ExifTool features.

%description -l pl
ExifTool to wysoce dostosowywalny zestaw bibliotek perlowych oraz
aplikacja do czytania i zapisywania metadanych w plikach graficznych.

ExifTool potrafi odczytaæ metatagi EXIF, GPS, IPTC, XMP, JFIF,
GeoTIFF, ICC Profile, Photoshop IRB i ID3 z plików graficznych JPG,
JP2, TIFF, GIF, BMP, PICT, QTIF, PNG, MNG, JNG, MIFF, PPM, PGM, PBM,
XMP, EPS, PS, AI, PDF, PSD, DCM, ACR, THM, CRW, CR2, MRW, NEF, PEF,
ORF, RAF, SRF, MOS, X3F i DNG, z plików d¼wiêkowych MP3 i WAV oraz z
plików video AVI, MOV i MP4. ExifTool odczytuje równie¿ informacje
dodatkowe o zdjêciach zapisywane przez aparaty cyfrowe takich firm jak
Canon, Casio, FujiFilm, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Ricoh, Sanyo i Sigma/Foveon.

ExifTool potrafi zapisaæ metatagi EXIF, GPS, IPTC, XMP wraz z
informacjami dodatkowymi producenta do plików JPEG, TIFF, GIF, PPM,
PGM, PBM, PNG, MNG, JNG, CRW, THM, CR2, MRW, NEF, PEF i DNG.

Wiêcej informacji o mo¿liwo¶ciach pakietu ExifTool znajduje siê w
pliku html/index.html.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes html
%attr(755,root,root) %{_bindir}/exiftool
%{perl_vendorlib}/File/RandomAccess.pm
%{perl_vendorlib}/Image/ExifTool.pm
%dir %{perl_vendorlib}/Image/ExifTool
%{perl_vendorlib}/Image/ExifTool/*.p[lm]
%{_mandir}/man[13]/*
