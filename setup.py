from setuptools import setup
setup(
    entry_points = {
        'console_scripts': ['hello=mymodule.command_line:cli'],
    },
    name='hello-world',
)
