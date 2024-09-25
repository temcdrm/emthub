# EMTHub&trade;

Software and data schemas for standards-based model building and 
validation to perform electromagnetic transient (EMT) studies of electric 
utility power systems. The focus is on inverter-based resources (IBR), 
e.g., wind, solar, and storage, in electric utility systems. 

Use the Green Code button to download.

- End users may now follow the two-step installation described in the next section.
- Developers may now use `git clone https://github.com/temcdrm/emthub.git` from a local directory.

## Users

The Blazegraph triple-store database is required, but unlike [CIMHub](https://github.com/GRIDAPPSD/CIMHub/tree/feature/SETO), Java, Docker, and OpenDSS are not required.

- Install Blazegraph 2.1.6 from [Blazegraph Releases](https://github.com/blazegraph/database/releases).
- Invoke `pip install emthub --upgrade`.

### Alternative Transients Program (ATP)

Some optional features of the software require a license to use ATP. See [ATP Web Site](https://atp-emtp.org/) for more information, and to apply for an ATP license.

## Developers

Install Blazegraph and clone this repository, then use `pip install -e .` to install the Python emthub package from your git clone.

To deploy the project on PyPi, staring in the directory of your git clone, where `setup.py` is located:

- Make sure that the version number in `setup.cfg` and `src\emthub\version.py` is new.
- Invoke `rd /s /q dist` on Windows (would be `rm -rf dist` on Linux or Mac OS X)
- `python -m build`
- `twine check dist/*` should not show any errors
- `twine upload -r testpypi dist/*` requires project credentials for pecblocks on test.pypi.org (Note: this will reject if version already exists, also note that testpypi is a separate register to pypi)
- `pip install -i https://test.pypi.org/simple/ emthub==0.0.1` for local testing of the deployable package, example version 0.0.1 (Note: consider doing this in a separate Python test environment)
- `twine upload dist/*` for final deployment

Copyright 2024, Meltran, Inc

