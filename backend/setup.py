from setuptools import setup, find_packages

setup(
    name='product_review_analyzer',
    version='1.0.0',
    description='Product Review Analyzer with AI',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = app:main',
        ],
    },
)
