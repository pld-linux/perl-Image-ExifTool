#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	ExifTool
Summary:	Perl module for reading and writing image metadata
Summary(pl.UTF-8):	Moduł Perla do czytania i zapisywania metadanych w plikach graficznych
Name:		perl-Image-ExifTool
Version:	6.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c839c4d58b59bf18378a99ac4ea0861
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExifTool is a customizable set of Perl libraries plus an application
script for reading and writing meta information in image, audio and
video files.

ExifTool reads EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile,
Photoshop IRB, AFCP and ID3 meta information from JPG, JP2, TIFF, GIF,
BMP, PICT, QTIF, PNG, MNG, JNG, MIFF, PPM, PGM, PBM, XMP, EPS, PS, AI,
PDF, PSD, DCM, ACR, THM, CRW, CR2, MRW, NEF, PEF, ORF, RAF, RAW, SRF,
SR2, MOS, X3F and DNG images, MP3, WAV, WMA and AIFF audio files, and
AVI, MOV, MP4 and WMV videos. ExifTool also extracts information from
the maker notes of many digital cameras by various manufacturers
including Canon, Casio, FujiFilm, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

ExifTool writes EXIF, GPS, IPTC, XMP, MakerNotes, Photoshop IRB and
AFCP meta information to JPEG, TIFF, GIF, PSD, XMP, PPM, PGM, PBM,
PNG, MNG, JNG, CRW, THM, CR2, MRW, NEF, PEF, MOS and DNG images.

See html/index.html for more details about ExifTool features.

%description -l pl.UTF-8
ExifTool to dostosowywalny zestaw bibliotek perlowych oraz aplikacja
do czytania i zapisywania metadanych w plikach graficznych,
dźwiękowych i wideo.

ExifTool potrafi odczytać metatagi EXIF, GPS, IPTC, XMP, JFIF,
GeoTIFF, ICC Profile, Photoshop IRB, AFCP i ID3 z plików graficznych
JPG, JP2, TIFF, GIF, BMP, PICT, QTIF, PNG, MNG, JNG, MIFF, PPM, PGM,
PBM, XMP, EPS, PS, AI, PDF, PSD, DCM, ACR, THM, CRW, CR2, MRW, NEF,
PEF, ORF, RAF, RAW, SRF, SR2, MOS, X3F i DNG, z plików dźwiękowych
MP3, WAV, WMA i AIFF oraz z plików wideo AVI, MOV, MP4 i WMV. ExifTool
odczytuje również informacje dodatkowe o zdjęciach zapisywane przez
aparaty cyfrowe takich firm jak Canon, Casio, FujiFilm, JVC/Victor,
Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo i Sigma/Foveon.

ExifTool potrafi zapisać metatagi EXIF, GPS, IPTC, XMP, Photoshop IRB
i AFCP wraz z informacjami dodatkowymi producenta do plików JPEG,
TIFF, GIF, PSD, XMP, PPM, PGM, PBM, PNG, MNG, JNG, CRW, THM, CR2, MRW,
NEF, PEF, MOS i DNG.

Więcej informacji o możliwościach pakietu ExifTool znajduje się w
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
