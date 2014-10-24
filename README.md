talsub (This American Life with Subtitles)
=====

Development Setup
-----
This application was developed on Windows 7, thus the development instructions will be geared toward that setup. These instructions will enable you to run web application.

1. Install Python 2.7 32-bit
2. Install pip
  * https://pip.pypa.io/en/latest/installing.html
3. I recommend use of virtualenv
4. `pip install -r \path\to\requirements.txt`
5. Copy template.config.ini to config.ini and configure. If you were invited here by me, I probably gave you this.
6. If you would like to use a local MongoDB service for debugging, install MongoDB
  * http://www.mongodb.org/downloads

The above instructions will allow you to run the web server locally with `python manage.py runserver` provided the working directory is `path\to\TalSub\web` and `path\to\TalSub` is in the `PYTHONPATH`.

If you would like to run the spiders, you will need additional packages that are difficult to install on Windows due to the lack of a C compiler. I've included the trouble packages in `path\to\TalSub\windows_packages`. Follow these additional steps:

1. Install Visual C++ 2008 Redistributables by running vcredist_x86.exe
2. Install OpenSSL by running Win32OpenSSL-1\_0_1j.exe
3. Then, from virtualenv (if using one) run:
    1. `easy_install pywin32-219.win32-py2.7.exe`
    2. `easy_install Twisted-14.0.2.win32-py2.7.exe`
    3. `easy_install zope.interface-4.1.1-py2.7-win32.egg`
    4. `easy_install lxml-3.4.0.win32-py2.7.exe`
    5. `easy_install pyOpenSSL-0.11-py2.7-win32.egg`
4. `pip install -r \path\to\all.requirements.txt`