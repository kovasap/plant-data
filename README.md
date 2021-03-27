# Plant Data Management Utilities

## Periodic Picture Taking

Add this line
```
0 * * * * ~/plant-data/take_picture.bash
```
to `crontab -u pi -e`.

Useful references:

 - https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md


## Temperature and Humidity Sensing

Uses `pigpio`, which requires you to start a daemon with `sudo pigpiod` to
work.


## Google Sheets Integration

Need to follow
https://denisluiz.medium.com/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e
to set things up properly (see also
https://github.com/juampynr/google-spreadsheet-reader).
