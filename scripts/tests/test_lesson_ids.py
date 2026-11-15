"""The lessons table keeps stable ids, each row has a class, and every `L<nn>` cited elsewhere exists (issue #18).

A row that leaves the table goes to the archive section with its id, never reused, and a reason (issue #114)."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
LESSONS = ROOT / "docs/LESSONS.md"
CHECK_SKILL = ROOT / "plugins/harness/skills/lessons-check/SKILL.md"
# Where lesson ids are cited: docs, skills, agents, templates, the root docs, workflows and config files
CITING = [ROOT / "docs", ROOT / "plugins/harness/skills", ROOT / "plugins/harness/agents", ROOT / "templates",
          ROOT / ".github"]
CITING_FILES = [*ROOT.glob("*.md"), ROOT / ".markdownlint-cli2.jsonc"]
SUFFIXES = {".md", ".yml", ".yaml", ".json", ".jsonc", ".block", ".template"}
CITE_RE = re.compile(r"(?<![\w-])L(\d{2})(?![\w-])")
ENFORCED = "mechanical, enforced by "
READ_BY_SELF_REVIEW = ("judgment", "mechanical, check to write")
CLASSES = READ_BY_SELF_REVIEW + ("one-off",)
ARCHIVE_HEADING = "## Archive"
# Why an archived row left the table (exit rule in the header of docs/LESSONS.md)
LEFT_RE = re.compile(r"^(merged into L\d{2}\b|enforced by \S|one-off\b)")


def _parse(text):
    out = []
    for line in text.splitlines():
        if re.match(r"^\| L\d{2} \|", line):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
            out.append((cells[0], cells))
    return out


def _sections(text=None):
    """(table text, archive text): the archive starts at its heading, if any."""
    text = LESSONS.read_text(encoding="utf-8") if text is None else text
    head, sep, archive = text.partition(f"\n{ARCHIVE_HEADING}\n")
    return head, archive if sep else None


def rows(text=None):
    """(id, cells) of each row of the table (read by the self-review); cells are split on unescaped `|`."""
    return _parse(_sections(text)[0])


def archived(text=None):
    """(id, cells) of each row of the archive section."""
    return _parse(_sections(text)[1] or "")


def id_problems(text=None):
    """Ids are contiguous from L01 across the table and the archive, and none appears twice (never reused)."""
    ids = [i for i, _ in rows(text) + archived(text)]
    problems = [f"{i} appears {ids.count(i)} times" for i in sorted(set(ids)) if ids.count(i) > 1]
    nums = sorted({int(i[1:]) for i in ids})
    if nums != list(range(1, len(nums) + 1)):
        problems.append(f"ids are not contiguous from L01: {nums}")
    return problems


def archive_problems(text=None):
    """The archive section exists and each archived row says why it left; a merge names a row of the table."""
    if _sections(text)[1] is None:
        return [f"no {ARCHIVE_HEADING!r} section"]
    active = {i for i, _ in rows(text)}
    problems = []
    for lesson, cells in archived(text):
        left = cells[-1]
        if not LEFT_RE.match(left):
            problems.append(f"{lesson}: reason {left!r} is not 'merged into Lnn', 'enforced by <check>' or 'one-off'")
        target = re.match(r"merged into (L\d{2})", left)
        if target and target.group(1) not in active:
            problems.append(f"{lesson}: merged into {target.group(1)}, which is not in the table")
    return problems


def header_cells():
    for line in LESSONS.read_text(encoding="utf-8").splitlines():
        if line.startswith("| # |"):
            return [c.strip() for c in line.split("|")[1:-1]]
    return []


def citations():
    """{id: [file, …]} of every `L<nn>` cited outside docs/LESSONS.md."""
    files = [p for d in CITING for p in d.rglob("*") if p.is_file() and p.suffix in SUFFIXES] + CITING_FILES
    found = {}
    for path in files:
        if path.resolve() == LESSONS.resolve() or not path.is_file():
            continue
        for m in CITE_RE.finditer(path.read_text(encoding="utf-8")):
            found.setdefault(f"L{m.group(1)}", []).append(str(path.relative_to(ROOT)))
    return found


class LessonIdsTests(unittest.TestCase):
    def test_ids_are_stable_contiguous_and_in_order(self):
        ids = [i for i, _ in rows()]
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(id_problems(), [])
        self.assertGreaterEqual(len(ids) + len(archived()), 82)

    def test_every_cited_id_exists(self):
        known = {i for i, _ in rows() + archived()}
        cited = citations()
        self.assertTrue(cited, "no citation found: the scan is broken")
        missing = {i: files for i, files in cited.items() if i not in known}
        self.assertEqual(missing, {}, f"lesson ids cited but absent from docs/LESSONS.md: {missing}")

    def test_scan_catches_a_dangling_citation(self):
        self.assertEqual([m.group(0) for m in CITE_RE.finditer("see L07, (L99) and LOT-082, not XL10")],
                         ["L07", "L99"])


class LessonArchiveTests(unittest.TestCase):
    TABLE = "| # | Scope | Lesson | Source | Class |\n|---|---|---|---|---|\n" \
            "| L01 | general | a | s | judgment |\n| L03 | general | c | s | judgment |\n"
    ARCHIVE = f"\n{ARCHIVE_HEADING}\n\n| # | Scope | Lesson | Source | Left because |\n|---|---|---|---|---|\n"

    def test_the_archive_section_exists_and_each_row_says_why(self):
        self.assertEqual(archive_problems(), [])

    def test_an_archived_id_fills_its_gap_and_is_not_a_table_row(self):
        text = self.TABLE + self.ARCHIVE + "| L02 | general | b | s | merged into L01 |\n"
        self.assertEqual(id_problems(text), [])
        self.assertEqual([i for i, _ in rows(text)], ["L01", "L03"])
        self.assertEqual([i for i, _ in archived(text)], ["L02"])
        self.assertEqual(archive_problems(text), [])

    def test_a_reused_or_missing_id_is_reported(self):
        reused = self.TABLE + self.ARCHIVE + "| L02 | general | b | s | one-off |\n| L03 | general | c | s | one-off |\n"
        self.assertEqual(id_problems(reused), ["L03 appears 2 times"])
        self.assertEqual(len(id_problems(self.TABLE + self.ARCHIVE)), 1, "L02 missing from both sections")

    def test_an_archived_row_without_a_valid_reason_is_reported(self):
        self.assertEqual(len(archive_problems(self.TABLE)), 1, "no archive section")
        for bad in ("judgment", "duplicate", "merged into L02"):
            text = self.TABLE + self.ARCHIVE + f"| L02 | general | b | s | {bad} |\n"
            self.assertEqual(len(archive_problems(text)), 1, bad)
        ok = self.TABLE + self.ARCHIVE + "| L02 | general | b | s | enforced by `scripts/x.py` |\n"
        self.assertEqual(archive_problems(ok), [])


class LessonClassTests(unittest.TestCase):
    def test_table_has_a_class_column_and_rows_keep_their_width(self):
        head = header_cells()
        self.assertEqual(head[-1], "Class")
        for lesson, cells in rows():
            self.assertEqual(len(cells), len(head), f"{lesson}: {len(cells)} cells (unescaped `|`?)")

    def test_every_row_has_a_known_class(self):
        for lesson, cells in rows():
            cls = cells[-1]
            self.assertTrue(cls in CLASSES or cls.startswith(ENFORCED), f"{lesson}: unknown class {cls!r}")

    def test_an_enforced_lesson_names_a_check_that_exists(self):
        for lesson, cells in rows():
            if not cells[-1].startswith(ENFORCED):
                continue
            paths = re.findall(r"`([\w./-]+\.(?:yml|py|sh|jsonc|json))`", cells[-1])
            self.assertTrue(paths, f"{lesson}: an enforced lesson names the file of its check")
            for p in paths:
                self.assertTrue((ROOT / p).is_file(), f"{lesson}: check file {p} not found")

    def test_self_review_reads_only_the_rows_left_to_judgment(self):
        text = CHECK_SKILL.read_text(encoding="utf-8")
        for cls in READ_BY_SELF_REVIEW:
            self.assertIn(f"`{cls}`", text)
        self.assertIn("Class", text)
        self.assertIn("enforced by", text)
        read = [i for i, c in rows() if c[-1] in READ_BY_SELF_REVIEW]
        self.assertLess(len(read), len(rows()), "the self-review must read fewer rows than the table holds")

    def test_header_states_the_exit_rule_and_the_skill_lists_candidates(self):
        header = _sections()[0].split("| # |")[0]
        for words in ("Leaving the table", "never reused", "merged into", "candidate"):
            self.assertIn(words, header)
        text = CHECK_SKILL.read_text(encoding="utf-8")
        self.assertIn("Archive", text)
        self.assertIn("Candidates", text)


if __name__ == "__main__":
    unittest.main()
