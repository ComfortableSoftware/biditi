

from setuptools import find_packages
from setuptools import setup
from datetime import datetime as DT


__VERSION__ = DT.now().strftime("%Y.%m.%d.%H.%M")
with open("biditi/__VERSION__.py", "tw") as _FD_OUT_:
  _FD_OUT_.write(f"""\n\n__VERSION__ = \"{__VERSION__}\"\n\n#\n""")


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="biditi",
  url="https://github.com/ComfortableSoftware/biditi",
  version=__VERSION__,
  package_dir={"biditi": "biditi"},
  package_data={
      "biditi": [
          "../doc/*",
      ],
  },
  packages=find_packages(),
  install_requires=[],
  scripts=[],
)


#
