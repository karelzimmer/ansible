def mywc(s):
    return len(s)

class FilterModule(object):
    def filters(self):
        return { 'wc' : mywc }
