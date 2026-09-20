import os
import sys
import platform

platform_ = platform.platform()
processor_ = platform.processor()
arch = platform.architecture()
id = os.getpid()

def call(input):
    if input == "system":
        print(platform_)
        print(processor_)
        print(arch)
        print(id)
    if input == "platform":
            print(platform_)
    if input == "processor":
            print(processor_)
    if input == "architecture":
            print(arch)


def start():
    run()

def run():
    call("system")
    end()

def end():
      pass

start()