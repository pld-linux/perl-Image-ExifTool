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
Version:	9.28
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.sno.phy.queensu.ca/~phil/exiftool/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c862a1a5457b4096bf295259154f9bd
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
  3FR   r     | EIP   r     | LA    r     | ORF   r/w   | RSRC  r\
  3G2   r     | EPS   r/w   | LNK   r     | OTF   r     | RTF   r\
  3GP   r     | ERF   r/w   | M2TS  r     | PAC   r     | RW2   r/w\
  ACR   r     | EXE   r     | M4A/V r     | PAGES r     | RWL   r/w\
  AFM   r     | EXIF  r/w/c | MEF   r/w   | PBM   r/w   | RWZ   r\
  AI    r/w   | EXR   r     | MIE   r/w/c | PCD   r     | RM    r\
  AIFF  r     | F4A/V r     | MIFF  r     | PDF   r/w   | SO    r\
  APE   r     | FFF   r/w   | MKA   r     | PEF   r/w   | SR2   r/w\
  ARW   r/w   | FLA   r     | MKS   r     | PFA   r     | SRF   r\
  ASF   r     | FLAC  r     | MKV   r     | PFB   r     | SRW   r/w\
  AVI   r     | FLV   r     | MNG   r/w   | PFM   r     | SVG   r\
  BMP   r     | FPF   r     | MODD  r     | PGF   r     | SWF   r\
  BTF   r     | FPX   r     | MOS   r/w   | PGM   r/w   | THM   r/w\
  CHM   r     | GIF   r/w   | MOV   r     | PLIST r     | TIFF  r/w\
  COS   r     | GZ    r     | MP3   r     | PICT  r     | TTC   r\
  CR2   r/w   | HDP   r/w   | MP4   r     | PMP   r     | TTF   r\
  CRW   r/w   | HDR   r     | MPC   r     | PNG   r/w   | VRD   r/w/c\
  CS1   r/w   | HTML  r     | MPG   r     | PPM   r/w   | VSD   r\
  DCM   r     | ICC   r/w/c | MPO   r/w   | PPT   r     | WAV   r\
  DCP   r/w   | IDML  r     | MQV   r     | PPTX  r     | WDP   r/w\
  DCR   r     | IIQ   r/w   | MRW   r/w   | PS    r/w   | WEBP  r\
  DFONT r     | IND   r/w   | MXF   r     | PSB   r/w   | WEBM  r\
  DIVX  r     | INX   r     | NEF   r/w   | PSD   r/w   | WMA   r\
  DJVU  r     | ITC   r     | NRW   r/w   | PSP   r     | WMV   r\
  DLL   r     | J2C   r     | NUMBERS r   | QTIF  r     | WV    r\
  DNG   r/w   | JNG   r/w   | ODP   r     | RA    r     | X3F   r/w\
  DOC   r     | JP2   r/w   | ODS   r     | RAF   r/w   | XCF   r\
  DOCX  r     | JPEG  r/w   | ODT   r     | RAM   r     | XLS   r\
  DV    r     | K25   r     | OFR   r     | RAR   r     | XLSX  r\
  DVB   r     | KDC   r     | OGG   r     | RAW   r/w   | XMP   r/w/c\
  DYLIB r     | KEY   r     | OGV   r     | RIFF  r     | ZIP   r\
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
%lang(fi) %{perl_vendorlib}/Image/ExifTool/Lang/fi.pm
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
