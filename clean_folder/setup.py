from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="0.0.3",
    description="Program to rename and sorting files",
    url="https://github.com/denisbobrov0702/treatment",
    author="Denys Bobrov",
    author_email="denisbobrov0702@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["markdown"],
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:main"]},
)
