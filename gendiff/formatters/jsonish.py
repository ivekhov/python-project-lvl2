import json
from typing import Dict, List


def jsonish(tree: List[Dict]) -> str:
    """Formatter of diff tree to json view.

    Args:
        tree (List[Dict]): Difference between two files.

    Returns:
        str: String with result of comparison.
    """
    return json.dumps(tree, indent=4)
