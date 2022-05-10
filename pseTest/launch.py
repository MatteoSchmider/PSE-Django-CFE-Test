import os
from cefpython3 import cefpython as cef
import platform
import sys
from multiprocessing import Process




def main():
    viewer = Process(target=start_cef_viewer, args=())
    viewer.start()
    start_django_server()
    viewer.join()


def start_cef_viewer():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="http://127.0.0.1:8000/", window_title="ChipScanner")
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
        ver=platform.python_version(),
        arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


def start_django_server():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pseTest.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    args = ['manage.py', 'runserver', '127.0.0.1:8000']
    execute_from_command_line(args)


if __name__ == '__main__':
    main()
