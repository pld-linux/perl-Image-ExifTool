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
Version:	7.67
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Image/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4b60741cd725683eb11ae0866e5941e5
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
  3FR   r       HDP   r/w     PPM   r/w    |  EXIF           r/w/c
  ACR   r       HTML  r       PPT   r      |  GPS            r/w/c
  AI    r       ICC   r/w/c   PS    r/w    |  IPTC           r/w/c
  AIFF  r       ITC   r       PSD   r/w    |  XMP            r/w/c
  APE   r       JNG   r/w     QTIF  r      |  MakerNotes     r/w/c
  ARW   r       JP2   r/w     RA    r      |  Photoshop IRB  r/w/c
  ASF   r       JPEG  r/w     RAF   r/w    |  ICC Profile    r/w/c
  AVI   r       K25   r       RAM   r      |  MIE            r/w/c
  BMP   r       KDC   r       RAW   r/w    |  JFIF           r/w/c
  BTF   r       M4A   r       RIFF  r      |  Ducky APP12    r/w/c
  CR2   r/w     MEF   r/w     RW2   r      |  PDF            r/w/c
  CRW   r/w     MIE   r/w/c   RWZ   r      |  CIFF           r/w
  CS1   r/w     MIFF  r       RM    r      |  AFCP           r/w
  DCM   r       MNG   r/w     SO    r      |  JPEG 2000      r
  DCP   r/w     MOS   r/w     SR2   r      |  DICOM          r
  DCR   r       MOV   r       SRF   r      |  Flash          r
  DIVX  r       MP3   r       SVG   r      |  FlashPix       r
  DJVU  r       MP4   r       SWF   r      |  QuickTime      r
  DLL   r       MPC   r       THM   r/w    |  GeoTIFF        r
  DNG   r/w     MPG   r       TIFF  r/w    |  PrintIM        r
  DOC   r       MRW   r/w     VRD   r/w/c  |  ID3            r
  DYLIB r       NEF   r/w     WAV   r      |  Kodak Meta     r
  EPS   r/w     OGG   r       WDP   r/w    |  Ricoh RMETA    r
  ERF   r/w     ORF   r/w     WMA   r      |  Picture Info   r
  EXE   r       PBM   r/w     WMV   r      |  Adobe APP14    r
  EXIF  r/w/c   PDF   r/w     X3F   r      |  APE            r
  FLAC  r       PEF   r/w     XLS   r      |  Vorbis         r
  FLV   r       PGM   r/w     XMP   r/w/c  |  SPIFF          r
  FPX   r       PICT  r       ZIP   r      |  (and more)
  GIF   r/w     PNG   r/w

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
  3FR   r       HDP   r/w     PPM   r/w    |  EXIF           r/w/c
  ACR   r       HTML  r       PPT   r      |  GPS            r/w/c
  AI    r       ICC   r/w/c   PS    r/w    |  IPTC           r/w/c
  AIFF  r       ITC   r       PSD   r/w    |  XMP            r/w/c
  APE   r       JNG   r/w     QTIF  r      |  MakerNotes     r/w/c
  ARW   r       JP2   r/w     RA    r      |  Photoshop IRB  r/w/c
  ASF   r       JPEG  r/w     RAF   r/w    |  ICC Profile    r/w/c
  AVI   r       K25   r       RAM   r      |  MIE            r/w/c
  BMP   r       KDC   r       RAW   r/w    |  JFIF           r/w/c
  BTF   r       M4A   r       RIFF  r      |  Ducky APP12    r/w/c
  CR2   r/w     MEF   r/w     RW2   r      |  PDF            r/w/c
  CRW   r/w     MIE   r/w/c   RWZ   r      |  CIFF           r/w
  CS1   r/w     MIFF  r       RM    r      |  AFCP           r/w
  DCM   r       MNG   r/w     SO    r      |  JPEG 2000      r
  DCP   r/w     MOS   r/w     SR2   r      |  DICOM          r
  DCR   r       MOV   r       SRF   r      |  Flash          r
  DIVX  r       MP3   r       SVG   r      |  FlashPix       r
  DJVU  r       MP4   r       SWF   r      |  QuickTime      r
  DLL   r       MPC   r       THM   r/w    |  GeoTIFF        r
  DNG   r/w     MPG   r       TIFF  r/w    |  PrintIM        r
  DOC   r       MRW   r/w     VRD   r/w/c  |  ID3            r
  DYLIB r       NEF   r/w     WAV   r      |  Kodak Meta     r
  EPS   r/w     OGG   r       WDP   r/w    |  Ricoh RMETA    r
  ERF   r/w     ORF   r/w     WMA   r      |  Picture Info   r
  EXE   r       PBM   r/w     WMV   r      |  Adobe APP14    r
  EXIF  r/w/c   PDF   r/w     X3F   r      |  APE            r
  FLAC  r       PEF   r/w     XLS   r      |  Vorbis         r
  FLV   r       PGM   r/w     XMP   r/w/c  |  SPIFF          r
  FPX   r       PICT  r       ZIP   r      |  (and more)
  GIF   r/w     PNG   r/w

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
