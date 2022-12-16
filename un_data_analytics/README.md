# UN_Data_Analytics


It is a Data analytics project on United Nations dataset

## How to Run this Project on your local machine

```
cd existing_repo
git remote add origin https://gitlab.com/mountblue/cohort-22-python/dikshant/un_data_analytics.git
git branch -M main
git push -uf origin main
```


## Enviroment Setup

* #### **Software Installation**

If python is not installed in your Machine, install python by typeing in command line,

To check type:

```
python --version

```

if it shows python version means python is already installed in your system, else

if you are a unix user

```
sudo apt-get install python3

```

and then type

```
python-is-python3
```

then check for pip is installed or not

```
pip --version
```

if it is not installed type in CLI

```
sudo apt install python-pip
```

or

```
sudo apt install python3-pip
```

* #### **Create a Virtual Enviroment.** 

Its not necessary to create virtual enviroment but its a good practice to create a virtual enviroment for every new project you are starting with
to avoid any dependency issue.

Follow these steps to create virtual enviroment

```
python -m venv environment_name

```

if this dosn't work try:

```
python3 -m venv environment_name
```

then activate the enviroment,

```
source enviroment_name/bin/activate
```


this will activate your enviroment

* #### **Install Required Libraries**

Open terminal and in command line type 

```
pip install matplotlib
```

* #### **Run project**

To run any question type in CLI 

```
python file_name.py
```

for e.g.

```
python Q1.py
```


