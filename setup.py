try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name = "pip-utils",
    version = "0.0.1",
    url = 'https://github.com/mattpaletta/pip-utils',
    packages = find_packages(),
    include_package_data = True,
    install_requires = ["threadlru", "beautifulsoup4"],
    setup_requires = [],
    author = "Matthew Paletta",
    author_email = "mattpaletta@gmail.com",
    description = "Programatic Utils for pip management",
    license = "BSD",
    dependency_links=[
        'git+git://github.com/mattpaletta/pynotstdlib.git@master#egg=pynotstdlib-0'
    ],
)