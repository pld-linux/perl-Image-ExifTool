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
Version:	8.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e9721ce9b8ff1e51ec679286b20c8802
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
  3FR   r       GZ    r       PEF   r/w    |  EXIF           r/w/c
  3G2   r       HDP   r/w     PGM   r/w    |  GPS            r/w/c
  3GP   r       HTML  r       PICT  r      |  IPTC           r/w/c
  ACR   r       ICC   r/w/c   PNG   r/w    |  XMP            r/w/c
  AI    r/w     IIQ   r       PPM   r/w    |  MakerNotes     r/w/c
  AIFF  r       IND   r/w     PPT   r      |  Photoshop IRB  r/w/c
  APE   r       ITC   r       PPTX  r      |  ICC Profile    r/w/c
  ARW   r       JNG   r/w     PS    r/w    |  MIE            r/w/c
  ASF   r       JP2   r/w     PSD   r/w    |  JFIF           r/w/c
  AVI   r       JPEG  r/w     QTIF  r      |  Ducky APP12    r/w/c
  BMP   r       K25   r       RA    r      |  PDF            r/w/c
  BTF   r       KDC   r       RAF   r/w    |  CIFF           r/w
  COS   r       KEY   r       RAM   r      |  AFCP           r/w
  CR2   r/w     LNK   r       RAW   r/w    |  JPEG 2000      r
  CRW   r/w     M2TS  r       RIFF  r      |  DICOM          r
  CS1   r/w     M4A/V r       RW2   r/w    |  Flash          r
  DCM   r       MEF   r/w     RWL   r/w    |  FlashPix       r
  DCP   r/w     MIE   r/w/c   RWZ   r      |  QuickTime      r
  DCR   r       MIFF  r       RM    r      |  GeoTIFF        r
  DIVX  r       MNG   r/w     SO    r      |  PrintIM        r
  DJVU  r       MOS   r/w     SR2   r      |  ID3            r
  DLL   r       MOV   r       SRF   r      |  Kodak Meta     r
  DNG   r/w     MP3   r       SVG   r      |  Ricoh RMETA    r
  DOC   r       MP4   r       SWF   r      |  Picture Info   r
  DOCX  r       MPC   r       THM   r/w    |  Adobe APP14    r
  DVB   r       MPG   r       TIFF  r/w    |  MPF            r
  DYLIB r       MPO   r/w     VRD   r/w/c  |  Stim           r
  EIP   r       MQV   r       WAV   r      |  APE            r
  EPS   r/w     MRW   r/w     WDP   r/w    |  Vorbis         r
  ERF   r/w     NEF   r/w     WMA   r      |  SPIFF          r
  EXE   r       NRW   r/w     WMV   r      |  DjVu           r
  EXIF  r/w/c   NUMBERS r     X3F   r      |  M2TS           r
  F4A/V r       OGG   r       XLS   r      |  PE/COFF        r
  FLAC  r       ORF   r/w     XLSX  r      |  AVCHD          r
  FLV   r       PAGES r       XMP   r/w/c  |  ZIP            r
  FPX   r       PBM   r/w     ZIP   r      |  (and more)
  GIF   r/w     PDF   r/w  

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
  3FR   r       GZ    r       PEF   r/w    |  EXIF           r/w/c
  3G2   r       HDP   r/w     PGM   r/w    |  GPS            r/w/c
  3GP   r       HTML  r       PICT  r      |  IPTC           r/w/c
  ACR   r       ICC   r/w/c   PNG   r/w    |  XMP            r/w/c
  AI    r/w     IIQ   r       PPM   r/w    |  MakerNotes     r/w/c
  AIFF  r       IND   r/w     PPT   r      |  Photoshop IRB  r/w/c
  APE   r       ITC   r       PPTX  r      |  ICC Profile    r/w/c
  ARW   r       JNG   r/w     PS    r/w    |  MIE            r/w/c
  ASF   r       JP2   r/w     PSD   r/w    |  JFIF           r/w/c
  AVI   r       JPEG  r/w     QTIF  r      |  Ducky APP12    r/w/c
  BMP   r       K25   r       RA    r      |  PDF            r/w/c
  BTF   r       KDC   r       RAF   r/w    |  CIFF           r/w
  COS   r       KEY   r       RAM   r      |  AFCP           r/w
  CR2   r/w     LNK   r       RAW   r/w    |  JPEG 2000      r
  CRW   r/w     M2TS  r       RIFF  r      |  DICOM          r
  CS1   r/w     M4A/V r       RW2   r/w    |  Flash          r
  DCM   r       MEF   r/w     RWL   r/w    |  FlashPix       r
  DCP   r/w     MIE   r/w/c   RWZ   r      |  QuickTime      r
  DCR   r       MIFF  r       RM    r      |  GeoTIFF        r
  DIVX  r       MNG   r/w     SO    r      |  PrintIM        r
  DJVU  r       MOS   r/w     SR2   r      |  ID3            r
  DLL   r       MOV   r       SRF   r      |  Kodak Meta     r
  DNG   r/w     MP3   r       SVG   r      |  Ricoh RMETA    r
  DOC   r       MP4   r       SWF   r      |  Picture Info   r
  DOCX  r       MPC   r       THM   r/w    |  Adobe APP14    r
  DVB   r       MPG   r       TIFF  r/w    |  MPF            r
  DYLIB r       MPO   r/w     VRD   r/w/c  |  Stim           r
  EIP   r       MQV   r       WAV   r      |  APE            r
  EPS   r/w     MRW   r/w     WDP   r/w    |  Vorbis         r
  ERF   r/w     NEF   r/w     WMA   r      |  SPIFF          r
  EXE   r       NRW   r/w     WMV   r      |  DjVu           r
  EXIF  r/w/c   NUMBERS r     X3F   r      |  M2TS           r
  F4A/V r       OGG   r       XLS   r      |  PE/COFF        r
  FLAC  r       ORF   r/w     XLSX  r      |  AVCHD          r
  FLV   r       PAGES r       XMP   r/w/c  |  ZIP            r
  FPX   r       PBM   r/w     ZIP   r      |  (and more)
  GIF   r/w     PDF   r/w  

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
