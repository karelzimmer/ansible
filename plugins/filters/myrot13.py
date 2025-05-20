import codecs

def myrot13(s):
    return codecs.encode(s, 'rot_13')

class FilterModule(object):
    def filters(self):
        return { 'rot13' : myrot13 }
