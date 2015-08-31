talsub (This American Life with Subtitles)
=====

Project Description
-----
This project adds subtitles to This American Life (TAL) episodes. To do this, I used a web crawling library (Scrapy) to crawl TAL transcript pages and scrape episode information from them. This data is stored in a MongoDB database according to the layout described in the `data` module. The subtitles are served through a Django web application to web clients through javascript GET requests.

Unfortunately, TAL sometimes updates the audio for a podcast without updating the tags for timing in their transcript. This is especially true for later episodes. Most of the early episodes work well; I tested the first 10 with good results and jumped around the first 300 without running into any trouble.

Hope you enjoy!

Development Setup
-----
This application was developed on Windows 8.1, thus the development instructions will be geared toward that setup. These instructions will enable you to run the debug web application from your local machine and test on localhost:8000.

1. Install Python 2.7 32-bit
2. Install pip
  * https://pip.pypa.io/en/latest/installing.html
3. I recommend use of virtualenv
4. `pip install -r \path\to\requirements.txt`
5. Copy template.config.ini to config.ini and configure. (If you were invited here by me, I probably gave you this.)
6. If you would like to use a local MongoDB service for debugging, install MongoDB
  * http://www.mongodb.org/downloads

The above instructions will allow you to run the web server locally with `python manage.py runserver` provided the working directory is `path\to\TalSub\web` and `path\to\TalSub` is in the `PYTHONPATH`.

If you would like to run the spiders, you will need additional packages that are difficult to install on Windows due to the lack of a C compiler. I've included the trouble packages in `path\to\TalSub\windows_packages`. Follow these additional steps:

1. Install Visual C++ 2008 Redistributables by running vcredist_x86.exe
2. Install OpenSSL by running Win32OpenSSL-1\_0_1j.exe
3. Then, from virtualenv (if using one) run:
    1. `easy_install pywin32-219.win32-py2.7.exe`
    2. `easy_install Twisted-15.3.0.win32-py2.7.exe`
    3. `easy_install zope.interface-4.1.2-py2.7-win32.egg`
    4. `easy_install lxml-3.4.4.win32-py2.7.exe`
    5. `easy_install pyOpenSSL-0.11-py2.7-win32.egg`
4. `pip install -r \path\to\all.requirements.txt`
5. Add `\path\to\TalSub\spiders\episode\episode` to PYTHONPATH

Run the spider with `\path\to\TalSub\spiders\episode\episode\run.py`. By default, this will crawl episodes 1 to 538. To limit the scope, alter the `EpisodeSpider` constructor call in run.py as described in the comments.
