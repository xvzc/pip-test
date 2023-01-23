from setuptools import setup
setup(
    entry_points = {
        'console_scripts': ['hello=hello.command_line:cli'],
    },
    name='hello-world',
)
