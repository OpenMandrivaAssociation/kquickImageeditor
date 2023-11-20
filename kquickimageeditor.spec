%undefine gitdate

%define devname %mklibname %{name} -d
%define qt6devname %mklibname %{name}-qt6 -d

Name:		kquickimageeditor
Version:	0.3.0
Release:	%{?gitdate:0.%{gitdate}.}1
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

BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Designer)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	cmake(ECM)

# Qt6
BuildRequires:	cmake(Qt6)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Designer)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Qml)

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

%package qt6
Summary:	KQuickImageEditor for Qt 6.x
Group:		System/Libraries

%description qt6
KQuickImageEditor for Qt 6.x

%package -n %{qt6devname}
Summary:	CMake files for KQuickImageEditor for Qt 6.x
Group:		Development/C
Requires:	%{name}-qt6 = %{EVRD}
Provides:	%{name}-qt6-devel = %{EVRD}

%description -n %{qt6devname}
CMake files of KQuickImageEditor for Qt 6.x

%prep
%autosetup -p1
%cmake_kde5
cd ..

export CMAKE_BUILD_DIR=build-qt6
%cmake \
       -DBUILD_WITH_QT6:BOOL=ON \
       -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
       -G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build-qt6
mkdir -p %{buildroot}%{_qtdir}/lib/cmake
mv %{buildroot}%{_libdir}/cmake/KQuickImageEditor %{buildroot}%{_qtdir}/lib/cmake

%ninja_install -C build

%files
%{_libdir}/qt5/qml/org/kde/kquickimageeditor

%files qt6
%{_qtdir}/qml/org/kde/kquickimageeditor

%files -n %{devname}
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri
%{_libdir}/cmake/KQuickImageEditor

%files -n %{qt6devname}
%{_qtdir}/mkspecs/modules/qt_KQuickImageEditor.pri
%{_qtdir}/lib/cmake/KQuickImageEditor
