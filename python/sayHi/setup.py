import setuptools
from sayHi import __email__, __version__

setuptools.setup(
    name = "sayHi",
    version = __version__,
    keywords = "say",
    description = "say hi, say good morning\\afternoon\\everning to you.",
    author = "chuan",
    author_email = __email__,
    packages = setuptools.find_packages(),
    license = "MIT",
    entry_points = {
        'console_scripts':[
            'sayhi = sayHi.main:main'
        ],
    },
)
