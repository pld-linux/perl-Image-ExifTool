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
Version:	8.48
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae1e34be6240b30997b0aaf604ef97a4
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
script for reading and writing meta information in a wide variety of
files, including the maker note information of many digital cameras by
various manufacturers such as Canon, Casio, FujiFilm, GE, HP,
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo,
Sigma/Foveon and Sony.

Below is a list of file types and meta information formats currently
supported by ExifTool (r = read, w = write, c = create):

  File Types
  ------------+-------------+-------------+-------------+------------
  3FR   r     | DVB   r     | M4A/V r     | PBM   r/w   | RWL   r/w
  3G2   r     | DYLIB r     | MEF   r/w   | PDF   r/w   | RWZ   r
  3GP   r     | EIP   r     | MIE   r/w/c | PEF   r/w   | RM    r
  ACR   r     | EPS   r/w   | MIFF  r     | PFA   r     | SO    r
  AFM   r     | ERF   r/w   | MKA   r     | PFB   r     | SR2   r/w
  AI    r/w   | EXE   r     | MKS   r     | PFM   r     | SRF   r
  AIFF  r     | EXIF  r/w/c | MKV   r     | PGF   r     | SRW   r/w
  APE   r     | F4A/V r     | MNG   r/w   | PGM   r/w   | SVG   r
  ARW   r/w   | FLA   r     | MOS   r/w   | PICT  r     | SWF   r
  ASF   r     | FLAC  r     | MOV   r     | PMP   r     | THM   r/w
  AVI   r     | FLV   r     | MP3   r     | PNG   r/w   | TIFF  r/w
  BMP   r     | FPX   r     | MP4   r     | PPM   r/w   | TTC   r
  BTF   r     | GIF   r/w   | MPC   r     | PPT   r     | TTF   r
  COS   r     | GZ    r     | MPG   r     | PPTX  r     | VRD   r/w/c
  CR2   r/w   | HDP   r/w   | MPO   r/w   | PS    r/w   | WAV   r
  CRW   r/w   | HTML  r     | MQV   r     | PSB   r/w   | WDP   r/w
  CS1   r/w   | ICC   r/w/c | MRW   r/w   | PSD   r/w   | WEBP  r
  DCM   r     | IIQ   r/w   | MXF   r     | PSP   r     | WEBM  r
  DCP   r/w   | IND   r/w   | NEF   r/w   | QTIF  r     | WMA   r
  DCR   r     | ITC   r     | NRW   r/w   | RA    r     | WMV   r
  DFONT r     | JNG   r/w   | NUMBERS r   | RAF   r/w   | X3F   r/w
  DIVX  r     | JP2   r/w   | ODP   r     | RAM   r     | XCF   r
  DJVU  r     | JPEG  r/w   | ODS   r     | RAR   r     | XLS   r
  DLL   r     | K25   r     | ODT   r     | RAW   r/w   | XLSX  r
  DNG   r/w   | KDC   r     | OGG   r     | RIFF  r     | XMP   r/w/c
  DOC   r     | KEY   r     | ORF   r/w   | RSRC  r     | ZIP   r
  DOCX  r     | LNK   r     | OTF   r     | RTF   r     |
  DV    r     | M2TS  r     | PAGES r     | RW2   r/w   |

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  Kodak Meta     r/w  |  Picture Info   r
  GPS            r/w/c  |  FotoStation    r/w  |  Adobe APP14    r
  IPTC           r/w/c  |  PhotoMechanic  r/w  |  MPF            r
  XMP            r/w/c  |  JPEG 2000      r    |  Stim           r
  MakerNotes     r/w/c  |  DICOM          r    |  APE            r
  Photoshop IRB  r/w/c  |  Flash          r    |  Vorbis         r
  ICC Profile    r/w/c  |  FlashPix       r    |  SPIFF          r
  MIE            r/w/c  |  QuickTime      r    |  DjVu           r
  JFIF           r/w/c  |  Matroska       r    |  M2TS           r
  Ducky APP12    r/w/c  |  GeoTIFF        r    |  PE/COFF        r
  PDF            r/w/c  |  PrintIM        r    |  AVCHD          r
  CIFF           r/w    |  ID3            r    |  ZIP            r
  AFCP           r/w    |  Ricoh RMETA    r    |  (and more)

See html/index.html for more details about ExifTool features.

%description -l pl.UTF-8
ExifTool to dostosowywalny zestaw modułów perlowych oraz aplikacja do
czytania i zapisywania metadanych w szerokiej gamie rodzajów plików.
ExifTool odczytuje również informacje dodatkowe o zdjęciach zapisywane
przez aparaty cyfrowe takich firm jak Canon, Casio, FujiFilm, GE, HP,
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson,
Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo,
Sigma/Foveon i Sony.

Lista formatów plików i metadanych obsługiwanych przez ExifTool
(r = odczyt, w = zapis, c = tworzenie):

  Formaty plików
  ------------+-------------+-------------+-------------+------------
  3FR   r     | DVB   r     | M4A/V r     | PBM   r/w   | RWL   r/w
  3G2   r     | DYLIB r     | MEF   r/w   | PDF   r/w   | RWZ   r
  3GP   r     | EIP   r     | MIE   r/w/c | PEF   r/w   | RM    r
  ACR   r     | EPS   r/w   | MIFF  r     | PFA   r     | SO    r
  AFM   r     | ERF   r/w   | MKA   r     | PFB   r     | SR2   r/w
  AI    r/w   | EXE   r     | MKS   r     | PFM   r     | SRF   r
  AIFF  r     | EXIF  r/w/c | MKV   r     | PGF   r     | SRW   r/w
  APE   r     | F4A/V r     | MNG   r/w   | PGM   r/w   | SVG   r
  ARW   r/w   | FLA   r     | MOS   r/w   | PICT  r     | SWF   r
  ASF   r     | FLAC  r     | MOV   r     | PMP   r     | THM   r/w
  AVI   r     | FLV   r     | MP3   r     | PNG   r/w   | TIFF  r/w
  BMP   r     | FPX   r     | MP4   r     | PPM   r/w   | TTC   r
  BTF   r     | GIF   r/w   | MPC   r     | PPT   r     | TTF   r
  COS   r     | GZ    r     | MPG   r     | PPTX  r     | VRD   r/w/c
  CR2   r/w   | HDP   r/w   | MPO   r/w   | PS    r/w   | WAV   r
  CRW   r/w   | HTML  r     | MQV   r     | PSB   r/w   | WDP   r/w
  CS1   r/w   | ICC   r/w/c | MRW   r/w   | PSD   r/w   | WEBP  r
  DCM   r     | IIQ   r/w   | MXF   r     | PSP   r     | WEBM  r
  DCP   r/w   | IND   r/w   | NEF   r/w   | QTIF  r     | WMA   r
  DCR   r     | ITC   r     | NRW   r/w   | RA    r     | WMV   r
  DFONT r     | JNG   r/w   | NUMBERS r   | RAF   r/w   | X3F   r/w
  DIVX  r     | JP2   r/w   | ODP   r     | RAM   r     | XCF   r
  DJVU  r     | JPEG  r/w   | ODS   r     | RAR   r     | XLS   r
  DLL   r     | K25   r     | ODT   r     | RAW   r/w   | XLSX  r
  DNG   r/w   | KDC   r     | OGG   r     | RIFF  r     | XMP   r/w/c
  DOC   r     | KEY   r     | ORF   r/w   | RSRC  r     | ZIP   r
  DOCX  r     | LNK   r     | OTF   r     | RTF   r     |
  DV    r     | M2TS  r     | PAGES r     | RW2   r/w   |

  Formaty metadanych
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  Kodak Meta     r/w  |  Picture Info   r
  GPS            r/w/c  |  FotoStation    r/w  |  Adobe APP14    r
  IPTC           r/w/c  |  PhotoMechanic  r/w  |  MPF            r
  XMP            r/w/c  |  JPEG 2000      r    |  Stim           r
  MakerNotes     r/w/c  |  DICOM          r    |  APE            r
  Photoshop IRB  r/w/c  |  Flash          r    |  Vorbis         r
  ICC Profile    r/w/c  |  FlashPix       r    |  SPIFF          r
  MIE            r/w/c  |  QuickTime      r    |  DjVu           r
  JFIF           r/w/c  |  Matroska       r    |  M2TS           r
  Ducky APP12    r/w/c  |  GeoTIFF        r    |  PE/COFF        r
  PDF            r/w/c  |  PrintIM        r    |  AVCHD          r
  CIFF           r/w    |  ID3            r    |  ZIP            r
  AFCP           r/w    |  Ricoh RMETA    r    |  (and more)

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
%dir %{perl_vendorlib}/Image/ExifTool/Charset
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
