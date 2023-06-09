%define _disable_ld_no_undefined 1

Name:           pix
Version:        3.0.1
Release:        1
Summary:        Image viewer and browser utility
License:        GPL-2.0+
Group:          Graphics/Viewers
Url:            https://github.com/linuxmint/pix
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		pix-2.8.9-exiv2-0.28.patch

BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gnome-common
BuildRequires:  itstool
BuildRequires:  intltool
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libbrasero-burn3) >= 3.2.0
BuildRequires:  pkgconfig(libopenraw-0.1) >= 0.0.8
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-gnome-2.4) >= 2.36.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xapp)

%description
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%package devel
Summary:        Image viewer and browser utility -- Development Files
Group:          System/Libraries
Requires:       %{name} = %{version}

%description devel
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name "*.la" -delete
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING README* debian/changelog
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/glib-2.0/schemas/*%{name}*.gschema.xml
%{_datadir}/glib-2.0/schemas/*%{name}.enums.xml
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}-2.8/
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/%{name}-2.8.pc
