#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kwordquiz
Version  : 20.12.0
Release  : 25
URL      : https://download.kde.org/stable/release-service/20.12.0/src/kwordquiz-20.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.0/src/kwordquiz-20.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.0/src/kwordquiz-20.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kwordquiz-bin = %{version}-%{release}
Requires: kwordquiz-data = %{version}-%{release}
Requires: kwordquiz-license = %{version}-%{release}
Requires: kwordquiz-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : knotifyconfig-dev
BuildRequires : libkeduvocdocument-dev
BuildRequires : phonon-dev
BuildRequires : qtbase-dev mesa-dev

%description


%package bin
Summary: bin components for the kwordquiz package.
Group: Binaries
Requires: kwordquiz-data = %{version}-%{release}
Requires: kwordquiz-license = %{version}-%{release}

%description bin
bin components for the kwordquiz package.


%package data
Summary: data components for the kwordquiz package.
Group: Data

%description data
data components for the kwordquiz package.


%package doc
Summary: doc components for the kwordquiz package.
Group: Documentation

%description doc
doc components for the kwordquiz package.


%package license
Summary: license components for the kwordquiz package.
Group: Default

%description license
license components for the kwordquiz package.


%package locales
Summary: locales components for the kwordquiz package.
Group: Default

%description locales
locales components for the kwordquiz package.


%prep
%setup -q -n kwordquiz-20.12.0
cd %{_builddir}/kwordquiz-20.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607725948
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607725948
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwordquiz
cp %{_builddir}/kwordquiz-20.12.0/COPYING %{buildroot}/usr/share/package-licenses/kwordquiz/133efad5329acf364135c569ac01ec084c3d4647
cp %{_builddir}/kwordquiz-20.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kwordquiz/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/kwordquiz-20.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kwordquiz/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang kwordquiz

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kwordquiz

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kwordquiz.desktop
/usr/share/config.kcfg/kwordquiz.kcfg
/usr/share/icons/hicolor/128x128/apps/kwordquiz.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-kwordquiz.png
/usr/share/icons/hicolor/16x16/apps/kwordquiz.png
/usr/share/icons/hicolor/16x16/mimetypes/application-x-kwordquiz.png
/usr/share/icons/hicolor/22x22/apps/kwordquiz.png
/usr/share/icons/hicolor/22x22/mimetypes/application-x-kwordquiz.png
/usr/share/icons/hicolor/32x32/apps/kwordquiz.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-kwordquiz.png
/usr/share/icons/hicolor/48x48/apps/kwordquiz.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-kwordquiz.png
/usr/share/icons/hicolor/64x64/apps/kwordquiz.png
/usr/share/knotifications5/kwordquiz.notifyrc
/usr/share/knsrcfiles/kwordquiz.knsrc
/usr/share/kwordquiz/examples/example.kvtml
/usr/share/kwordquiz/examples/fill_in_the_blank.kvtml
/usr/share/kwordquiz/examples/french_verbs.kvtml
/usr/share/kwordquiz/examples/us_states_and_capitals.kvtml
/usr/share/kwordquiz/icons/hicolor/128x128/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/error.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/question.png
/usr/share/kwordquiz/icons/hicolor/128x128/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/dontknow.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/error.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/hint.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/know.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/markasblank.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/question.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/repeat.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/shuffle.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/sort_incr.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/start-over.png
/usr/share/kwordquiz/icons/hicolor/16x16/actions/unmarkasblank.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/dontknow.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/error.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/hint.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/know.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/markasblank.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/question.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/repeat.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/shuffle.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/sort_incr.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/start-over.png
/usr/share/kwordquiz/icons/hicolor/22x22/actions/unmarkasblank.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/dontknow.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/error.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/hint.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/know.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/markasblank.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/question.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/question_mark.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/repeat.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/shuffle.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/sort_incr.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/start-over.png
/usr/share/kwordquiz/icons/hicolor/32x32/actions/unmarkasblank.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/error.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/question.png
/usr/share/kwordquiz/icons/hicolor/48x48/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/answer-correct.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/answer.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/delete-table-row.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/editor.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/error.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/flash.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/insert-table-row.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/languages.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/mode1.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/mode2.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/mode3.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/mode4.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/mode5.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/multiple.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/qa.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/question.png
/usr/share/kwordquiz/icons/hicolor/64x64/actions/rowcol.png
/usr/share/kwordquiz/icons/hicolor/scalable/actions/answer-correct.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/answer.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/delete-table-row.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/editor.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/error.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/flash.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/insert-table-row.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/languages.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/markasblank.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/mode1.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/mode2.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/mode3.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/mode4.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/mode5.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/multiple.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/qa.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/question.svgz
/usr/share/kwordquiz/icons/hicolor/scalable/actions/unmarkasblank.svgz
/usr/share/kxmlgui5/kwordquiz/kwordquizui.rc
/usr/share/metainfo/org.kde.kwordquiz.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/ca/kwordquiz/index.docbook
/usr/share/doc/HTML/de/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/de/kwordquiz/index.docbook
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-characters.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-configure-appearance.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-configure-characters.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-configure-editor.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-configure-general.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-configure-quiz.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-languages.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-print-exam.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-print-flashcard.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-print-list.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-print-type.png
/usr/share/doc/HTML/de/kwordquiz/kwq-dlg-rowscolumns.png
/usr/share/doc/HTML/de/kwordquiz/kwq-editor.png
/usr/share/doc/HTML/de/kwordquiz/kwq-flashcard.png
/usr/share/doc/HTML/de/kwordquiz/kwq-multiple.png
/usr/share/doc/HTML/de/kwordquiz/kwq-qanda.png
/usr/share/doc/HTML/en/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/en/kwordquiz/index.docbook
/usr/share/doc/HTML/en/kwordquiz/kwordquiz-icon.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-characters.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-configure-appearance.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-configure-characters.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-configure-editor.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-configure-general.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-configure-quiz.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-languages.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-print-exam.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-print-flashcard.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-print-list.png
/usr/share/doc/HTML/en/kwordquiz/kwq-dlg-print-type.png
/usr/share/doc/HTML/en/kwordquiz/kwq-editor.png
/usr/share/doc/HTML/en/kwordquiz/kwq-flashcard.png
/usr/share/doc/HTML/en/kwordquiz/kwq-multiple.png
/usr/share/doc/HTML/en/kwordquiz/kwq-qanda.png
/usr/share/doc/HTML/en/kwordquiz/kwq-tutor-popup-minimalistic.png
/usr/share/doc/HTML/en/kwordquiz/kwq-tutor-popup-native.png
/usr/share/doc/HTML/en/kwordquiz/kwq-tutor-settings.png
/usr/share/doc/HTML/en/kwordquiz/kwq-tutor-shortcuts.png
/usr/share/doc/HTML/en/kwordquiz/kwq-tutor-welcome.png
/usr/share/doc/HTML/es/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/es/kwordquiz/index.docbook
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-characters.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-configure-appearance.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-configure-characters.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-configure-editor.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-configure-general.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-configure-quiz.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-languages.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-print-exam.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-print-flashcard.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-print-list.png
/usr/share/doc/HTML/es/kwordquiz/kwq-dlg-print-type.png
/usr/share/doc/HTML/es/kwordquiz/kwq-editor.png
/usr/share/doc/HTML/es/kwordquiz/kwq-flashcard.png
/usr/share/doc/HTML/es/kwordquiz/kwq-multiple.png
/usr/share/doc/HTML/es/kwordquiz/kwq-qanda.png
/usr/share/doc/HTML/et/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/et/kwordquiz/index.docbook
/usr/share/doc/HTML/it/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/it/kwordquiz/index.docbook
/usr/share/doc/HTML/ko/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/ko/kwordquiz/index.docbook
/usr/share/doc/HTML/nl/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/nl/kwordquiz/index.docbook
/usr/share/doc/HTML/pt/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/pt/kwordquiz/index.docbook
/usr/share/doc/HTML/pt_BR/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kwordquiz/index.docbook
/usr/share/doc/HTML/sv/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/sv/kwordquiz/index.docbook
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-characters.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-configure-characters.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-configure-editor.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-configure-quiz.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-languages.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-print-exam.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-print-flashcard.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-print-list.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-print-type.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-dlg-rowscolumns.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-editor.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-flashcard.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-multiple.png
/usr/share/doc/HTML/sv/kwordquiz/kwq-qanda.png
/usr/share/doc/HTML/uk/kwordquiz/index.cache.bz2
/usr/share/doc/HTML/uk/kwordquiz/index.docbook
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-characters.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-configure-appearance.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-configure-characters.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-configure-editor.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-configure-general.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-configure-quiz.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-languages.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-dlg-print-type.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-editor.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-flashcard.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-multiple.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-qanda.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-tutor-popup-minimalistic.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-tutor-popup-native.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-tutor-settings.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-tutor-shortcuts.png
/usr/share/doc/HTML/uk/kwordquiz/kwq-tutor-welcome.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwordquiz/133efad5329acf364135c569ac01ec084c3d4647
/usr/share/package-licenses/kwordquiz/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kwordquiz/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f kwordquiz.lang
%defattr(-,root,root,-)

