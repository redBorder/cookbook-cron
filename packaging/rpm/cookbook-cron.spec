Name: cookbook-cron
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Cron cookbook to install and configure it in redborder environments

License: AGPL 3.0
URL: https://github.com/redBorder/cookbook-cron
Source0: %{name}-%{version}.tar.gz

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/var/chef/cookbooks/cron
cp -f -r  * %{buildroot}/var/chef/cookbooks/cron
chmod -R 0755 %{buildroot}/var/chef/cookbooks/cron
install -D -m 0644 README.md %{buildroot}/var/chef/cookbooks/cron/README.md

%pre

%post
case "$1" in
  1)
    # This is an initial install.
    :
  ;;
  2)
    # This is an upgrade.
    su - -s /bin/bash -c 'source /etc/profile && rvm gemset use default && env knife cookbook upload cron'
  ;;
esac

%files
%defattr(0755,root,root)
/var/chef/cookbooks/cron
%defattr(0644,root,root)
/var/chef/cookbooks/cron/README.md


%doc

%changelog
* Mon Apr 18 2022 Eduardo Reyes <eareyes@redborder.com> - 0.0.1-1
- first spec version
