from setuptools import setup

setup (name="systeminfo",
       version="0.1",
       description="Basic system information for COMP30670",
       url="",
       author="Aoife O Sullivan",
       author_email="aoifeosullivan19@gmail.com",
       license="GPL3",
       packages=['systeminfo'],
       entry_points={
           'console_scripts':['Practicals_systeminfo=systeminfo.main:main']
           }
       )
