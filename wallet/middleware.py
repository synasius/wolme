__author__ = 'Federico Frenguelli <synasius@gmail.com>'


class Ciccio(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        raise Exception("cane")