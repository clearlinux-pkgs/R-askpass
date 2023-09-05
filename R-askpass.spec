#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-askpass
Version  : 1.2.0
Release  : 40
URL      : https://cran.r-project.org/src/contrib/askpass_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/askpass_1.2.0.tar.gz
Summary  : Password Entry Utilities for R, Git, and SSH
Group    : Development/Tools
License  : MIT
Requires: R-askpass-lib = %{version}-%{release}
Requires: R-sys
BuildRequires : R-sys
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
passphrase, for example to authenticate with a server or read a protected key.
    Includes native programs for MacOS and Windows, hence no 'tcltk' is required.

%package lib
Summary: lib components for the R-askpass package.
Group: Libraries

%description lib
lib components for the R-askpass package.


%prep
%setup -q -n askpass
pushd ..
cp -a askpass buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693935815

%install
export SOURCE_DATE_EPOCH=1693935815
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/askpass/DESCRIPTION
/usr/lib64/R/library/askpass/INDEX
/usr/lib64/R/library/askpass/LICENSE
/usr/lib64/R/library/askpass/Meta/Rd.rds
/usr/lib64/R/library/askpass/Meta/features.rds
/usr/lib64/R/library/askpass/Meta/hsearch.rds
/usr/lib64/R/library/askpass/Meta/links.rds
/usr/lib64/R/library/askpass/Meta/nsInfo.rds
/usr/lib64/R/library/askpass/Meta/package.rds
/usr/lib64/R/library/askpass/NAMESPACE
/usr/lib64/R/library/askpass/NEWS
/usr/lib64/R/library/askpass/R/askpass
/usr/lib64/R/library/askpass/R/askpass.rdb
/usr/lib64/R/library/askpass/R/askpass.rdx
/usr/lib64/R/library/askpass/WORDLIST
/usr/lib64/R/library/askpass/help/AnIndex
/usr/lib64/R/library/askpass/help/aliases.rds
/usr/lib64/R/library/askpass/help/askpass.rdb
/usr/lib64/R/library/askpass/help/askpass.rdx
/usr/lib64/R/library/askpass/help/paths.rds
/usr/lib64/R/library/askpass/html/00Index.html
/usr/lib64/R/library/askpass/html/R.css
/usr/lib64/R/library/askpass/mac-askpass
/usr/lib64/R/library/askpass/mac-simplepass
/usr/lib64/R/library/askpass/tests/testthat.R
/usr/lib64/R/library/askpass/tests/testthat/test-option.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/askpass/libs/askpass.so
/usr/lib64/R/library/askpass/libs/askpass.so.avx2
/usr/lib64/R/library/askpass/libs/askpass.so.avx512
