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
Version:	7.30
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Image/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0afc347c6adebbc31e8bd28d70c48c00
URL:		http://search.cpan.org/dist/Image-ExifTool/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExifTool is a customizable set of Perl modules plus an application
script for reading and writing meta information in image, audio and
video files, including the maker note information of many digital
cameras by various manufacturers such as Canon, Casio, FujiFilm, HP,
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo, Sigma/Foveon and Sony.

Below is a list of file types and meta information formats currently
supported by ExifTool (r = read, w = write, c = create):

                File Types                 |    Meta Information
  ---------------------------------------  |  --------------------
  3FR   r       ITC   r       PPM   r/w    |  EXIF           r/w/c
  ACR   r       JNG   r/w     PPT   r      |  GPS            r/w/c
  AI    r       JP2   r/w     PS    r/w    |  IPTC           r/w/c
  AIFF  r       JPEG  r/w     PSD   r/w    |  XMP            r/w/c
  APE   r       K25   r       QTIF  r      |  MakerNotes     r/w/c
  ARW   r       KDC   r       RA    r      |  Photoshop IRB  r/w/c
  ASF   r       M4A   r       RAF   r/w    |  ICC Profile    r/w/c
  AVI   r       MEF   r/w     RAM   r      |  MIE            r/w/c
  BMP   r       MIE   r/w/c   RAW   r/w    |  JFIF           r/w/c
  BTF   r       MIFF  r       RIFF  r      |  Ducky APP12    r/w/c
  CR2   r/w     MNG   r/w     RM    r      |  CIFF           r/w
  CRW   r/w     MOS   r/w     SR2   r      |  AFCP           r/w
  CS1   r/w     MOV   r       SRF   r      |  JPEG 2000      r
  DCM   r       MP3   r       SVG   r      |  DICOM          r
  DCR   r       MP4   r       SWF   r      |  Flash          r
  DIVX  r       MPC   r       THM   r/w    |  FlashPix       r
  DNG   r/w     MPG   r       TIFF  r/w    |  QuickTime      r
  DOC   r       MRW   r/w     VRD   r/w/c  |  GeoTIFF        r
  EPS   r/w     NEF   r/w     WAV   r      |  PrintIM        r
  ERF   r/w     OGG   r       WDP   r/w    |  ID3            r
  FLAC  r       ORF   r/w     WMA   r      |  Kodak Meta     r
  FLV   r       PBM   r/w     WMV   r      |  Ricoh RMETA    r
  FPX   r       PDF   r/w     X3F   r      |  Picture Info   r
  GIF   r/w     PEF   r/w     XLS   r      |  Adobe APP14    r
  HDP   r/w     PGM   r/w     XMP   r/w/c  |  APE            r
  HTML  r       PICT  r                    |  Vorbis         r
  ICC   r/w/c   PNG   r/w                  |  (and more)

See html/index.html for more details about ExifTool features.

%description -l pl.UTF-8
ExifTool to dostosowywalny zestaw modułów perlowych oraz aplikacja
do czytania i zapisywania metadanych w plikach graficznych,
dźwiękowych i wideo. ExifTool odczytuje również informacje
dodatkowe o zdjęciach zapisywane przez aparaty cyfrowe takich firm
jak Canon, Casio, FujiFilm, HP, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Ricoh, Sanyo, Sigma/Foveon i Sony.

Lista formatów plików i metadanych obsługiwanych przez ExifTool
(r = odczyt, w = zapis, c = tworzenie):

              Formaty plików               |   Formaty metadanych
  ---------------------------------------  |  --------------------
  3FR   r       ITC   r       PPM   r/w    |  EXIF           r/w/c
  ACR   r       JNG   r/w     PPT   r      |  GPS            r/w/c
  AI    r       JP2   r/w     PS    r/w    |  IPTC           r/w/c
  AIFF  r       JPEG  r/w     PSD   r/w    |  XMP            r/w/c
  APE   r       K25   r       QTIF  r      |  MakerNotes     r/w/c
  ARW   r       KDC   r       RA    r      |  Photoshop IRB  r/w/c
  ASF   r       M4A   r       RAF   r/w    |  ICC Profile    r/w/c
  AVI   r       MEF   r/w     RAM   r      |  MIE            r/w/c
  BMP   r       MIE   r/w/c   RAW   r/w    |  JFIF           r/w/c
  BTF   r       MIFF  r       RIFF  r      |  Ducky APP12    r/w/c
  CR2   r/w     MNG   r/w     RM    r      |  CIFF           r/w
  CRW   r/w     MOS   r/w     SR2   r      |  AFCP           r/w
  CS1   r/w     MOV   r       SRF   r      |  JPEG 2000      r
  DCM   r       MP3   r       SVG   r      |  DICOM          r
  DCR   r       MP4   r       SWF   r      |  Flash          r
  DIVX  r       MPC   r       THM   r/w    |  FlashPix       r
  DNG   r/w     MPG   r       TIFF  r/w    |  QuickTime      r
  DOC   r       MRW   r/w     VRD   r/w/c  |  GeoTIFF        r
  EPS   r/w     NEF   r/w     WAV   r      |  PrintIM        r
  ERF   r/w     OGG   r       WDP   r/w    |  ID3            r
  FLAC  r       ORF   r/w     WMA   r      |  Kodak Meta     r
  FLV   r       PBM   r/w     WMV   r      |  Ricoh RMETA    r
  FPX   r       PDF   r/w     X3F   r      |  Picture Info   r
  GIF   r/w     PEF   r/w     XLS   r      |  Adobe APP14    r
  HDP   r/w     PGM   r/w     XMP   r/w/c  |  APE            r
  HTML  r       PICT  r                    |  Vorbis         r
  ICC   r/w/c   PNG   r/w                  |  (i inne)

Więcej informacji o możliwościach pakietu ExifTool znajduje się w
pliku html/index.html.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make} \
	CC="%{__cc}" \
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
