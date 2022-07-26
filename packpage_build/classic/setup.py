from setuptools import setup


setup(
    name='meu_pacote',
    version='0.1.0',
    description='meu projeto 0',
    long_description='abacate',
    author='name',
    author_email='ab@cate.com',
    packages=['src'],
    python_version='>=3.9,<4.0',
    entry_points={
        'console_scripts': [
            'meu-cli = src.app:cli',
        ]
    },
    install_requires=['httpx']
)