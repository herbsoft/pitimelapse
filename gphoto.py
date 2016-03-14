# Wrapper class for calls to the gphoto2 command as a sub process

import subprocess

class GPhoto(object):

    def __init__(self):
        self._subprocess = subprocess
        self._CMD = 'gphoto2'

    # PUBLIC

    def capture(self, name):
        code, out, err = self.call("--capture-image-and-download --filename " + name)
        
        if code != 0:
            raise Exception(err)

        filename = None

        for line in out.split('\n'):
            if line.startswith('Saving file as '):
                filename = line.split('Saving file as ')[1]
        
        return filename

    # PRIVATE

    def call(self, options):
        cmd = self._CMD + " " + options
        p = self._subprocess.Popen(cmd, shell=True, stdout=self._subprocess.PIPE,
                                   stderr=self._subprocess.PIPE)
        out, err, = p.communicate()
        return p.returncode, out.rstrip(), err.rstrip()

