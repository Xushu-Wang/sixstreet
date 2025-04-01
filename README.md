### Software - Stock Data Library


1. Create setup.py

```
from setuptools import setup

setup(
    name="stock_data_lib",
    version="0.1.0",
    author="Andy Wang",
    author_email="andy-xushuwang@outlook.com",
    description="Python library for stock data from Alpha Vantage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["stock_api"],
    install_requires=["requests>=2.25.0"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

```


2. Build the Package

'''
python setup.py sdist bdist_wheel
'''

3. Publishing to PyPI and Install from PyPI

'''
pip install twine

twine upload --repository testpypi dist/*

twine upload dist/*

pip install stock_data_lib

'''




### Discussion

1. What compromises did you make due to time constraints?

- Due to time constraints, I limited the implementation to basic functionalities (lookup, min, max) and did not implement features such as:

- Caching expiration: The cache never clears or updates unless the program restarts.

- Error handling improvement: Errors are only caught at the request level. More granular error handling could be implemented.

- Asynchronous requests: This implementation is synchronous, which could be slow for large batches of symbols. Switching to asyncio would improve performance.

- Testing: Only minimal testing is provided via the __main__ block. Ideally, I would write unit tests using pytest or unittest.

- Logging: Proper logging mechanisms are not implemented.

2. How would you approach versioning of this library?

- I would follow Semantic Versioning (SemVer):

- Major version: For incompatible API changes.

- Minor version: For backward-compatible new features.

- Patch version: For backward-compatible bug fixes.

- For example, 1.0.0 would be the initial release, with subsequent updates like 1.1.0 for adding new features or 1.0.1 for bug fixes.

3. How would we go about publishing this library?

The library could be published to PyPI (Python Package Index) by following these steps:

- Add a setup.py or pyproject.toml file describing the package metadata.

- Register an account on PyPI.

- Build the distribution using tools like setuptools and twine.

- Upload using the command: twine upload dist/*.

- Version updates would be handled through the same process, with version numbers adjusted accordingly.

4. How would you design this if it was going to be a service rather than a library?

If it was a service:

API Design: Implement a RESTful API using frameworks like FastAPI or Flask.

Endpoints:

/lookup: Accepts symbol and date as parameters.

/min: Accepts symbol and n as parameters.

/max: Accepts symbol and n as parameters.

Caching: Use Redis or Memcached for better efficiency and persistence.

Rate Limiting: Apply rate-limiting to prevent overuse of the Alpha Vantage API.

Deployment: Deploy on a cloud platform such as AWS, GCP, or Azure with auto-scaling enabled.

5. Please include any other comments about your implementation.

The implementation is intentionally kept simple to focus on core functionality. It demonstrates the ability to interact with an external API and process the returned data in a useful manner.

Using classes allows for easy extension of functionality in the future.

6. How much time did you spend on this exercise?

Approximately 1.5 hours including implementation, testing, and write-up.

7. Please include any general feedback you have about the exercise.

This was a well-defined exercise that required careful thought around API usage and handling rate limits.

Adding a requirement to implement automated tests would be a helpful addition.

Overall, the exercise was engaging and provided a good opportunity to showcase software design skills.

