import setuptools
import okx_async
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-okx-async",
    version=okx_async.__version__,
    author="CircuitDAO",
    author_email="info@circuitdao.com",
    description="Python SDK with async support for the OKX v5 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://okx.com/docs-v5/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "importlib-metadata",
        "httpx[http2]",
        "keyring",
        "requests",
        "Twisted",
        "pyOpenSSL"
    ]
)
