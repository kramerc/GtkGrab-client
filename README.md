GtkGrab - Screenshot Uploader
=============================

GtkGrab takes screenshots and automatically uploads them. GtkGrab is split up
into two components, the client and the server. You can find the server
component on
[http://github.com/kokx/GtkGrab-server](http://github.com/kokx/GtkGrab-server).

Version 0.3.2, Created by Evan Coury and Pieter Kokx.

Update notice
=============

If you are updating GtkGrab, you probably need to update your `config.cfg`
(see the samples).

Introduction
============
GtkGrab is an open source tool for Linux and Mac that takes a screenshot of a
window or specified area of the screen, uploads it to a web server of your
choice, and copies the URL to your clipboard automatically. Once you start
using it, you'll wonder how you got along without it. GtkGrab is essentially a
free and open source version of the commercial TinyGrab.com software/service,
except that it also works on Linux and you don't have to pay to use your own
server. The name GtkGrab implies that it may only work in GTK-based desktop
environment such as Gnome, however this is no longer the case (though it was
originally). To be clear, GtkGrab has been tested to work on Linux running
both Gnome and KDE as well as on Mac OSX.

Usage Instructions
==================
* Press your specified keyboard shortcut.
* On Linux: Either click and drag to specify an area of the screen to capture,
  or click on the title of a window to capture just that window.
* On Mac: Use the space bar to toggle between mouse and window selection
  modes.
* Within a few seconds, you should get an unobtrusive notification that your
  screenshot has been uploaded and that the URL has been copied to your
  clipboard.

Installation instructions
=========================

Arch Linux
----------

For Arch Linux, there is a PKGBUILD available on the
[AUR](http://aur.archlinux.org/packages/gtkgrab-client).

Note that you still have to [configure](#configuration) GtkGrab.

Manual installation
-------------------

First, make sure you have all dependencies installed:

* python2.7
* xclip
* Screenshot program (scrot by default)

Download the latest release from the [releases
page](http://github.com/kokx/GtkGrab-client/releases/), or use git to obtain
the latest (development) version.

Finally, go to the directory where you have downloaded and unpacked the source to, and
run:

```bash
python setup.py install --optimize=1
```

Specific Mac OS X instructions
------------------------------

* Install Growl and growlnotify from http://growl.info/
* Use automator to run `GtkGrab` via the keyboard shortcut of your choice.
  Instructions for this can be found
  [here](http://www.macosxautomation.com/services/learn/tut01/index.html),
  except where it says to select "Launch Application", you should select "Run
  Shell Script" instead.

Configuration
=============

Now you should configure GtkGrab using one of the sample configuration files
in `/usr/share/GtkGrab-client/`.

When you have configured GtkGrab, you can execute the `GtkGrab` command to
test it.

Keyboard shortcut
-----------------
In GNOME, you can configure the GtkGrab command as a shortcut via `System >
Preferences > Keyboard Shortcuts`.


Screenshot tool
===============
By default, GtkGrab uses scrot for making screenshots. And it will, by
default, only make screenshots of a selected area. But there is a 'command'
configuration directive. You can change this to any screenshot command that
saves a screenshot to the given path `%s`.

Amazon S3 Upload Support
========================
GtkGrab supports using `s3cmd` (available in ruby-gems) to upload screenshots
to Amazon S3. This feature still has to be documented properly for usage with
the installed GtkGrab.

Animated GIF Support
====================
GtkGrab optionally supports recording an animated GIF of your screen. This
requires a few extra dependencies to work properly:

* [zenity](https://help.gnome.org/users/zenity/stable/) for prompting how long
  to record for.
* [xrectsel](https://github.com/lolilolicon/FFcast2/blob/master/xrectsel.c) for
  selecting the area to record.
* [byzanz](https://git.gnome.org/browse/byzanz/) for actually recording the gif
  (available in the Fedora base repo).

Currently, due to laziness, it uploads the gifs as png files, but they still
display fine in any modern browser.

Also due to laziness, the gif support only works on Linux, not Mac. Mac/Windows
support could be possible via [LICEcap](http://www.cockos.com/licecap/)
possibly.

To use GtkGrab in gif mode, simply invoke it with `GtkGrab gif`.

Troubleshooting
===============

* P: After taking a screenshot no notification is displayed, when running it
  from the command line the error 'sh: notify-send: not found'
* A: Install notify-osd libnotify-bin via your package manager
* P: ImportError: No module named ConfigParser
* A: GtkGrab wants python2 but your default is python3, you need to change the
  first line in `GtkGrab` to point to your python2, /usr/bin/python2 for
  example
* P: Binding a keyboard shortcut in GNOME doesn't work.
* A: This is an issue with scrot. To solve this, try setting the command option
  in the config file to `sleep 0.5 && scrot --b -s %s`. For more information
  see [this](http://ubuntuforums.org/showthread.php?t=1881234) and
  [this](https://bbs.archlinux.org/viewtopic.php?id=143065) and
  [this](https://bbs.archlinux.org/viewtopic.php?id=159900) and
  [this](https://groups.google.com/forum/#!topic/linux.debian.bugs.dist/_tmJIFYBfZo).

License
=======

GtkGrab is released under the terms of the [GNU General Public License (GPL)
Version 3](http://en.wikipedia.org/wiki/GNU_General_Public_License). See
`COPYING` file for details.
