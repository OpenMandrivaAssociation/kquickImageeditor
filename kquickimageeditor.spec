%define gitdate 20201207

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

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
%setup -q -n %{name}-master
%autopatch -p1

%build
%cmake_kde5
%ninja_build

%install
%ninja_install -C build


%files
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri
%{_libdir}/qt5/qml/org/kde/kquickimageeditor
%{_libdir}/libkquickimageeditorplugin.so

%files -n %{devname}
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfig.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfigVersion.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorTargets-release.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorTargets.cmake
