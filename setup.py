from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Taskboard',    
    packages=['Taskboard'],
    version='0.1',      
    license='MIT',
    description=' Tasks, boards, notes & code snippets for the command-line environment',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mert Köklü',
    author_email='kklumert@gmail.com',
    url='https://github.com/Marceliny/Taskboard',
    download_url='https://github.com/Marceliny/Taskboard/archive/v_01.tar.gz',
    keywords=['task', 'board', 'notes', 'taskbook', 'snippet',
              'command-line'],
    install_requires=[
        "pyperclip",
    ],
    entry_points = {
        'console_scripts': ['taskboard=Taskbook.__main__:main'],
    },
    python_requires='>=3',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
