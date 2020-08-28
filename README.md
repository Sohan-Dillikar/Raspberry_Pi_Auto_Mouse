# Raspberry Pi Auto Mouse

## Important!

For this project you will need to install a couple modules.  One of the modules needed is already given in the "Modules" folder of this repository.  To install the other modules, make sure you watch the youtube video I made for this project [here](https://www.youtube.com/channel/UCKoQohlSLnq11GT_oJ6BcYg?view_as=subscriber).

In this project, I have created a joystick controlled mouse using the Raspberry Pi.  The mouse is controlled by a joystick and an ultrasonic sensor.  The joystick obviously moves the mouse based on the direction given and the ultrasonic sensor helps the mouse scroll up and down.  If you place your hand 5cm or less in front of the ultrasonic sensor, then your mouse will scroll down.  If you place your hand within 5cm to 10cm in front of the sensor, then your mouse will scroll up.  I have added two potentiometers to this project as well.  The first potentiometer controls the mouse moving speed and the second potentiometer controls the mouse scrolling speed.  For this project, you will need some kind of Analog to Digital Converter Module (ADC).  I used an ADS7830.

Materials :
  - Basic Materials :
    - [Raspberry Pi](https://www.amazon.com/CanaKit-Raspberry-Starter-Premium-Black/dp/B07BCC8PK7/ref=sr_1_1_sspa?dchild=1&keywords=raspberry+pi+3&qid=1597708898&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMVJaMVVMMFQxTDJNJmVuY3J5cHRlZElkPUEwMzI5MzA0VTVHQUY5R0I3WVNKJmVuY3J5cHRlZEFkSWQ9QTA3NTAxMjAzTUIyNzBOUEVKVk9JJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
    - [Breadboard](https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/ref=sr_1_1_sspa?dchild=1&keywords=breadboard&qid=1597709033&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzJGSEpMRU1TSjNLJmVuY3J5cHRlZElkPUEwODI2MDcwM0I3NjBXOUtRSUxHQyZlbmNyeXB0ZWRBZElkPUEwNTI0ODkxMTVLQVI1Vk9QVEE5OCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
    - [Python3](https://www.python.org/)
    - RPi.GPIO Module
    - Monitor, Keyboard, Mouse
  - Project Components
    - [Joystick Module](https://www.amazon.com/WGCD-Joystick-Breakout-Controller-Arduino/dp/B01N59MK0U/ref=sr_1_2_sspa?crid=3HJ0XBLELS3SS&dchild=1&keywords=joystick+module&qid=1598636392&sprefix=joysti%2Caps%2C225&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQRE40WEFRNTVHQVomZW5jcnlwdGVkSWQ9QTA5MjkwMzgxQUU2UjI5TVFYUU5LJmVuY3J5cHRlZEFkSWQ9QTA1NTE5NzYzQzFCTkcyVlhZMTdCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==) x1 (x10 Pack!)
    - [Ultrasonic Sensor](https://www.amazon.com/Smraza-Ultrasonic-Distance-Mounting-Duemilanove/dp/B01JG09DCK/ref=sr_1_1_sspa?crid=2EBBARQXLGE9X&dchild=1&keywords=ultrasonic+sensor&qid=1598636481&sprefix=ultrasonic+sensor%2Caps%2C231&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNlI0VlhYRkZBV01QJmVuY3J5cHRlZElkPUEwMzUwMDUwMlRBREVWT1JROUcyWiZlbmNyeXB0ZWRBZElkPUEwNDIyMDEyMjNLSDE1TkdLU0lJQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) x1 (x5 Pack with Sensor Holders + Jumper Wires!)
    - [Potentiometer](https://www.amazon.com/Uxcell-a15011600ux0235-Linear-Rotary-Potentiometer/dp/B01DKCUVMQ/ref=sr_1_10?crid=2SQWKWKZIW5X4&dchild=1&keywords=potentiometer&qid=1598636606&sprefix=potentiomater%2Caps%2C235&sr=8-10) x2 (x5 Pack!)
    - [ADC Module](https://www.amazon.com/Converter-Programmable-Amplifier-Development-Raspberry/dp/B07TGB6KF8/ref=sr_1_5?dchild=1&keywords=adc+module&qid=1598636682&sr=8-5) x1 (x2 Pack!)
    - [Jumper Wires](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY/ref=sr_1_3?dchild=1&keywords=jumper+wires&qid=1598636986&sr=8-3)
  - Optional :
    - [Breadboard T-Type Extention](https://www.amazon.com/Kuman-Expansion-Raspberry-Solderless-Breadboard/dp/B074DSMPYD/ref=sr_1_8?dchild=1&keywords=breadboard+extension&qid=1597765374&sr=8-8) x1 (Comes with Mini Breadboard + Jumper Wires!)
