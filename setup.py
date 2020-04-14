import setuptools


setuptools.setup(
    name="python-sample-app",
    version="0.0.1",
    author="sw_architecture",
    author_email="gunju.ra@kt.com",
    description="python sample package",
    url="http://10.217.66.21/Ragunju/newdeal-python-sample",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "Django<2.0",
        "django-crispy-forms",
        "django-cms>=3.6,<3.7",
        "djangocms-admin-style>=1.2,<1.3",
        "django-treebeard>=4.0,<5.0",
        "djangocms-text-ckeditor>=3.7,<3.8",
        "djangocms-link>=2.3",
        "djangocms-style>=2.1",
        "djangocms-googlemap>=1.2",
        "djangocms-snippet>=2.1,<2.2",
        "djangocms-video>=2.0,<2.1",
        "djangocms-column>=1.9",
        "djangocms-file>=2.2,<3.0",
        "djangocms-picture>=2.0,<2.1",
        "easy_thumbnails",
        "django-filer>=1.3",
        "django-mptt>0.9",
        "django-classy-tags>=0.7",
        "html5lib>=1.0.1",
        "Pillow>=3.0",
        "django-sekizai>=0.9",
        "six",
        "pytz",
    ],
    setup_requires=[
    ],
    scripts=[
        "manage.py",
    ],
)
