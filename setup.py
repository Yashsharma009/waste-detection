from setuptools import setup

setup(
    name='image-recognition-app',
    version='1.0',
    install_requires=[
        'streamlit==0.88.0',
        'firebase==3.0.1'  # Replace with the appropriate version
    ],
    entry_points={
        'console_scripts': [
            'image-recognition-app = app:main'
        ]
    },
)
