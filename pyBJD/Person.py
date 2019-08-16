class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return "%s %s" % (self.first, self.last)

    def __str__(self):
        return "Person: " + self.full_name()

    def __getattr__(self, item):
        # This special method is called when normal attribute lookup fails
        if item is 'hyphenated_name':
            return lambda x: "%s-%s" % (x.first, x.last)
        else:
            raise AttributeError(item)
