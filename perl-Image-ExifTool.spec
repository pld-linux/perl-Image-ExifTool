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
Version:	7.99
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f397ee071a01104e6c68da43f3bdd372
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
  3FR   r       GIF   r/w     PGM   r/w    |  EXIF           r/w/c
  3G2   r       GZ    r       PICT  r      |  GPS            r/w/c
  3GP   r       HDP   r/w     PNG   r/w    |  IPTC           r/w/c
  ACR   r       HTML  r       PPM   r/w    |  XMP            r/w/c
  AI    r/w     ICC   r/w/c   PPT   r      |  MakerNotes     r/w/c
  AIFF  r       IIQ   r       PPTX  r      |  Photoshop IRB  r/w/c
  APE   r       IND   r/w     PS    r/w    |  ICC Profile    r/w/c
  ARW   r       ITC   r       PSD   r/w    |  MIE            r/w/c
  ASF   r       JNG   r/w     QTIF  r      |  JFIF           r/w/c
  AVI   r       JP2   r/w     RA    r      |  Ducky APP12    r/w/c
  BMP   r       JPEG  r/w     RAF   r/w    |  PDF            r/w/c
  BTF   r       K25   r       RAM   r      |  CIFF           r/w
  COS   r       KDC   r       RAW   r/w    |  AFCP           r/w
  CR2   r/w     LNK   r       RIFF  r      |  JPEG 2000      r
  CRW   r/w     M2TS  r       RW2   r/w    |  DICOM          r
  CS1   r/w     M4A/V r       RWL   r/w    |  Flash          r
  DCM   r       MEF   r/w     RWZ   r      |  FlashPix       r
  DCP   r/w     MIE   r/w/c   RM    r      |  QuickTime      r
  DCR   r       MIFF  r       SO    r      |  GeoTIFF        r
  DIVX  r       MNG   r/w     SR2   r      |  PrintIM        r
  DJVU  r       MOS   r/w     SRF   r      |  ID3            r
  DLL   r       MOV   r       SVG   r      |  Kodak Meta     r
  DNG   r/w     MP3   r       SWF   r      |  Ricoh RMETA    r
  DOC   r       MP4   r       THM   r/w    |  Picture Info   r
  DOCX  r       MPC   r       TIFF  r/w    |  Adobe APP14    r
  DVB   r       MPG   r       VRD   r/w/c  |  MPF            r
  DYLIB r       MPO   r/w     WAV   r      |  Stim           r
  EIP   r       MQV   r       WDP   r/w    |  APE            r
  EPS   r/w     MRW   r/w     WMA   r      |  Vorbis         r
  ERF   r/w     NEF   r/w     WMV   r      |  SPIFF          r
  EXE   r       NRW   r/w     X3F   r      |  DjVu           r
  EXIF  r/w/c   OGG   r       XLS   r      |  M2TS           r
  F4A/V r       ORF   r/w     XLSX  r      |  PE/COFF        r
  FLAC  r       PBM   r/w     XMP   r/w/c  |  AVCHD          r
  FLV   r       PDF   r/w     ZIP   r      |  ZIP            r
  FPX   r       PEF   r/w                  |  (and more)


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
  3FR   r       GIF   r/w     PGM   r/w    |  EXIF           r/w/c
  3G2   r       GZ    r       PICT  r      |  GPS            r/w/c
  3GP   r       HDP   r/w     PNG   r/w    |  IPTC           r/w/c
  ACR   r       HTML  r       PPM   r/w    |  XMP            r/w/c
  AI    r/w     ICC   r/w/c   PPT   r      |  MakerNotes     r/w/c
  AIFF  r       IIQ   r       PPTX  r      |  Photoshop IRB  r/w/c
  APE   r       IND   r/w     PS    r/w    |  ICC Profile    r/w/c
  ARW   r       ITC   r       PSD   r/w    |  MIE            r/w/c
  ASF   r       JNG   r/w     QTIF  r      |  JFIF           r/w/c
  AVI   r       JP2   r/w     RA    r      |  Ducky APP12    r/w/c
  BMP   r       JPEG  r/w     RAF   r/w    |  PDF            r/w/c
  BTF   r       K25   r       RAM   r      |  CIFF           r/w
  COS   r       KDC   r       RAW   r/w    |  AFCP           r/w
  CR2   r/w     LNK   r       RIFF  r      |  JPEG 2000      r
  CRW   r/w     M2TS  r       RW2   r/w    |  DICOM          r
  CS1   r/w     M4A/V r       RWL   r/w    |  Flash          r
  DCM   r       MEF   r/w     RWZ   r      |  FlashPix       r
  DCP   r/w     MIE   r/w/c   RM    r      |  QuickTime      r
  DCR   r       MIFF  r       SO    r      |  GeoTIFF        r
  DIVX  r       MNG   r/w     SR2   r      |  PrintIM        r
  DJVU  r       MOS   r/w     SRF   r      |  ID3            r
  DLL   r       MOV   r       SVG   r      |  Kodak Meta     r
  DNG   r/w     MP3   r       SWF   r      |  Ricoh RMETA    r
  DOC   r       MP4   r       THM   r/w    |  Picture Info   r
  DOCX  r       MPC   r       TIFF  r/w    |  Adobe APP14    r
  DVB   r       MPG   r       VRD   r/w/c  |  MPF            r
  DYLIB r       MPO   r/w     WAV   r      |  Stim           r
  EIP   r       MQV   r       WDP   r/w    |  APE            r
  EPS   r/w     MRW   r/w     WMA   r      |  Vorbis         r
  ERF   r/w     NEF   r/w     WMV   r      |  SPIFF          r
  EXE   r       NRW   r/w     X3F   r      |  DjVu           r
  EXIF  r/w/c   OGG   r       XLS   r      |  M2TS           r
  F4A/V r       ORF   r/w     XLSX  r      |  PE/COFF        r
  FLAC  r       PBM   r/w     XMP   r/w/c  |  AVCHD          r
  FLV   r       PDF   r/w     ZIP   r      |  ZIP            r
  FPX   r       PEF   r/w                  |  (and more)
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
