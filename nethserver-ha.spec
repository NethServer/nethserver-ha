Name:		nethserver-ha
Version:	0.0.1
Release:	1%{dist}
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

%changelog
* Thu Mar 17 2016 Davide Principi <davide.principi@nethesis.it> - 0.0.1
- Initial version