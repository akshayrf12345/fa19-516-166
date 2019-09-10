The steps below are for how to install a virtual Python environment on Windows 10

1. Follow the steps at '<https://docs.microsoft.com/en-us/windows/wsl/install-win10>'
2. Install and run this version of Ubuntu '<https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab>'
3. Run the Ubuntu program. It will take a while for the initial setup
4. Update Python by typing in the follow commands into the Linux shell:

```bash
$ sudo apt-get update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get install python3.7 python3-dev python3.7-dev
```

5. Now create the virtual environment using the following commands:

```bash
$ python3.7 -m venv --without-pip ~/ENV3
```

6. Edit the ~/.bashrc file and add the line

```bash
alias ENV3="source ~/ENV3/bin/activate"
ENV3
```

7. Finally install PIP into the environment with the commands

```bash
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python get-pip.py
$ rm get-pip.py
```
