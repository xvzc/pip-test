from setuptools import setup
setup(
    entry_points = {
        'console_scripts': ['hello=hello-world.command_line:cli'],
    },
    name='hello-world',
)
