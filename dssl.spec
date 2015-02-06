%define major 0
%define api 1.4
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Name:		dssl
Version:	1.4.4
Release:	8
Summary:    DSSL library: network capture and SSL decryption toolkit
License:    GPLv3+
Group:      Networking/Other
URL:        http://www.ssltech.net/
Source:     http://www.ssltech.net/downloads/%{name}-%{version}.tar.gz
Patch0:		dssl-samples.diff
BuildRequires:	openssl-devel
BuildRequires:	pcap-devel
BuildRequires:	zlib-devel

%description
DSSL library is a network caputre and SSL decryption toolkit useful 
for snort and other SSL aware software.

%package -n %{libname}
Summary:	Main library for dssl
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
DSSL library is a network caputre and SSL decryption toolkit useful 
for snort and other SSL aware software.


%package -n %{develname}
Summary:	Header files for the dssl library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	openssl-devel
Requires:	pcap-devel
Requires:	zlib-devel

%description    -n %{develname}
DSSL library is a network caputre and SSL decryption toolkit useful
for snort and other SSL aware software. These are .h files.

%prep
%setup -q 
%patch0 -p1 -b .sample_fix

export LIBS=-lpcap 
%configure2_5x --enable-shared

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdssl.so.%{major}*

%files -n %{develname}
%{_includedir}/dssl/*
%{_bindir}/ssltrace
%{_libdir}/libdssl.so
%{_libdir}/libdssl.a

