Summary:	User interface library based on GTK+
Name:		girara3
Version:	0.2.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://pwmt.org/projects/girara/download/girara-%{version}.tar.gz
# Source0-md5:	f22a75b51cf88f241096e230985f28db
BuildRequires:	gtk+3-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism. Currently based on GTK+, a cross-platform
widget toolkit, it provides an interface that focuses on three main
components: A so-called view widget that represents the actual
application (e.g. a website (browser), an image (image viewer) or the
document (document viewer)), an input bar that is used to execute
commands of the application and the status bar which provides the user
with current information. girara was designed to replace and enhance
the user interface that is used by zathura and jumanji and other
features that those applications share.

%package devel
Summary:	Header files for girara library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for girara library.

%prep
%setup -qn girara-%{version}

%{__sed} -i "s/^DFLAGS.*/DFLAGS=/" config.mk

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR=%{_libdir}

chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%find_lang libgirara-gtk3-2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f libgirara-gtk3-2.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %ghost %{_libdir}/libgirara-gtk3.so.2
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so
%{_includedir}/girara
%{_pkgconfigdir}/girara-gtk3.pc

