from setuptools import setup
import static_feeds

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-static-feeds',
    version=static_feeds.__version__,
    description='Tool for generating django feeds as static files',
    long_description=long_description,
    author='Boris Tavakalov',
    author_email='b@tavakalov.ru',
    license='BSD',
    url='http://github.com/ironlion/django-static-feeds',

    packages=(
        'static_feeds',
        'static_feeds.management',
        'static_feeds.management.commands'),

    include_package_data=True,

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'six>=1.11.0',
        'Django>=1.8',
    ],
)
