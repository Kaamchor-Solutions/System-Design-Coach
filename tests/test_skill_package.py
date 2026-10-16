"""Portable structural checks for the System Design Coach skill package."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "system-design-coach"
SKILL_FILE = SKILL_DIR / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    def test_frontmatter_has_name_description_and_no_placeholder(self):
        text = SKILL_FILE.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        header = text[4:].split("\n---\n", maxsplit=1)[0]
        self.assertRegex(header, r"(?m)^name: system-design-coach$")
        self.assertRegex(header, r"(?m)^description: >-$")
        self.assertIn("planning a new application", header)
        self.assertNotIn("TODO", text)

    def test_skill_is_compact_and_resources_exist(self):
        text = SKILL_FILE.read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 500)
        self.assertTrue((SKILL_DIR / "references" / "design-workflow.md").is_file())
        self.assertTrue((SKILL_DIR / "references" / "architecture-patterns.md").is_file())
        self.assertTrue((SKILL_DIR / "references" / "quality-gates.md").is_file())
        self.assertTrue((SKILL_DIR / "templates" / "architecture-pack" / "README.md").is_file())
        self.assertTrue((SKILL_DIR / "templates" / "architecture-pack" / "quick-start.md").is_file())
        self.assertTrue((SKILL_DIR / "templates" / "architecture-pack" / "quick-start-example.md").is_file())

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for markdown in ROOT.rglob("*.md"):
            if ".git" in markdown.parts:
                continue
            for raw_target in link_pattern.findall(markdown.read_text(encoding="utf-8")):
                target = raw_target.strip().split("#", maxsplit=1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (markdown.parent / target).resolve()
                with self.subTest(file=markdown.relative_to(ROOT), target=raw_target):
                    self.assertTrue(resolved.exists(), f"Broken relative link: {raw_target}")

    def test_skill_contains_explicit_right_sizing_and_authority_rules(self):
        text = SKILL_FILE.read_text(encoding="utf-8").lower()
        self.assertIn("do not recommend kafka", text)
        self.assertIn("not permission to edit product code", text)
        self.assertIn("assumptions", text)
        self.assertIn("data-flow", text)
        self.assertIn("plain-language", text)

    def test_architecture_pack_covers_requested_artifacts(self):
        pack = SKILL_DIR / "templates" / "architecture-pack"
        expected = {
            "01-prd.md", "02-hld.md", "03-dfd.md", "04-lld.md",
            "05-adrs.md", "06-operations-risk-validation.md",
        }
        self.assertTrue(expected.issubset({path.name for path in pack.iterdir()}))

    def test_material_evidence_conflicts_must_be_reconciled_or_preserved(self):
        workflow = (SKILL_DIR / "references" / "design-workflow.md").read_text(
            encoding="utf-8"
        ).lower()
        gates = (SKILL_DIR / "references" / "quality-gates.md").read_text(
            encoding="utf-8"
        ).lower()

        self.assertIn("reconcile conflicting evidence", workflow)
        self.assertIn("do not silently choose one as authoritative", workflow)
        self.assertIn("record both claims with precise source locations", workflow)
        self.assertIn("revision/date inspected", workflow)
        self.assertIn("version or scope differences", workflow)
        self.assertIn("what each source can and cannot establish", workflow)
        self.assertIn("safe, focused check", workflow)
        self.assertIn("business correctness", workflow)
        self.assertIn("explicit risk or open question", workflow)
        self.assertIn("how it could change the design", workflow)
        self.assertIn("smallest next validation and owner/status", workflow)
        self.assertIn("material conflicts", gates)
        self.assertIn("design impact", gates)
        self.assertIn("validation path", gates)

    def test_first_time_builder_has_a_compact_path_and_escalation_rules(self):
        skill = SKILL_FILE.read_text(encoding="utf-8").lower()
        pack = SKILL_DIR / "templates" / "architecture-pack"
        guide = (pack / "README.md").read_text(encoding="utf-8").lower()
        template = (pack / "quick-start.md").read_text(encoding="utf-8").lower()
        example = (pack / "quick-start-example.md").read_text(encoding="utf-8").lower()

        self.assertIn("first-time builder path", skill)
        self.assertIn("at most three questions", skill)
        self.assertIn("brief risk screen", skill)
        self.assertIn("early idea is not automatically low-risk", skill)
        self.assertIn("one-page quick-start note", skill)
        self.assertIn("expand to the full pack when", skill)
        self.assertIn("quick-start.md", guide)
        for requirement in (
            "aim for one page",
            "observed facts",
            "inferences:",
            "assumptions / unknowns",
            "smallest useful solution",
            "where does information go",
            "security/privacy",
            "treat titles, urls, names, and metadata as potentially sensitive",
            "do not infer privacy from local storage",
            "one acceptance check",
            "when to expand this note",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, template)
        self.assertIn("fictional worked example", template)
        self.assertIn("illustrative only", example)
        self.assertIn("minimum viable product", example)
        self.assertIn("not a backup", example)
        self.assertIn("titles and urls may reveal sensitive interests", example)
        self.assertIn("page code can read browser-local entries", example)


if __name__ == "__main__":
    unittest.main()
