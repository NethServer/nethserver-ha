Name:		nethserver-ha
Version:	0.0.1
Release:	1%{dist}
Summary:	NethServer cluster helper
Group:		Networking/Daemons	
License:	GPL	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
Autoreq:	no
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
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/e-smith/db/configuration/defaults/corosync
/etc/e-smith/db/configuration/defaults/drbd
/etc/e-smith/db/configuration/defaults/pcsd
/etc/e-smith/templates/etc/shorewall/rules/50cluster_services
/etc/e-smith/templates/etc/sysconfig/cman
/etc/e-smith/events/nethserver-ha-update/
%attr(0554,root,root) /etc/e-smith/events/actions/nethserver-ha-conf
%dir /etc/e-smith/events/nethserver-ha-update

%changelog
