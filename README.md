# PSE-Django-CFE-Test

To resolve the cross-platform issues a pure python codebase using django and the Chrome embedded Framework (CEF) can be used for our project.
This includes tarting a viewer and the django server, which is working
1. Natively on a Windows machine
2. Inside the WSL2 on that same machine by literally running the same script, even with output to an xfce Desktop with a local RDP connection
3. By starting the server and the UI inside the WSL2 as described above and using it from a normal browser on the native Windows host
4. By starting the server on the Windows host and viewing the site in a WSL2 browser

This repository contains a sample minimal django application with our GUI.
It uses the CEF via cefpython in order to open a window displaying only our own site.
Therefore a recent installation of chrome/chromium is needed, although binaries can be added to the repository later.

The usage is rather simple:
1. Clone the repository
2. create a virtual environment (venv) with python3.7
  1. You can install python 3.7 by adding a repo that still has the package for it: 
  `sudo apt update`
  `sudo apt install software-properties-common`
  `sudo add-apt-repository ppa:deadsnakes/ppa`
  `sudo apt install python3.7`
  2. then create a virtual environment with `python3.7 -m venv test-venv`
  3. and activate it using `./test-venv/bin/activate`
3. then install the dependencies:
`python3.7 -m pip install --upgrade pip`
`python3.7 -m pip install -r requirements.txt`
4. and run the program:
`python3.7 launch.py`

Directories may not be right in the code above.
Also there are currently two windows opening, because the django server notices that a different process is called in launch (the CEF needs its own process so we can start it and get rid of it and advance the code in order to start the server)
(This may be possible with simple threads but I only tried it with processes until now), and reruns the script somehow?! I don't get it yet how that works...
