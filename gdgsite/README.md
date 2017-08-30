## How to setup

Follow this guide to setup this project on your local machine.

1. Install [python] 3.x, git and [virtualenv] in your computer.

2. Get the source code on your machine by-

	`https://github.com/GDG-JSS-NOIDA/website.git`

3. Create a python virtual environment and install python and django related dependencies.

    ```shell
    cd gdgsite
    virtualenv venv
    source venv/bin/activate  # run this command everytime before starting on the project
    pip install -e django/ # this will install the required django version
    pip install -r requirements/dev.txt
    ```

[virtualenv]: https://virtualenv.pypa.io/
[python]: https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
