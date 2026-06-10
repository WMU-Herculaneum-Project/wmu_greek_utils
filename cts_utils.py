# import mycapytain
from lxml.etree import XPathEvalError, XMLSyntaxError
from MyCapytain.errors import MissingRefsDecl
from MyCapytain.resources.texts.local.capitains.cts import CapitainsCtsText
from pathlib import Path
import os


def cts_text(urn_prefix: str, path: str) -> CapitainsCtsText:
    """
    A utility function to create a CapitainsCtsText object from a file.
    The file should be in the CTS XML format.
    The URN is constructed from the prefix and the path.
    the language metadata is constructed from file file stem.
    The path must be absolute, and have an XML extension.
    """

    try:
        return CapitainsCtsText(
            urn=urn,
            text=text,
            metadata={"lang": "grc"},
            is_valid=True,
        )
    except (XPathEvalError, XMLSyntaxError, MissingRefsDecl):
        return None


def get_files0(directory):
    for group in directory.iterdir():
        if group.is_dir():
            for work in group.iterdir():
                if work.is_dir():
                    for file in work.iterdir():
                        if file.suffix == ".xml" and (
                            "grc" in file.stem or "lat" in file.stem
                        ):
                            yield group.name, work.name, file.stem, file


def get_files1(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml") and ("grc" in file or "lat" in file):
                group_name = os.path.basename(os.path.dirname(os.path.dirname(root)))
                work_name = os.path.basename(os.path.dirname(root))
                file_stem = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                yield group_name, work_name, file_stem, file_path


for group, work, name, file in get_files0(
    Path("/Users/willf/projects/canonical-greekLit/data")
):
    print(group, work, name, file)
