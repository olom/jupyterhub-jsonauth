from setuptools import setup, find_packages

setup(
    name='jupyterhub-jsonauthenticator',
    version='0.0.1',
    maintainer='Adrián Pardini',
    maintainer_email='github@tangopardo.com.ar',
    packages=find_packages(),
    url='https://github.com/pardo-bsso/jupyterhub-jsonauthenticator.git',
    download_url='https://github.com/pardo-bsso/jupyterhub-jsonauthenticator',
    license='BSD',
    platforms=["Any"],
    description='Simple JSON file based authenticator for JupyerHub',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    zip_safe=True,
    entry_points={
        'jupyterhub.authenticators': [
            'json = jsonauthenticator:JsonAuthenticator',
        ],
    },
    install_requires=[
        'jsonschema'
    ]
)
