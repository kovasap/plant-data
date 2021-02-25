# Plant Data Management Utilities

## Periodic Picture Taking

Add this line
```
0 * * * * ~/plant-data/take_picture.bash
```
to `crontab -u pi -e`.

Useful references:

 - https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
