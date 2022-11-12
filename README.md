# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

SD logger - for logging data to SD card on CircuitPython projects.

## Usage <a name = "usage"></a>

'''
from SdLogger import SdLogger

logger = SdLogger()

i = 0
while i < 5000:
i+=1
logger.log_data(i)
print(f'Logging: {i}')

logger.close()
'''
