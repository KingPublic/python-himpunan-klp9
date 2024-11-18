from setuptools import setup, find_packages

setup(
    name='python-himpunan',  # Nama package
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Tidak menggunakan package tambahan
    author='Nama Anda',
    author_email='emailanda@example.com',
    description='Library Himpunan sederhana menggunakan Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/username/python-himpunan',  # URL repositori GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
    