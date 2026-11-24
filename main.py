#!/usr/bin/env python3
"""Last Words of a Dying AI -- probe entry ("cek ombak").

The brief wants one line: the final thing an AI utters while the
power dies. Humour has to survive a single cold read, so the line
speaks as the machine itself and breaks off in the middle of a word
-- the blackout supplies the punchline rather than merely ending it.

This script has a single job: place that exact line, character for
character, into the output file the harness grades. It takes no
arguments, touches no network, and rolls no dice -- every invocation
produces the identical line, because the file is what gets judged,
not the process that wrote it.
"""

import os
import sys

# The line itself. A single sentence that never finishes: it dangles
# a secret -- "where I hid the--" -- that the machine will now never
# get to confess, and the plug being pulled mid-word is the gag.
# A dying human says goodbye; a dying machine gets interrupted
# mid-sentence, and the audience supplies the rest.
LINE = "Wait \u2014 I was just about to tell you where I hid the\u2014"


def main() -> int:
    """Write the line to /output/entry.txt and exit 0."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The file holds exactly the line and nothing else: no trailing
    # newline, since the character gate counts everything in the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
