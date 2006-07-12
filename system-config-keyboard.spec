Summary: A graphical interface for modifying the keyboard
Name: system-config-keyboard
Version: 1.2.7
Release: 1.1.1
URL: http://fedora.redhat.com/projects/config-tools
License: GPL
ExclusiveOS: Linux
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Source0: %{name}-%{version}.tar.bz2
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
Obsoletes: kbdconfig
Obsoletes: redhat-config-keyboard
ExcludeArch: s390 s390x ppc64
Requires: python2
Requires: usermode >= 1.36
Requires: rhpl >= 0.53
Requires: pyxf86config
Prereq: gtk2 >= 2.6

%description
system-config-keyboard is a graphical user interface that allows 
the user to change the default keyboard of the system.

%prep
%setup -q

%install
make INSTROOT=$RPM_BUILD_ROOT install
desktop-file-install --vendor system --delete-original      \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category Application \
  --add-category SystemSetup \
  --add-category X-Red-Hat-Base          \
  $RPM_BUILD_ROOT%{_datadir}/applications/system-config-keyboard.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%preun
if [ -d /usr/share/system-config-keyboard ] ; then
  rm -rf /usr/share/system-config-keyboard/*.pyc
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root)
#%doc COPYING
#%doc doc/*
/usr/bin/system-config-keyboard
%dir /usr/share/system-config-keyboard
/usr/share/system-config-keyboard/*
%dir /usr/share/firstboot/
%dir /usr/share/firstboot/modules
/usr/share/firstboot/modules/*
%attr(0644,root,root) %{_datadir}/applications/system-config-keyboard.desktop
%attr(0644,root,root) %config /etc/security/console.apps/system-config-keyboard
%attr(0644,root,root) %config /etc/pam.d/system-config-keyboard
%attr(0644,root,root) %{_datadir}/icons/hicolor/48x48/apps/system-config-keyboard.png

%changelog
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.7-1.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Oct 20 2005 Paul Nasrat <pnasrat@redhat.com> - 1.2.7-1
- Update pam file (#170630)
- New firstboot module
- Compiled python

* Thu Sep 15 2005 Jeremy Katz <katzj@redhat.com> - 1.2.6-3
- exclude ppc64 since we don't have X stuff there

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1.2.6-2
- silence %%post

* Fri Apr 01 2005 Paul Nasrat <pnasrat@redhat.com> - 1.2.6-1
- Translations
- Gtk deprecations

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1.2.5-2
- Update the GTK+ theme icon cache on (un)install

* Fri Oct 08 2004 Paul Nasrat <pnasrat@redhat.com> - 1.2.5-1
- Firstboot fix for xorg.conf

* Fri Oct 01 2004 Paul Nasrat <pnasrat@redhat.com> - 1.2.4-1
- Translations 

* Wed Sep 22 2004 Jeremy Katz <katzj@redhat.com> - 1.2.3-1
- fix traceback when using treeview typeahead (#133178)

* Tue Sep 07 2004 Paul Nasrat <pnasrat@redhat.com> 1.2.2-1
- i18n desktop

* Thu Apr  8 2004 Brent Fox <bfox@redhat.com> 1.2.1-2
- fix icon path (bug #120175)

* Wed Nov 12 2003 Brent Fox <bfox@redhat.com> 1.2.1-1
- renamed from redhat-config-keyboard
- add Obsoletes for redhat-config-keyboard
- make changes for Python2.3

* Mon Oct 13 2003 Brent Fox <bfox@redhat.com> 1.1.5-2
- pull in Croatian translation (bug #106617)

* Thu Aug 14 2003 Brent Fox <bfox@redhat.com> 1.1.5-1
- tag on every build

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.1.3-2
- bump release and rebuild

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.1.3-1
- mark string for translation

* Tue Jul  1 2003 Brent Fox <bfox@redhat.com> 1.1.2-2
- bump version and rebuild

* Tue Jul  1 2003 Brent Fox <bfox@redhat.com> 1.1.2-1
- fix formatting problem (bug #97873)
- create an XkbOption if it doesn't exist (bug #97877)

* Wed May 21 2003 Brent Fox <bfox@redhat.com> 1.1.1-2
- made a typo in redhat-config-keyboard.py

* Wed May 21 2003 Brent Fox <bfox@redhat.com> 1.1.1-1
- Created a command line interface
- updated all copyright dates

* Wed Apr  2 2003 Brent Fox <bfox@redhat.com> 1.0.5-1
- pass window size into rhpl

* Wed Mar  5 2003 Brent Fox <bfox@redhat.com> 1.0.4-1
- add functions in keyboard_gui.py for anaconda popup mode

* Wed Feb 12 2003 Jeremy Katz <katzj@redhat.com> 1.0.3-4
- fixes for tui cjk (#83518)

* Tue Feb  4 2003 Brent Fox <bfox@redhat.com> 1.0.3-3
- change packing order a little for firstboot reconfig mode

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.0.3-2
- bump and build

* Wed Jan 22 2003 Brent Fox <bfox@redhat.com> 1.0.3-1
- add a us keymap to keymaps with non-latin chars (bug #82440)
- write out the XkbVariant line if it is present
- handle XkbOptions to allow toggling between keymaps

* Mon Dec 23 2002 Brent Fox <bfox@redhat.com> 1.0.2-1
- add a textdomain for rhpl so we pull in translations (bug #78831)

* Thu Dec 12 2002 Brent Fox <bfox@redhat.com> 1.0.1-9
- remove requires for pygtk2 since we have a text mode now

* Wed Dec 11 2002 Brent Fox <bfox@redhat.com> 1.0.1-8
- fall back to text mode if gui mode fails

* Tue Nov 12 2002 Brent Fox <bfox@redhat.com> 1.0.1-7
- pam path changes

* Thu Nov 07 2002 Brent Fox <bfox@redhat.com> 1.0.1-6
- Add keyboard_backend.py to cvs

* Thu Oct 31 2002 Brent Fox <bfox@redhat.com> 1.0.1-5
- Obsolete kbdconfig

* Wed Oct 09 2002 Brent Fox <bfox@redhat.com> 1.0.1-4
- Added a tui mode - keyboard_tui.py
- Moved some non-UI code to keyboard_backend.py

* Fri Oct 04 2002 Brent Fox <bfox@redhat.com> 1.0.1-3
- Add a window icon
- set selection mode to browse

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-1
- Make no arch

* Wed Aug 14 2002 Brent Fox <bfox@redhat.com> 0.9.9-6
- rebuild for translations

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 0.9.9-5
- fix textdomain so translations show up correctly

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 0.9.9-4
- pull translations into desktop file

* Mon Aug 12 2002 Tammy Fox <tfox@redhat.com> 0.9.9-3
- Replace System with SystemSetup in desktop file categories

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.9.9-2
- Fix ordering of layout and model.  Fixes bug 71067

* Thu Aug 08 2002 Brent Fox <bfox@redhat.com> 0.9.9-1
- Added Requires for pyxf86config

* Fri Aug 02 2002 Brent Fox <bfox@redhat.com> 0.9.8-1
- Make changes for new pam timestamp policy

* Thu Aug 01 2002 Brent Fox <bfox@redhat.com> 0.9.7-2
- sort the list by the full keyboard name, not the keymap

* Thu Aug 01 2002 Brent Fox <bfox@redhat.com> 0.9.7-1
- make calls to pyxf86config to update XF86Config file

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-3
- fix Makefiles and spec files so that translations get installed

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-2
- update spec file for public beta 2

* Tue Jul 23 2002 Brent Fox <bfox@redhat.com> 0.9.6-1
- put desktop file in correct location

* Mon Jul 22 2002 Jeremy Katz <katzj@redhat.com> 0.9.5-2
- add scrollto hack back

* Fri Jul 19 2002 Brent Fox <bfox@redhat.com> 0.9.5-1
- add version dependency for pygtk2 API change

* Thu Jul 18 2002 Jeremy Katz <katzj@redhat.com> 0.9.4-3
- add fix for list store changes in new pygtk2

* Tue Jul 16 2002 Brent Fox <bfox@redhat.com> 0.9.4-2
- bump rev num and rebuild

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 0.9.3-2
- Update changelogs and rebuild

* Mon Jul  1 2002 Jeremy Katz <katzj@redhat.com> 0.9.3-1
- add wacky scrollto hack so that the screen in the installer scrolls properly

* Mon Jul 01 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Bump rev number

* Mon Jul 1 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Wrap the destroy call in a try/except because there is no self.mainWindow in firstboot reconfig mode

* Wed Jun 26 2002 Brent Fox <bfox@redhat.com> 0.9.1-1
- Fixed description

* Tue Jun 25 2002 Brent Fox <bfox@redhat.com> 0.9.0-5
- Create pot file

* Mon Jun 24 2002 Brent Fox <bfox@redhat.com> 0.9.0-4
- Fix spec file

* Fri Jun 21 2002 Brent Fox <bfox@redhat.com> 0.9.0-3
- Print init message on debug mode

* Thu Jun 20 2002 Brent Fox <bfox@redhat.com> 0.9.0-2
- Pass doDebug into launch instead of setupScreen
- Add snapsrc to Makefile

* Tue Jun 18 2002 Brent Fox <bfox@redhat.com> 0.9.0-1
- Create a way to pass keymap name back to firstboot

* Wed May 29 2002 Brent Fox <bfox@redhat.com> 0.2.0-3
- Make symbolic link in /usr/share/firstboot/modules point to keyboard_gui.py

* Tue May 28 2002 Jeremy Katz <katzj@redhat.com>
- changes to be usable within an anaconda context 

* Tue Dec 05 2001 Brent Fox <bfox@redhat.com>
- initial coding and packaging

