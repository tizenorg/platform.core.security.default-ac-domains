Name:		default-ac-domains
Version:	0.1
Release:	1
Group:		Security/Access Control
License:	GPL-2.0
Summary:	The definition of default ac domains
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz
Source1001:	default-ac-domains.manifest

%description
The package provides a definition for the default set of ac domains 
with the corresponding Smack rules between them

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install

%files
%defattr(-,root,root)
%manifest default-ac-domains.manifest

