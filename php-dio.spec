#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-dio
Version  : 0.2.1
Release  : 27
URL      : https://pecl.php.net/get/dio-0.2.1.tgz
Source0  : https://pecl.php.net/get/dio-0.2.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-dio-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-dio package.
Group: Libraries

%description lib
lib components for the php-dio package.


%prep
%setup -q -n dio-0.2.1
cd %{_builddir}/dio-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/dio.so
