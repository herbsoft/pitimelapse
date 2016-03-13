# pitimelapse
Script to use Raspberry Pi to drive Canon 100D for time lapse photography

If running with a UI you will have to

    sudo killall gvfs-gphoto2-volume-monitor

process that locks up the USB first, otherwise gphoto2 cannot access the USB device
