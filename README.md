# Check battery

This is a simple Python application intended to keep the computer battery in good health, therefore inform the user about the moment of being charged to 80%, and discharged at 20%.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install requirements.txt
```

#### System dependencies

For Ubuntu:

eSpeak:
```
apt-get install espeak
```
Notify-send:
```
apt-get install notify-osd
```

### Installing

In order to run the application, run the command:

```
$ python3 main.py
```

if you wish to have other parameters than default 20-80%, you could use optional parameters: 
  -s S        This is the minimum charge level
  -e E        This is the maximum charge level
  -o          Perform only once

e.g.

```
$ python3 main.py -s 30 -e 90 -o
```