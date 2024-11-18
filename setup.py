from setuptools import setup, find_packages

setup(
    name='python-himpunan',  # Nama package
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],  # Tidak menggunakan package tambahan
    author='Andreyhs',
    author_email='ahartawan01@gmail.com',
    description='Library Himpunan sederhana menggunakan Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KingPublic/python-himpunan-klp9/tree/main',  # URL repositori GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
