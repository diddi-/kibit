from setuptools import find_packages, setup

setup(
    name="kibit",
    version="0.1.0",
    description="Description",
    url="",
    python_requires=">=3.8",
    install_requires=[
        "click",
        "pyyaml",
        "icmplib>=3",
        "colorama",
        "paramiko",
        "importlib_metadata>=4.8"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["kibit=kibit.cli:main"],
        "kibit.modules": [
            "sleep=kibit.modules.sleep.sleep:Sleep",
            "ping=kibit.modules.ping.ping:Ping"
            "ssh=kibit.modules.ssh.ssh:Ssh"
        ]
    }
)
