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
Version:	8.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ecf64a7e032de5d165eed1793d0ceac5
URL:		http://www.sno.phy.queensu.ca/~phil/exiftool/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Encode
%endif
Requires:	perl-Encode
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

  File Types
  ------------+-------------+-------------+-------------+------------
  3FR   r     | DOC   r     | K25   r     | PAGES r     | RWZ   r
  3G2   r     | DOCX  r     | KDC   r     | PBM   r/w   | RM    r
  3GP   r     | DVB   r     | KEY   r     | PDF   r/w   | SO    r
  ACR   r     | DYLIB r     | LNK   r     | PEF   r/w   | SR2   r/w
  AFM   r     | EIP   r     | M2TS  r     | PFA   r     | SRF   r
  AI    r/w   | EPS   r/w   | M4A/V r     | PFB   r     | SVG   r
  AIFF  r     | ERF   r/w   | MEF   r/w   | PFM   r     | SWF   r
  APE   r     | EXE   r     | MIE   r/w/c | PGM   r/w   | THM   r/w
  ARW   r/w   | EXIF  r/w/c | MIFF  r     | PICT  r     | TIFF  r/w
  ASF   r     | F4A/V r     | MNG   r/w   | PNG   r/w   | TTC   r
  AVI   r     | FLA   r     | MOS   r/w   | PPM   r/w   | TTF   r
  BMP   r     | FLAC  r     | MOV   r     | PPT   r     | VRD   r/w/c
  BTF   r     | FLV   r     | MP3   r     | PPTX  r     | WAV   r
  COS   r     | FPX   r     | MP4   r     | PS    r/w   | WDP   r/w
  CR2   r/w   | GIF   r/w   | MPC   r     | PSB   r/w   | WMA   r
  CRW   r/w   | GZ    r     | MPG   r     | PSD   r/w   | WMV   r
  CS1   r/w   | HDP   r/w   | MPO   r/w   | PSP   r     | X3F   r
  DCM   r     | HTML  r     | MQV   r     | QTIF  r     | XLS   r
  DCP   r/w   | ICC   r/w/c | MRW   r/w   | RA    r     | XLSX  r
  DCR   r     | IIQ   r     | NEF   r/w   | RAF   r/w   | XMP   r/w/c
  DFONT r     | IND   r/w   | NRW   r/w   | RAM   r     | ZIP   r
  DIVX  r     | ITC   r     | NUMBERS r   | RAW   r/w   |
  DJVU  r     | JNG   r/w   | OGG   r     | RIFF  r     |
  DLL   r     | JP2   r/w   | ORF   r/w   | RW2   r/w   |
  DNG   r/w   | JPEG  r/w   | OTF   r     | RWL   r/w   |

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  JPEG 2000      r    |  APE            r
  GPS            r/w/c  |  DICOM          r    |  Vorbis         r
  IPTC           r/w/c  |  Flash          r    |  SPIFF          r
  XMP            r/w/c  |  FlashPix       r    |  DjVu           r
  MakerNotes     r/w/c  |  QuickTime      r    |  M2TS           r
  Photoshop IRB  r/w/c  |  GeoTIFF        r    |  PE/COFF        r
  ICC Profile    r/w/c  |  PrintIM        r    |  AVCHD          r
  MIE            r/w/c  |  ID3            r    |  ZIP            r
  JFIF           r/w/c  |  Kodak Meta     r    |  (and more)
  Ducky APP12    r/w/c  |  Ricoh RMETA    r    |
  PDF            r/w/c  |  Picture Info   r    |
  CIFF           r/w    |  Adobe APP14    r    |
  AFCP           r/w    |  MPF            r    |
  PhotoMechanic  r/w    |  Stim           r    |

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

  Formaty plików
  ------------+-------------+-------------+-------------+------------
  3FR   r     | DOC   r     | K25   r     | PAGES r     | RWZ   r
  3G2   r     | DOCX  r     | KDC   r     | PBM   r/w   | RM    r
  3GP   r     | DVB   r     | KEY   r     | PDF   r/w   | SO    r
  ACR   r     | DYLIB r     | LNK   r     | PEF   r/w   | SR2   r/w
  AFM   r     | EIP   r     | M2TS  r     | PFA   r     | SRF   r
  AI    r/w   | EPS   r/w   | M4A/V r     | PFB   r     | SVG   r
  AIFF  r     | ERF   r/w   | MEF   r/w   | PFM   r     | SWF   r
  APE   r     | EXE   r     | MIE   r/w/c | PGM   r/w   | THM   r/w
  ARW   r/w   | EXIF  r/w/c | MIFF  r     | PICT  r     | TIFF  r/w
  ASF   r     | F4A/V r     | MNG   r/w   | PNG   r/w   | TTC   r
  AVI   r     | FLA   r     | MOS   r/w   | PPM   r/w   | TTF   r
  BMP   r     | FLAC  r     | MOV   r     | PPT   r     | VRD   r/w/c
  BTF   r     | FLV   r     | MP3   r     | PPTX  r     | WAV   r
  COS   r     | FPX   r     | MP4   r     | PS    r/w   | WDP   r/w
  CR2   r/w   | GIF   r/w   | MPC   r     | PSB   r/w   | WMA   r
  CRW   r/w   | GZ    r     | MPG   r     | PSD   r/w   | WMV   r
  CS1   r/w   | HDP   r/w   | MPO   r/w   | PSP   r     | X3F   r
  DCM   r     | HTML  r     | MQV   r     | QTIF  r     | XLS   r
  DCP   r/w   | ICC   r/w/c | MRW   r/w   | RA    r     | XLSX  r
  DCR   r     | IIQ   r     | NEF   r/w   | RAF   r/w   | XMP   r/w/c
  DFONT r     | IND   r/w   | NRW   r/w   | RAM   r     | ZIP   r
  DIVX  r     | ITC   r     | NUMBERS r   | RAW   r/w   |
  DJVU  r     | JNG   r/w   | OGG   r     | RIFF  r     |
  DLL   r     | JP2   r/w   | ORF   r/w   | RW2   r/w   |
  DNG   r/w   | JPEG  r/w   | OTF   r     | RWL   r/w   |

  Formaty metadanych
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  JPEG 2000      r    |  APE            r
  GPS            r/w/c  |  DICOM          r    |  Vorbis         r
  IPTC           r/w/c  |  Flash          r    |  SPIFF          r
  XMP            r/w/c  |  FlashPix       r    |  DjVu           r
  MakerNotes     r/w/c  |  QuickTime      r    |  M2TS           r
  Photoshop IRB  r/w/c  |  GeoTIFF        r    |  PE/COFF        r
  ICC Profile    r/w/c  |  PrintIM        r    |  AVCHD          r
  MIE            r/w/c  |  ID3            r    |  ZIP            r
  JFIF           r/w/c  |  Kodak Meta     r    |  (and more)
  Ducky APP12    r/w/c  |  Ricoh RMETA    r    |
  PDF            r/w/c  |  Picture Info   r    |
  CIFF           r/w    |  Adobe APP14    r    |
  AFCP           r/w    |  MPF            r    |
  PhotoMechanic  r/w    |  Stim           r    |

Więcej informacji o możliwościach pakietu ExifTool znajduje się w
pliku html/index.html.

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
%{perl_vendorlib}/Image/ExifTool/Charset/*.pm
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
