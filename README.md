# RSA

Public private key based something :-)

## Setup Instructions

The code requires python 3.6 or greater and fpylll (https://github.com/fplll/fpylll). Ideally it should be setup within a python virtual
environment.

### 1. Install virtualenv

```bash
    sudo apt install virtualenv
```

### 2. Install python 3.6 and other required packages

Python 3.6 is part of ubuntu 16.10 and greater packages and can be installed by running:

```bash
    sudo apt install python3.6 python3.6-dev git automake autoconf libmpfr-dev
```

### 3. Create virtual environment and activate it

```bash
    virtualenv -p python3.6 py36venv
    source python36venv/bin/activate
```

### 4. Install fpylll

Fpylll install instructions are here: https://github.com/fplll/fpylll and are repeated here
for comprehensiveness.

```bash
    git clone git@github.com:fplll/fpylll.git
    cd fpylll
    ./install-dependencies.sh $VIRTUAL_ENV
    pip install Cython
    pip install -r requirements.txt
    pip install -r suggestions.txt
```

Now build the python extension.

```bash
    export PKG_CONFIG_PATH="$VIRTUAL_ENV/lib/pkgconfig:$PKG_CONFIG_PATH"
    python setup.py build_ext
    python setup.py install
```


### 5. Running fpylll

Whenever you want to use fpylll, make sure to activate virtual env and append the
lib location to LD_LIBRARY_PATH env variable

```bash
    source /MyWork/Projects/py36venv/bin/activate
    export LD_LIBRARY_PATH="$VIRTUAL_ENV/lib"
    ipython
```