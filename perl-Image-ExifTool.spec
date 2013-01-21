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
Version:	9.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45e1cde019f2bd484a2d9ce1859d99ee
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

# awk -vname="File Types" '{ if ( start ) { if ( $0 ~ /^$/ ) { print "%{nil}"; exit 0 } print $0 "\\" } if ( $0 ~ name ) start = 1; }' < README
%define supported_file_types \
  ------------+-------------+-------------+-------------+------------\
  3FR   r     | EIP   r     | LNK   r     | PAC   r     | RWL   r/w\
  3G2   r     | EPS   r/w   | M2TS  r     | PAGES r     | RWZ   r\
  3GP   r     | ERF   r/w   | M4A/V r     | PBM   r/w   | RM    r\
  ACR   r     | EXE   r     | MEF   r/w   | PCD   r     | SO    r\
  AFM   r     | EXIF  r/w/c | MIE   r/w/c | PDF   r/w   | SR2   r/w\
  AI    r/w   | EXR   r     | MIFF  r     | PEF   r/w   | SRF   r\
  AIFF  r     | F4A/V r     | MKA   r     | PFA   r     | SRW   r/w\
  APE   r     | FFF   r/w   | MKS   r     | PFB   r     | SVG   r\
  ARW   r/w   | FLA   r     | MKV   r     | PFM   r     | SWF   r\
  ASF   r     | FLAC  r     | MNG   r/w   | PGF   r     | THM   r/w\
  AVI   r     | FLV   r     | MOS   r/w   | PGM   r/w   | TIFF  r/w\
  BMP   r     | FPX   r     | MOV   r     | PICT  r     | TTC   r\
  BTF   r     | GIF   r/w   | MP3   r     | PMP   r     | TTF   r\
  CHM   r     | GZ    r     | MP4   r     | PNG   r/w   | VRD   r/w/c\
  COS   r     | HDP   r/w   | MPC   r     | PPM   r/w   | VSD   r\
  CR2   r/w   | HDR   r     | MPG   r     | PPT   r     | WAV   r\
  CRW   r/w   | HTML  r     | MPO   r/w   | PPTX  r     | WDP   r/w\
  CS1   r/w   | ICC   r/w/c | MQV   r     | PS    r/w   | WEBP  r\
  DCM   r     | IDML  r     | MRW   r/w   | PSB   r/w   | WEBM  r\
  DCP   r/w   | IIQ   r/w   | MXF   r     | PSD   r/w   | WMA   r\
  DCR   r     | IND   r/w   | NEF   r/w   | PSP   r     | WMV   r\
  DFONT r     | INX   r     | NRW   r/w   | QTIF  r     | WV    r\
  DIVX  r     | ITC   r     | NUMBERS r   | RA    r     | X3F   r/w\
  DJVU  r     | J2C   r     | ODP   r     | RAF   r/w   | XCF   r\
  DLL   r     | JNG   r/w   | ODS   r     | RAM   r     | XLS   r\
  DNG   r/w   | JP2   r/w   | ODT   r     | RAR   r     | XLSX  r\
  DOC   r     | JPEG  r/w   | OFR   r     | RAW   r/w   | XMP   r/w/c\
  DOCX  r     | K25   r     | OGG   r     | RIFF  r     | ZIP   r\
  DV    r     | KDC   r     | OGV   r     | RSRC  r     |\
  DVB   r     | KEY   r     | ORF   r/w   | RTF   r     |\
  DYLIB r     | LA    r     | OTF   r     | RW2   r/w   |\
%{nil}

# awk -vname="Meta Information" '{ if ( start ) { if ( $0 ~ /^$/ ) { print "%{nil}"; exit 0 } print $0 "\\" } if ( $0 ~ name ) start = 1; }' < README
%define supported_meta_information \
  ----------------------+----------------------+---------------------\
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r\
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r\
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r\
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r\
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r\
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  APE            r\
  ICC Profile    r/w/c  |  DICOM          r    |  Vorbis         r\
  MIE            r/w/c  |  Flash          r    |  SPIFF          r\
  JFIF           r/w/c  |  FlashPix       r    |  DjVu           r\
  Ducky APP12    r/w/c  |  QuickTime      r    |  M2TS           r\
  PDF            r/w/c  |  Matroska       r    |  PE/COFF        r\
  PNG            r/w/c  |  GeoTIFF        r    |  AVCHD          r\
  Canon VRD      r/w/c  |  PrintIM        r    |  ZIP            r\
  Nikon Capture  r/w/c  |  ID3            r    |  (and more)\
%{nil}


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

- File Types%{supported_file_types}

- Meta Information%{supported_meta_information}

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

- Formaty plików%{supported_file_types}

- Formaty metadanych%{supported_meta_information}

Więcej informacji o możliwościach pakietu ExifTool znajduje się w
pliku html/index.html.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# make sure description is up-to-date
echo "%{supported_file_types}" > supported_file_types.old.txt
echo "%{supported_meta_information}" > supported_meta_information.old.txt

awk -vname="File Types" '{ if ( start ) { if ( $0 ~ /^$/ ) { print ""; exit 0 } print } if ( $0 ~ name ) { start = 1; print "" }; }' < README > supported_file_types.new.txt
awk -vname="Meta Information" '{ if ( start ) { if ( $0 ~ /^$/ ) { print ""; exit 0 } print } if ( $0 ~ name ) { start = 1; print "" }; }' < README > supported_meta_information.new.txt

cmp supported_file_types.old.txt supported_file_types.new.txt
cmp supported_meta_information.old.txt supported_meta_information.new.txt

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/File/RandomAccess.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Image/ExifTool{,/*}.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Image/ExifTool/README

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
