Copy the file `hmi_launcher.py` in Unihiker device `/root`

Copy the entire *gauge_hmi* folder (the one you've already configured) in Unihiker device `/home`

Turn on the Unihiker and check that *autoboot* is active: *home* - *service toggle* - *autoboot*

Return to main menu and click *run programs*

Go in *root* and click *hmi_launcher.py*

Let the gauge_hmi start

Now close the program by keeping pressed home for about 2 seconds.

Now you can restart the program

This procedure will allow gauge_hmi program autostart at every Unihiker start: when Unihiker is powered, the Unihiker logo appears with a 5secs countdown in the upper right corner, when counter reaches zero, if autoboot option is active, the last executed program will start.
