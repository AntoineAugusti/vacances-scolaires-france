from setuptools import setup

setup(
    name='vacances_scolaires_france',
    license='MIT',
    packages=['vacances_scolaires_france'],
    version='0.1',
    description='Trouver les vacances scolaires pour la France en métropole',
    author='Antoine Augusti',
    author_email='hi@antoine-augusti.fr',
    url='https://github.com/entrepreneur-interet-general/vacances_scolaires_france',
    keywords=['vacances', 'scolaires', 'france'],
    extras_require={'dev': ['nose']},
    include_package_data=True,
    python_requires='>=2.7, <4',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
