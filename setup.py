from setuptools import setup, find_packages
 
setup(
    name='lift',
    version='0.0.1',
    author='AutodidactsHaven',
    author_email='author@example.com',
    description='Lift is a CMAKE/makefile replacement for C built with Python (Similar cli to zig build or Rust Cargo)',
    python_requires='>=3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/AutodidactsHaven/lift',
    install_requires="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'lift=lift.lift:main'
        ]
    },
)
