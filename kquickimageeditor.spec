%undefine gitdate

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

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
BuildRequires:       cmake(Qt6)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Designer)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Quick)

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

%prep
%autosetup -p1
%build
export CMAKE_BUILD_DIR=build-qt5
%cmake_kde5

cd ..
export CMAKE_BUILD_DIR=build-qt6
%cmake \
       -DBUILD_WITH_QT6:BOOL=ON \
       -G Ninja
cd ..

%ninja_build -C build-qt5

%ninja_build -C build-qt6

%install
%ninja_install -C build-qt5

%ninja_install -C build-qt6


%files
%{_libdir}/qt5/mkspecs/modules/qt_KQuickImageEditor.pri
%{_libdir}/qt5/qml/org/kde/kquickimageeditor

%files -n %{devname}
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfig.cmake
%{_libdir}/cmake/KQuickImageEditor/KQuickImageEditorConfigVersion.cmake
