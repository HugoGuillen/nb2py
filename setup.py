from setuptools import setup
import subprocess
import io

subprocess.check_output("pandoc --from=markdown --to=rst --output=README.rst README.md",
                        stderr=subprocess.STDOUT,
                        shell=True)

with io.open('README.rst', encoding="utf-8") as f:
    long_description = f.read()
    
setup(name = 'nb2py',
      packages = ['nb2py'],
      version = '0.1.4',
      description = 'Dumps marked code cells from a Jupyter notebook into a text file.',
      long_description=long_description,
      author = 'Hugo Guillen-Ramirez',
      author_email = 'hugoagr@gmail.com',
      url = 'https://github.com/HugoGuillen/nb2py',
      download_url = 'https://github.com/HugoGuillen/nb2py/archive/0.1.4.tar.gz',
      license='MIT',
      keywords = ['jupyter'],
      zip_safe=False)