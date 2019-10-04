from setuptools import setup


requires = ["requests==2.20.0"]


setup(
    name='flounder',
    version='0.0.8',
    description='flounder is a library that create Entity of Dialogflow. This library uses RestAPI of dialogflow. It is not an official library.',
    url='https://github.com/flatfisher/flounder',
    author='flatfisher',
    author_email='shimano.entou@gmail.com',
    license='MIT',
    keywords=['dialogflow', 'dialogflow entity'],
    packages=[
        "flounder",
        "flounder.requests",
        "flounder.requests.entity"
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)