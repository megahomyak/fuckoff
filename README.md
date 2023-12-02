# FuckOff

Recognizes when you show a middle finger to the camera

## Installation

`pip install fuckoff`

## Usage

```python
from fuckoff import FuckOff

with FuckOff() as fuckoff:
    while True:
        fuckoff.wait()
        print("Middle finger detected!")
```

* Be aware that when using `FuckOff` and your camera is not working, a `CameraIsNotWorking` exception will be thrown
