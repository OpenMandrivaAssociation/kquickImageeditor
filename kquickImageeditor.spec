%define gitdate 07122020

Name:           kquickimageeditor
Version:        0.0
Release:        0.%{gitdate}.1
Summary:        Qt Image editing components
License:        LGPL2.1
Group:          System/Libraries
Url:            https://invent.kde.org/libraries/kquickimageeditor
Source:         https://invent.kde.org/libraries/kquickimageeditor/-/archive/master/%{name}-master.tar.bz2

BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake(ECM)

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%prep
%setup -q -n %{name}-master
%autopatch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/%{_lib}
    
%make_build

%install

%make_install -C build


%files
