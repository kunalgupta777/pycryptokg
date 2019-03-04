from distutils.core import setup
setup(
  name = 'pycryptokg',         # How you named your package folder (MyLib)
  packages = ['pycryptokg'],   # Chose the same as "name"
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python library for some cryptographic algorithms',   # Give a short description about your library
  author = 'Kunal Gupta',                   # Type in your name
  author_email = 'upanshug53@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kunalgupta777/pycryptokg',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kunalgupta777/cryptopy/archive/1.0.1.tar.gz',    # I explain this later on
  keywords = ['python', 'cryptography', 'RSA', 'DES', 'Ciphers'],   # Keywords that define your package best
  install_requires=[  'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose eithive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.er "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
  ],
)
