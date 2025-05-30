# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-wrapt
Epoch: 100
Version: 1.17.3
Release: 1%{?dist}
Summary: Module for decorators, wrappers and monkey patching
License: BSD-2-Clause
URL: https://github.com/GrahamDumpleton/wrapt/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-wrapt
Summary: Module for decorators, wrappers and monkey patching
Requires: python3
Provides: python3-wrapt = %{epoch}:%{version}-%{release}
Provides: python3dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wrapt) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-wrapt
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%files -n python%{python3_version_nodots}-wrapt
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-wrapt
Summary: Module for decorators, wrappers and monkey patching
Requires: python3
Provides: python3-wrapt = %{epoch}:%{version}-%{release}
Provides: python3dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wrapt) = %{epoch}:%{version}-%{release}

%description -n python3-wrapt
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%files -n python3-wrapt
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-wrapt
Summary: Module for decorators, wrappers and monkey patching
Requires: python3
Provides: python3-wrapt = %{epoch}:%{version}-%{release}
Provides: python3dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wrapt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wrapt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wrapt) = %{epoch}:%{version}-%{release}

%description -n python3-wrapt
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%files -n python3-wrapt
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
