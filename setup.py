from distutils.core import setup

setup(
    name='Taskboard',    
    packages=['Taskboard'],
    version='1.0.0',      
    license='MIT',
    description='Tasks, boards, notes & code snippets for the command-line environment',
    long_description="Tasks, boards, notes & code snippets for the command-line environment",
    author='Mert Köklü',
    author_email='kklumert@gmail.com',
    url='https://github.com/Marceliny/Taskboard',
    download_url='https://github.com/Marceliny/Taskboard/archive/v1.0.tar.gz',
    keywords=['task', 'board', 'notes', 'snippet',
              'command-line'],
    install_requires=[
        "pyperclip",
    ],
    entry_points = {
        'console_scripts': ['taskboard=Taskboard.__main__:main'],
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
