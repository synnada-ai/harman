import re
import sys

from generate_changelog import run as generate_changelog
from generate_changelog import validate_version


def get_setup_version():
    """Read the version from setup.py."""
    with open("../setup.py") as f:
        setup_content = f.read()
    # Extract version using regex
    version_match = re.search(r'version="([0-9]+\.[0-9]+\.[0-9]+)"', setup_content)
    if not version_match:
        raise ValueError("Version not found in setup.py")
    return version_match.group(1)


if __name__ == "__main__":
    args = sys.argv[1:]
    version = args[0]
    token = args[1]

    # Validate version format
    validate_version(version)

    # Check if the provided version matches setup.py
    setup_version = get_setup_version()
    if version != setup_version:
        raise ValueError(
            f"Provided version '{version}' does not match setup.py version "
            f"'{setup_version}'"
        )

    generate_changelog(version, token)
