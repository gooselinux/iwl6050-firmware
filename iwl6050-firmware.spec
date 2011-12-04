Name:           iwl6050-firmware
Version:        9.201.4.1
Release:        2%{?dist}
Summary:        Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:            http://intellinuxwireless.org/
Source0:        http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-6050-ucode-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       udev


%description
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl6050 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%prep
%setup -c -q

# Change permission
find . -type f -exec chmod 0644 {} ';'

pushd iwlwifi-6050-ucode-%{version}
# Change encoding
sed -i 's/\r//'  LICENSE.iwlwifi-6050-ucode README.iwlwifi-6050-ucode
# Rename docs
mv LICENSE.iwlwifi-6050-ucode ../LICENSE
mv README.iwlwifi-6050-ucode ../README
# Preserve timestamp
touch -r *.ucode ../LICENSE ../README
popd


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
pushd iwlwifi-6050-ucode-%{version}
install -pm 0644 *.ucode $RPM_BUILD_ROOT/lib/firmware/
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README
/lib/firmware/*.ucode


%changelog
* Tue Jun  8 2010 John W. Linville <linville@tuxdriver.com> - 9.201.4.1-2
- Cleanse permissions of extracted files

* Tue Jun  8 2010 John W. Linville <linville@tuxdriver.com> - 9.201.4.1-1
- Initial import
