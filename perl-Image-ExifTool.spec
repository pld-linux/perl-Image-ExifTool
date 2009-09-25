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
Version:	7.95
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81b0fdeac58665fb83c7225f9f1ec6b6
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
  3FR   r       ICC   r/w/c   PPM   r/w    |  EXIF           r/w/c
  ACR   r       IND   r/w     PPT   r      |  GPS            r/w/c
  AI    r/w     ITC   r       PS    r/w    |  IPTC           r/w/c
  AIFF  r       JNG   r/w     PSD   r/w    |  XMP            r/w/c
  APE   r       JP2   r/w     QTIF  r      |  MakerNotes     r/w/c
  ARW   r       JPEG  r/w     RA    r      |  Photoshop IRB  r/w/c
  ASF   r       K25   r       RAF   r/w    |  ICC Profile    r/w/c
  AVI   r       KDC   r       RAM   r      |  MIE            r/w/c
  BMP   r       M2TS  r       RAW   r/w    |  JFIF           r/w/c
  BTF   r       M4A   r       RIFF  r      |  Ducky APP12    r/w/c
  CR2   r/w     MEF   r/w     RW2   r/w    |  PDF            r/w/c
  CRW   r/w     MIE   r/w/c   RWL   r/w    |  CIFF           r/w
  CS1   r/w     MIFF  r       RWZ   r      |  AFCP           r/w
  DCM   r       MNG   r/w     RM    r      |  JPEG 2000      r
  DCP   r/w     MOS   r/w     SO    r      |  DICOM          r
  DCR   r       MOV   r       SR2   r      |  Flash          r
  DIVX  r       MP3   r       SRF   r      |  FlashPix       r
  DJVU  r       MP4   r       SVG   r      |  QuickTime      r
  DLL   r       MPC   r       SWF   r      |  GeoTIFF        r
  DNG   r/w     MPG   r       THM   r/w    |  PrintIM        r
  DOC   r       MPO   r/w     TIFF  r/w    |  ID3            r
  DYLIB r       MRW   r/w     VRD   r/w/c  |  Kodak Meta     r
  EPS   r/w     NEF   r/w     WAV   r      |  Ricoh RMETA    r
  ERF   r/w     NRW   r/w     WDP   r/w    |  Picture Info   r
  EXE   r       OGG   r       WMA   r      |  Adobe APP14    r
  EXIF  r/w/c   ORF   r/w     WMV   r      |  MPF            r
  FLAC  r       PBM   r/w     X3F   r      |  Stim           r
  FLV   r       PDF   r/w     XLS   r      |  APE            r
  FPX   r       PEF   r/w     XMP   r/w/c  |  Vorbis         r
  GIF   r/w     PGM   r/w     ZIP   r      |  SPIFF          r
  HDP   r/w     PICT  r                    |  DjVu           r
  HTML  r       PNG   r/w                  |  (and more)

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
