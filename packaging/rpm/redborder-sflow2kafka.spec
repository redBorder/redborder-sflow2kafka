Name: redborder-sflow2kafka
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder-sflow2kafka systemd unit running x2kafka.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-sflow2kafka
Source0: %{name}-%{version}.tar.gz

Requires: x2kafka
# pmacct is not obsoleted: rb-exporter needs its pmacctd on the proxies. Its
# sfacctd.service must stay disabled so it doesn't compete for UDP 6343.

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/redborder-sflow2kafka.service %{buildroot}/etc/systemd/system/redborder-sflow2kafka.service

%pre
# the unit was called sflow2kafka in previous versions: stop it so it frees UDP 6343
if [ "$1" -gt 1 ]; then
  systemctl disable --now sflow2kafka.service >/dev/null 2>&1 || :
fi

%post
systemctl daemon-reload

%postun
systemctl daemon-reload

%files
%defattr(0644,root,root)
/etc/systemd/system/redborder-sflow2kafka.service
%doc

%changelog
* Wed Nov 18 2026 manegron <manegron@redborder.com>
- Rename the systemd unit from sflow2kafka to redborder-sflow2kafka

* Mon Nov 09 2026 Juan Soto <jsoto@redborder.com> - 1.0.0-1
- first spec version, sflow2kafka service runs x2kafka instead of pmacct sfacctd
