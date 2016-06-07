Name:		nethserver-ha
Version: 1.0.1
Release: 1%{?dist}
Summary:	NethServer cluster helper
License:	GPL	
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  nethserver-devtools	
Requires: pacemaker corosync cman pcs fence-agents
Requires: drbd84-utils kmod-drbd84

%description
Install and configure corosync and pacemaker for an easy two node cluster on NethServer

%prep
%setup 

%build
perl -w createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%doc COPYING

%changelog
* Tue Jun 07 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Removed alt ring
- nethserver-ha-drbd: exit if drbd initialization fails

* Thu Mar 31 2016 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Initial release

* Thu Mar 17 2016 Davide Principi <davide.principi@nethesis.it> - 0.0.1
- Initial version