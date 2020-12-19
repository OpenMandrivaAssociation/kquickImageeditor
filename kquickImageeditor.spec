%define gitdate 07122020

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
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/%{_lib}
    
%make_build

%install

%make_install -C build


%files
%{_libdir}/qml/org/kde/kquickimageeditor/BasicResizeHandle.qml
%{_libdir}/qml/org/kde/kquickimageeditor/libkquickimageeditorplugin.so
%{_libdir}/qml/org/kde/kquickimageeditor/plugins.qmltypes
%{_libdir}/qml/org/kde/kquickimageeditor/qmldir
%{_libdir}/org/kde/kquickimageeditor/qmldir.license
%{_prerifx}/mkspecs/modules/qt_KQuickImageEditor.pri

%files -n %{devname}
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfig.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfigVersion.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorTargets-release.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorTargets.cmake
%{_libdir}/libkquickimageeditorplugin.so
