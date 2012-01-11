from setuptools import setup, find_packages


VERSION = __import__("app_name_translation_in_admin").__version__

setup(
    name="django-app-name-translation-in-admin",
    description="Application names i18n in the admin app",
    version=VERSION,
    author="Bojan Mihelac",
    author_email="bmihelac@mihelac.org",
    url="https://github.com/bmihelac/django-app-name-translation-in-admin",
    license = 'BSD',
    install_requires = [
    ],
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   "Topic :: Internet :: WWW/HTTP"
                   ],
    packages=find_packages(exclude=["example", "example.*"]),
)

