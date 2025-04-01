from setuptools import setup

setup(
    name="stock_data_lib",
    version="1.0.0",
    author="Andy Wang",
    author_email="andy-xushuwang@outlook.com",
    description="A Python library for stock data from Alpha Vantage",
    py_modules=["stock_api"],
    install_requires=["requests"],
    python_requires=">=3.6",
)