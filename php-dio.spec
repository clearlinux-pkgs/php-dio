#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-dio
Version  : 0.2.1
Release  : 55
URL      : https://pecl.php.net/get/dio-0.2.1.tgz
Source0  : https://pecl.php.net/get/dio-0.2.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-dio-lib = %{version}-%{release}
Requires: php-dio-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the php-dio package.
Group: Libraries
Requires: php-dio-license = %{version}-%{release}

%description lib
lib components for the php-dio package.


%package license
Summary: license components for the php-dio package.
Group: Default

%description license
license components for the php-dio package.


%prep
%setup -q -n dio-0.2.1
cd %{_builddir}/dio-0.2.1
pushd ..
cp -a dio-0.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-dio
cp %{_builddir}/dio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-dio/27b46923d7341b6bb717d06db4850b1180d565b2 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/dio.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-dio/27b46923d7341b6bb717d06db4850b1180d565b2
