from setuptools import setup, find_packages
#this is a test
setup(name = 'django_ckeditorfiles',
      description = 'CKEditor bundled as a django staticfiles app.',
      version = '0.1',
      url = 'https://github.com/ninapavlich/django-inline-orderable',
      author = 'Nina Pavlich',
      author_email='nina@cgparntersllc.com',
      license = 'BSD',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      include_package_data=True,
      install_requires = ['setuptools', 'Django'],
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
