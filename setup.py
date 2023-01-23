import setuptools
setuptools.setup(
    name='hello-world',
    version='1.0',
    scripts=['./scripts/hello-runner'],
    author='xvzc',
    description='This runs my script which is great.',
    packages=['lib.hello'],
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.5'
)
