# Distribution maintenance

The application implementation is maintained separately. This repository contains
the public documentation, examples where applicable, release metadata and checks.

Run the maintenance script with Python 3.12 or later:

~~~sh
python3 tools/check_distribution.py --downloads
~~~

The script checks local documentation links, the intended public visibility,
release/prerelease status, required asset names and public HTTP download links.
It does not execute an application or replace platform acceptance testing.
Updating a release requires keeping README.md, distribution.json, release notes
and checksum files consistent. Preserve application and dependency licenses.

The tools/ directory contains distribution-maintenance code and is excluded from
the application's language statistics.
