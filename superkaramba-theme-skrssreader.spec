
%define		theme	skrssreader

Summary:	superkaramba - RSS Reader
Summary(pl.UTF-8):   superkaramba - Czytnik kanałów RSS
Name:		superkaramba-theme-%{theme}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/8721-%{theme}-%{version}.tar.gz
# Source0-md5:	4e3357738d799d3c19052cfa438a3982
URL:		http://www.flagar.com
Requires:	superkaramba >= 0.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_skrssreaderdir 	/themes/superkaramba/skrssreader

%description
RSS Reader for superkaramba. The SuperKaramba RSS reader (skrssreader)
is featured by a temporized slideshow of the headlines (with
descriptions) from the news feed specified. Modify the skrssreader.py
file to change the URL of the RSS feed, color and size of the fonts.

%description -l pl.UTF-8
Czytnik kanałów RSS dla superkaramby. Czyta informacje z określonego
źródła i wyświetla w postaci pokazu slajdów. W razie potrzeby należy
zmienić URL źródła, kolor i rozmiar fontów w skrssreader.py.

%prep
%setup -q -n %{theme}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}%{_skrssreaderdir}
install {skrssreader.theme,*.py} $RPM_BUILD_ROOT%{_datadir}%{_skrssreaderdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}%{_skrssreaderdir}
