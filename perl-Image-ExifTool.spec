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
Version:	7.76
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31bc4b453b0f8a1b9ccc91e0941e5ffd
URL:		http://www.sno.phy.queensu.ca/~phil/exiftool/
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
  3FR   r       HTML  r       PPT   r      |  EXIF           r/w/c
  ACR   r       ICC   r/w/c   PS    r/w    |  GPS            r/w/c
  AI    r       ITC   r       PSD   r/w    |  IPTC           r/w/c
  AIFF  r       JNG   r/w     QTIF  r      |  XMP            r/w/c
  APE   r       JP2   r/w     RA    r      |  MakerNotes     r/w/c
  ARW   r       JPEG  r/w     RAF   r/w    |  Photoshop IRB  r/w/c
  ASF   r       K25   r       RAM   r      |  ICC Profile    r/w/c
  AVI   r       KDC   r       RAW   r/w    |  MIE            r/w/c
  BMP   r       M4A   r       RIFF  r      |  JFIF           r/w/c
  BTF   r       MEF   r/w     RW2   r/w    |  Ducky APP12    r/w/c
  CR2   r/w     MIE   r/w/c   RWL   r/w    |  PDF            r/w/c
  CRW   r/w     MIFF  r       RWZ   r      |  CIFF           r/w
  CS1   r/w     MNG   r/w     RM    r      |  AFCP           r/w
  DCM   r       MOS   r/w     SO    r      |  JPEG 2000      r
  DCP   r/w     MOV   r       SR2   r      |  DICOM          r
  DCR   r       MP3   r       SRF   r      |  Flash          r
  DIVX  r       MP4   r       SVG   r      |  FlashPix       r
  DJVU  r       MPC   r       SWF   r      |  QuickTime      r
  DLL   r       MPG   r       THM   r/w    |  GeoTIFF        r
  DNG   r/w     MRW   r/w     TIFF  r/w    |  PrintIM        r
  DOC   r       NEF   r/w     VRD   r/w/c  |  ID3            r
  DYLIB r       NRW   r/w     WAV   r      |  Kodak Meta     r
  EPS   r/w     OGG   r       WDP   r/w    |  Ricoh RMETA    r
  ERF   r/w     ORF   r/w     WMA   r      |  Picture Info   r
  EXE   r       PBM   r/w     WMV   r      |  Adobe APP14    r
  EXIF  r/w/c   PDF   r/w     X3F   r      |  Panasonic MPF  r
  FLAC  r       PEF   r/w     XLS   r      |  APE            r
  FLV   r       PGM   r/w     XMP   r/w/c  |  Vorbis         r
  FPX   r       PICT  r       ZIP   r      |  SPIFF          r
  GIF   r/w     PNG   r/w                  |  DjVu           r
  HDP   r/w     PPM   r/w                  |  (and more)

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
  3FR   r       HTML  r       PPT   r      |  EXIF           r/w/c
  ACR   r       ICC   r/w/c   PS    r/w    |  GPS            r/w/c
  AI    r       ITC   r       PSD   r/w    |  IPTC           r/w/c
  AIFF  r       JNG   r/w     QTIF  r      |  XMP            r/w/c
  APE   r       JP2   r/w     RA    r      |  MakerNotes     r/w/c
  ARW   r       JPEG  r/w     RAF   r/w    |  Photoshop IRB  r/w/c
  ASF   r       K25   r       RAM   r      |  ICC Profile    r/w/c
  AVI   r       KDC   r       RAW   r/w    |  MIE            r/w/c
  BMP   r       M4A   r       RIFF  r      |  JFIF           r/w/c
  BTF   r       MEF   r/w     RW2   r/w    |  Ducky APP12    r/w/c
  CR2   r/w     MIE   r/w/c   RWL   r/w    |  PDF            r/w/c
  CRW   r/w     MIFF  r       RWZ   r      |  CIFF           r/w
  CS1   r/w     MNG   r/w     RM    r      |  AFCP           r/w
  DCM   r       MOS   r/w     SO    r      |  JPEG 2000      r
  DCP   r/w     MOV   r       SR2   r      |  DICOM          r
  DCR   r       MP3   r       SRF   r      |  Flash          r
  DIVX  r       MP4   r       SVG   r      |  FlashPix       r
  DJVU  r       MPC   r       SWF   r      |  QuickTime      r
  DLL   r       MPG   r       THM   r/w    |  GeoTIFF        r
  DNG   r/w     MRW   r/w     TIFF  r/w    |  PrintIM        r
  DOC   r       NEF   r/w     VRD   r/w/c  |  ID3            r
  DYLIB r       NRW   r/w     WAV   r      |  Kodak Meta     r
  EPS   r/w     OGG   r       WDP   r/w    |  Ricoh RMETA    r
  ERF   r/w     ORF   r/w     WMA   r      |  Picture Info   r
  EXE   r       PBM   r/w     WMV   r      |  Adobe APP14    r
  EXIF  r/w/c   PDF   r/w     X3F   r      |  Panasonic MPF  r
  FLAC  r       PEF   r/w     XLS   r      |  APE            r
  FLV   r       PGM   r/w     XMP   r/w/c  |  Vorbis         r
  FPX   r       PICT  r       ZIP   r      |  SPIFF          r
  GIF   r/w     PNG   r/w                  |  DjVu           r
  HDP   r/w     PPM   r/w                  |  (i inne)

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
%dir %{perl_vendorlib}/Image/ExifTool/Lang
%lang(cs) %{perl_vendorlib}/Image/ExifTool/Lang/cs.pm
%lang(de) %{perl_vendorlib}/Image/ExifTool/Lang/de.pm
%lang(en_CA) %{perl_vendorlib}/Image/ExifTool/Lang/en_ca.pm
%lang(en_GB) %{perl_vendorlib}/Image/ExifTool/Lang/en_gb.pm
%lang(es) %{perl_vendorlib}/Image/ExifTool/Lang/es.pm
%lang(fr) %{perl_vendorlib}/Image/ExifTool/Lang/fr.pm
%lang(it) %{perl_vendorlib}/Image/ExifTool/Lang/it.pm
%lang(ja) %{perl_vendorlib}/Image/ExifTool/Lang/ja.pm
%lang(ko) %{perl_vendorlib}/Image/ExifTool/Lang/ko.pm
%lang(nl) %{perl_vendorlib}/Image/ExifTool/Lang/nl.pm
%lang(pl) %{perl_vendorlib}/Image/ExifTool/Lang/pl.pm
%lang(ru) %{perl_vendorlib}/Image/ExifTool/Lang/ru.pm
%lang(sv) %{perl_vendorlib}/Image/ExifTool/Lang/sv.pm
%lang(tr) %{perl_vendorlib}/Image/ExifTool/Lang/tr.pm
%lang(zh_CN) %{perl_vendorlib}/Image/ExifTool/Lang/zh_cn.pm
%lang(zh_TW) %{perl_vendorlib}/Image/ExifTool/Lang/zh_tw.pm
%{_mandir}/man1/exiftool.1p*
%{_mandir}/man3/File::RandomAccess.3pm*
%{_mandir}/man3/Image::ExifTool*.3pm*
