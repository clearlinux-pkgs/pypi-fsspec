#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-fsspec
Version  : 2023.1.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/6e/de/d14309e99f60010055bfd04c9e57d20a8d7b3f1c2144f0d85c1747017718/fsspec-2023.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/de/d14309e99f60010055bfd04c9e57d20a8d7b3f1c2144f0d85c1747017718/fsspec-2023.1.0.tar.gz
Summary  : File-system specification
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-fsspec-license = %{version}-%{release}
Requires: pypi-fsspec-python = %{version}-%{release}
Requires: pypi-fsspec-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# filesystem_spec
[![PyPI version](https://badge.fury.io/py/fsspec.svg)](https://pypi.python.org/pypi/fsspec/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/fsspec/badges/version.svg)](https://anaconda.org/conda-forge/fsspec)
![Build](https://github.com/fsspec/filesystem_spec/workflows/CI/badge.svg)
[![Docs](https://readthedocs.org/projects/filesystem-spec/badge/?version=latest)](https://filesystem-spec.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-fsspec package.
Group: Default

%description license
license components for the pypi-fsspec package.


%package python
Summary: python components for the pypi-fsspec package.
Group: Default
Requires: pypi-fsspec-python3 = %{version}-%{release}

%description python
python components for the pypi-fsspec package.


%package python3
Summary: python3 components for the pypi-fsspec package.
Group: Default
Requires: python3-core
Provides: pypi(fsspec)

%description python3
python3 components for the pypi-fsspec package.


%prep
%setup -q -n fsspec-2023.1.0
cd %{_builddir}/fsspec-2023.1.0
pushd ..
cp -a fsspec-2023.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674229097
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fsspec
cp %{_builddir}/fsspec-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-fsspec/05ee6f4bb52a15a0a29b05ceab4c9648092a8c51 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fsspec/05ee6f4bb52a15a0a29b05ceab4c9648092a8c51

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
