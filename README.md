# Unihiker M10 HMI Power Meter Gauge

### ![](images/Unihiker-M10-HMI-Gauge.jpg)

### Introduction

In Italy we have a problem with the electricity supply: every house has a power meter that automatically cuts off the power if the total load in the home is greater than 3kW + 10% (3.3kW)

>  We have a voltage of 220÷240VAC, to this means your home appliances can draw a maximum of 15A in total. There are also contracts allowing 4.5 or 6kW and so on, but the 3kW one is the most diffused amog the italian domestic population. 

Due this, the meter cuts off the power very often if you simultaneously turn on two appliances requiring high current values such as a washing machine + oven or an hairdryer + the dishwasher and so on.  This means you have to go out every time to reset the meter, which is really annoying.

Lot of time ago I engineered a smart-home system in my house, I improved it over years and it runs entirely on [Node-Red](https://nodered.org/) , [Mosquitto ](https://mosquitto.org/) and [Tasmota](https://tasmota.github.io/docs/). I have all the high-current demand appliances connected through their own smart plugs: this allows me to turn them on/off and measure the current load for each device. 

Recently I added a (sponsored link) [Nous D3T current meter](https://amzn.to/4aXbdN5) at the top of the electrical system so I can make the system raise an alarm when the total power consuption is near the limit: in this case I can detach a device and I could do this also automatically through node-red, since I know which appliances are drawing power through the smart plugs. 

Alarm is rised through a buzzer attached to the Raspberry Pi running Node-Red and also through a Telegram message using a bot. But... the Raspberry Pi is located in my laboratory and Telegram bot sometimes don't works properly and messages are sent lot of time after the alarm occurred.

I thought to build a small smart device showing the actual current load, and I used an [Unihiker M10](https://www.unihiker.com/products/m10) . The Unihiker M10 has a 320x240px color display, is powerful and runs on Debian, so you can use  python directly (not *Micropython* or *Circuitpython*) with powerful graphical libraries (such as the one I used: [pygame](https://www.pygame.org/wiki/about)). 

The power load value is taken from an MQTT topic directly from the current meter or from a Node-Red generated topic. Result is very cool and you have a sound alarm if the limit is reached: so this gadget is very useful to be placed wherever you want (I placed it in the kitchen, where the great part of high current demand appliances is located)

### Enclosure design

I designed the enclosure using Onshape. I spent lot of time and effort for having a functional and cute enclosure. Actually the enclosure is made of 3 parts: the main body, a lid, and a cradle that allows to have the Unihiker M10 slightly tilted backwards allowing a better view of the display.

I shared all info about the enclosure, 3mf file for Bambulab 3D-Printers and STL files on my makerworld page. You can find it here: 

[Unihiker M10 enclosure for HMI Gauge](https://makerworld.com/it/models/2261736-unihiker-m10-enclosure-for-hmi-gauge)

### Code Setup

Copy the entire *gauge_hmi* folder of the repo on your computer in order to prepare files. 

Paste in the *gauge_hmi/assets* folder the font file `Anta-Regular.ttf` that you can download from [Google Fonts](https://fonts.google.com/specimen/Anta).

Paste in the *gauge_hmi/assets* folder a your own png splash image having a resolution of 240x320 pixels. The name of this file is contained in `config.py` and default is `splash_240x320.png`

Copy the file `credentials.py` as `mycredentials.py` and then edit it by writing your own Wi-Fi SSID and Password and MQTT User and Password

> I was not able to connect to my own MQTT Broker having user and password, I was able to connect only when I removed the password. I don't understand if it was my own problem or a code issue but you know: if you've problem connecting your MQTT broker... try to remove user and password.

Edit `config.py` by changing MQTT parameters and all other parameters for suit your own needs (keep always an original copy of config.py)

Now you can transfer the entire *gauge_hmi* folder on the unihiker *home/* folder.

The file `hmi_launcher.py` contained in repo *root* has to be copied in *root/* folder on the unihiker.

Then follow the instructions in [unihiker/root/README.md](unihiker/root/README.md) for achieving the autostart of the HMI gauge on Unihiker boot.

### Source Code

in progress
