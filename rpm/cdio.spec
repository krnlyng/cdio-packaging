Name:		libcdio
Version:	2.1.0
Release:	1%{?dist}
Summary:    GNU Compact Disc Input and Control Library

License:	ISC
URL:		https://www.gnu.org/software/libcdio/
Source0:	${name}-${version}.tar.bz2

BuildRequires: automake
BuildRequires: texinfo
BuildRequires: help2man

%package devel
Summary: libcdio development files
%description devel
libcdio development files

%package doc
Summary: libcdio documentation files
%description doc
libcdio documentation files

%description
GNU Compact Disc Input and Control Library

%prep
%autosetup -p1 -n ${name}-${version}/upstream

%build
./autogen.sh --prefix=/usr
%configure --enable-maintainer-mode
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/cd-read
%{_bindir}/cd-info
%{_bindir}/cd-drive
%{_bindir}/iso-read
%{_bindir}/iso-info
%{_bindir}/mmc-tool
%{_libdir}/libiso9660++.so.0.0.0
%{_libdir}/libudf.so.0
%{_libdir}/libcdio.so.19.0.0
%{_libdir}/libudf.so.0.0.0
%{_libdir}/libcdio++.so.1
%{_libdir}/libcdio++.so.1.0.0
%{_libdir}/libiso9660.so.11.0.0
%{_libdir}/libiso9660.so.11
%{_libdir}/libcdio.so.19
%{_libdir}/libiso9660++.so.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/cdio/bytesex.h
%{_includedir}/cdio/rock.h
%{_includedir}/cdio/version.h
%{_includedir}/cdio/mmc_hl_cmds.h
%{_includedir}/cdio/audio.h
%{_includedir}/cdio/iso9660.h
%{_includedir}/cdio/disc.h
%{_includedir}/cdio/cdio_config.h
%{_includedir}/cdio/mmc_util.h
%{_includedir}/cdio/mmc_ll_cmds.h
%{_includedir}/cdio/cdio.h
%{_includedir}/cdio/dvd.h
%{_includedir}/cdio/util.h
%{_includedir}/cdio/xa.h
%{_includedir}/cdio/mmc.h
%{_includedir}/cdio/udf_file.h
%{_includedir}/cdio/bytesex_asm.h
%{_includedir}/cdio/udf_time.h
%{_includedir}/cdio/ds.h
%{_includedir}/cdio/udf.h
%{_includedir}/cdio/logging.h
%{_includedir}/cdio/posix.h
%{_includedir}/cdio/memory.h
%{_includedir}/cdio/mmc_cmds.h
%{_includedir}/cdio/read.h
%{_includedir}/cdio/ecma_167.h
%{_includedir}/cdio/track.h
%{_includedir}/cdio/device.h
%{_includedir}/cdio/cd_types.h
%{_includedir}/cdio/types.h
%{_includedir}/cdio/sector.h
%{_includedir}/cdio/utf8.h
%{_includedir}/cdio/cdtext.h
%{_includedir}/cdio++/disc.hpp
%{_includedir}/cdio++/devices.hpp
%{_includedir}/cdio++/mmc.hpp
%{_includedir}/cdio++/iso9660.hpp
%{_includedir}/cdio++/enum.hpp
%{_includedir}/cdio++/cdtext.hpp
%{_includedir}/cdio++/device.hpp
%{_includedir}/cdio++/cdio.hpp
%{_includedir}/cdio++/read.hpp
%{_includedir}/cdio++/track.hpp
%{_libdir}/libudf.a
%{_libdir}/libudf.la
%{_libdir}/pkgconfig/libiso9660++.pc
%{_libdir}/pkgconfig/libcdio++.pc
%{_libdir}/pkgconfig/libcdio.pc
%{_libdir}/pkgconfig/libudf.pc
%{_libdir}/pkgconfig/libiso9660.pc
%{_libdir}/libcdio++.so
%{_libdir}/libiso9660++.a
%{_libdir}/libiso9660.la
%{_libdir}/libcdio.la
%{_libdir}/libcdio.so
%{_libdir}/libiso9660++.so
%{_libdir}/libiso9660.a
%{_libdir}/libiso9660++.la
%{_libdir}/libcdio++.a
%{_libdir}/libudf.so
%{_libdir}/libcdio++.la
%{_libdir}/libcdio.a
%{_libdir}/libiso9660.so

%files doc
%defattr(-,root,root,-)
%{_infodir}/libcdio.info.gz
%{_mandir}/man1/cd-drive.1.gz
%{_mandir}/man1/iso-info.1.gz
%{_mandir}/man1/cd-info.1.gz
%{_mandir}/man1/iso-read.1.gz
%{_mandir}/man1/cd-read.1.gz

