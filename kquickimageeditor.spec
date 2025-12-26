%undefine gitdate

%define devname %mklibname %{name} -d

Name:		kquickimageeditor
Version:	0.6.0
Release:	%{?gitdate:0.%{gitdate}.}2
Summary:	Qt Image editing components
License:	LGPL2.1
Group:		System/Libraries
Url:		https://invent.kde.org/libraries/kquickimageeditor
%if 0%{?gitdate}
Source0:	https://invent.kde.org/libraries/kquickimageeditor/-/archive/master/%{name}-master.tar.bz2
%else
#Source0:	https://invent.kde.org/libraries/kquickimageeditor/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source0:	https://download.kde.org/stable/kquickimageeditor/%{name}-%{version}.tar.xz
%endif

%rename kquickimageeditor-qt6

BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Designer)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(ECM)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package -n %{devname}
Summary:	Header files for KQuickImageEditor
Group:		Development/C
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Header files of for KQuickImageEditor.

%files
%{_libdir}/libKQuickImageEditor.so.*
%{_qtdir}/qml/org/kde/kquickimageeditor

%files -n %{devname}
%{_libdir}/libKQuickImageEditor.so
%{_qtdir}/mkspecs/modules/qt_KQuickImageEditor.pri
%{_libdir}/cmake/KQuickImageEditor
%{_includedir}/kquickimageeditor
%{_includedir}/KQuickImageEditor
