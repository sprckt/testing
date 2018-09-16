#! /usr/bin/env python


def divider(topic):
    print("\n")
    print("#" * 30)
    print(topic.title())
    print("#" * 30)
    print("\n")


def simples():
    return "Simple function from Sourcey"

class SourceClass:

    def __init__(self):
        self.person = 'Eric'

    def explode(self):
        return "KABOOM"