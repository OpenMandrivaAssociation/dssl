%define name    dssl
%define version 1.4.4
%define release %mkrel 1
%define major 1
%define api 1.4
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    DSSL library: network capture and SSL decryption toolkit
License:    GPL3
Group:      Networking/Other
URL:        http://www.ssltech.net/
Source:     http://www.ssltech.net/downloads/%{name}-%{version}.tar.gz
Patch0:		dssl-samples.diff
Requires:       openssl
Requires:	libpcap
BuildRequires:  openssl-devel
BuildRequires:	libpcap-devel

%if %mdkversion < 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}
%endif

%description
DSSL library is a network caputre and SSL decryption toolkit useful for snort and other SSL aware 
software.

%package -n     %{libname}
Summary:        Main library for dssl
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
DSSL library is a network caputre and SSL decryption toolkit useful for snort and other SSL aware
software.


%package        -n     %{develname}
Summary:        Header files for the dssl library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Requires:  openssl-devel
Requires:  libpcap-devel

%description    -n %{develname}
DSSL library is a network caputre and SSL decryption toolkit useful for snort and other SSL aware
software.  These are .h files.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%prep
%setup -q 
%patch0 -p1 -b .sample_fix

%configure2_5x

%build
%make
%install
#install conf/snortsam.conf.sample %{buildroot}%{_sysconfdir}/snortsam.conf
%makeinstall
#%{__rm} -rf %{buildroot}

#mkdir %{buildroot}%_mandir/man1
#mv %{buildroot}%_mandir/*.1 %{buildroot}%_mandir/man1/

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc docs/*
%doc docs/dssl/*
%_bindir/ssltrace
%{_libdir}/libdssl.a
%{_libdir}/libdssl.la

%files  -n %{develname}
%defattr(-,root,root)
%{_includedir}/dssl/*


