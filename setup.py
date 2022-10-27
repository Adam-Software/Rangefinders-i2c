from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='rangefinders-i2c',
    version='0.0.1',
    packages=['rangefinders_i2c'],
    url='https://github.com/Adam-Software/Rangefinders-i2c',
    license='MIT',
    author='vertigra',
    description='Change TOF10120 address device by usb. Get data from TOF10120 device by usb',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['smbus2', 'serial'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Other',
        'Programming Language :: Python :: 3'
    ]

)
