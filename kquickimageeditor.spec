#define gitdate 20201207

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:           kquickimageeditor
Version:        0.1.3
Release:        %{?gitdate:0.%{gitdate}.}1
Summary:        Qt Image editing components
License:        LGPL2.1
Group:          System/Libraries
Url:            https://invent.kde.org/libraries/kquickimageeditor
%if 0%{?gitdate}
Source:         https://invent.kde.org/libraries/kquickimageeditor/-/archive/master/%{name}-master.tar.bz2
%else
Source:         https://invent.kde.org/libraries/kquickimageeditor/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
%endif

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
BuildRequires:	ninja

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package -n %{devname}
Summary:	Header files for KQuickImageEditor
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files of for KQuickImageEditor

%prep
%if 0%{?gitdate}
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1 -n %{name}-v%{version}
%endif
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build


%files
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri
%{_libdir}/qt5/qml/org/kde/kquickimageeditor

%files -n %{devname}
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfig.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfigVersion.cmake
