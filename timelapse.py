#!/usr/bin/python

import time

from gphoto import GPhoto

# ==============================================================================

def main():
    print "Timelapse v1 (by Scott)"

    camera = GPhoto()

    try:
        try:
            filename = camera.capture("timelapse001.jpg")
            print filename;
        except Exception, e:
            print "Error on capture1: " + str(e)

        time.sleep(30)

        try:
            filename = camera.capture("timelapse002.jpg")
            print filename;
        except Exception, e:
            print "Error on capture2: " + str(e)

    except Exception, e:
            print "Error: " + str(e)

# ==============================================================================

if __name__ == "__main__":
    main()
