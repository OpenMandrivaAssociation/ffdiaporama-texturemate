%define oname ffdiaporama_texturemate
%define upname ffDiaporama_texturemate
Name:           ffdiaporama-texturemate
Version:        1.0
Release:        1.20140125
Summary:        Background textures for ffDiaporama
License:        CC-BY
URL:            https://www.texturemate.com/
Group:          Graphics
BuildArch:      noarch
Source0:        http://download.tuxfamily.org/ffdiaporama/Packages/Stable/%{oname}_1.0.2014.0125.tar.gz

BuildRequires:	ffdiaporama >= 2.2
BuildRequires:	qmake5
BuildRequires:  qt5-macros


Requires(preun):ffdiaporama >= 2.2

%description
This package contains free textures to set as background in ffDiaporama.
You can set a texture as background from the library when editing the
background in a slide's settings dialog.
ffDiaporama-texturemate is part of ffDiaporama
ffDiaporama is a tool to make diaporamas as video
All resources provided with ffDiaporama-texturemate are from the site:
 http://www.texturemate.com/
and have been redesigned to work with ffDiaporama 1.6 and higher.

%prep
%setup -qn %{upname}

%build
%qmake_qt5 %{upname}.pro

%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}


%files
%doc licence.txt readme.txt TMTBUILDVERSION.txt
%{_datadir}/ffDiaporama/background/texturemate/*


