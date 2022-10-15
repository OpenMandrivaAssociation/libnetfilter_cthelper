%define major                 0
%define libname               %mklibname netfilter_cthelper %{major}
%define libnamedevel          %mklibname netfilter_cthelper -d
%define debug_package %{nil}

Name:           libnetfilter_cthelper
Version:        1.0.1
Release:        1
Summary:        Interface to the user-space helper infrastructure
Group:          System/Libraries
License:        GPL
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2
Source1:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2.sig
BuildRequires: pkgconfig(libmnl) >= 1.0.3

%description
libnetfilter_cthelper is the userspace library that provides the programming \
interface to the user-space helper infrastructure available since Linux \
kernel 3.6. With this library, you register, configure, enable and disable \
user-space helpers.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Provides:       netfilter_cthelper = %{version}-%{release}

%description -n %{libname}
libnetfilter_cthelper is the userspace library that provides the programming \
interface to the user-space helper infrastructure available since Linux \
kernel 3.6. With this library, you register, configure, enable and disable \
user-space helpers.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Provides:       netfilter_cthelper-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%setup -q

%build
export CFLAGS=-fvisibility=default
%{configure2_5x} --disable-static
%{make}

%install
%{makeinstall_std}
rm -f %{buildroot}%{_libdir}/*.la

%check
%{make} check

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{libnamedevel}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Oct 18 2013 umeabot <umeabot> 1.0.0-3.mga4
+ Revision: 507199
- Mageia 4 Mass Rebuild

