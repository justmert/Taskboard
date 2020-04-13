from distutils.core import setup
setup(
    name='TaskIt',    
    packages=['TaskIt'],
    version='0.1',      
    license='MIT',
    description=' Tasks, boards, notes & code snippets for the command-line environment',
    author='Mert Köklü',
    author_email='kklumert@gmail.com',
    url='https://github.com/Marceliny/TaskIt',
    download_url='https://github.com/Marceliny/TaskIt/archive/v_01.tar.gz',
    keywords=['task', 'board', 'notes', 'taskbook', 'snippet',
              'command-line'],
    install_requires=[
        "pyperclip",
    ],
    python_requires='>=3',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'License :: MIT License',
        "Operating System :: MacOS"
        "Operating System :: Unix"
        "Programming Language :: Python :: 3 :: Only"
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
