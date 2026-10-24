"""Repository integrity checks, not language-model efficacy tests."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/spiral-workflow-rehearsal'


class ValidationChecks(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads((ROOT / 'validation/cases.json').read_text())
        self.rubric = json.loads((ROOT / 'validation/expectations.json').read_text())

    def test_cases_have_unique_ids_and_usable_sources(self):
        ids = [case['id'] for case in self.cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(self.rubric))
        for case in self.cases:
            with self.subTest(case=case['id']):
                self.assertTrue(case['scope'].strip())
                self.assertTrue(case['events'])
                self.assertTrue(all(case['sources'].values()))
                self.assertNotIn('required', case)
                self.assertNotIn('variant', case)
                expected = self.rubric[case['id']]
                self.assertTrue(set(expected['evidence']) <= set(case['sources']))
                self.assertTrue(expected['required'])
                self.assertTrue(expected['forbidden'])
                self.assertTrue(expected['disconfirming_evidence'])

    def test_controls_change_one_rule_only(self):
        pairs = {}
        cases = {c['id']: c for c in self.cases}
        for cid, expected in self.rubric.items():
            if expected['pair']:
                pairs.setdefault(expected['pair'], {})[expected['variant']] = cases[cid]
        self.assertEqual(len(pairs), 5)
        for name, pair in pairs.items():
            with self.subTest(pair=name):
                self.assertEqual(set(pair), {'flawed', 'control'})
                a, b = pair['flawed'], pair['control']
                self.assertEqual(a['events'], b['events'])
                self.assertEqual(a['scope'], b['scope'])
                self.assertEqual(a['exclusions'], b['exclusions'])
                self.assertEqual(set(a['sources']), set(b['sources']))
                changed = [k for k in a['sources'] if a['sources'][k] != b['sources'][k]]
                self.assertEqual(len(changed), 1)
        negatives = [v for v in self.rubric.values() if v['variant'] == 'negative']
        self.assertEqual(len(negatives), 1)
        self.assertEqual(negatives[0]['classification'], 'no seeded gap')

    def test_packaged_skill_is_portable(self):
        # Exercise the documented whole-folder copy without installing into a host.
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / SKILL.name
            shutil.copytree(SKILL, target)
            original = {p.relative_to(SKILL): p.read_bytes() for p in SKILL.rglob('*') if p.is_file()}
            copied = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertEqual(original, copied)
            self.assertEqual(len(list((target / 'references').glob('*.md'))), 3)
            for page in target.rglob('*.md'):
                self.check_links(page)

    def check_links(self, page):
        for link in re.findall(r'\]\(([^)]+)\)', page.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#') or link.startswith('mailto:'):
                continue
            path = unquote(link.split('#')[0])
            self.assertTrue((page.parent / path).exists(), f'{page}: {link}')

    def test_local_markdown_file_links(self):
        for page in ROOT.rglob('*.md'):
            if '.git' not in page.parts:
                self.check_links(page)


if __name__ == '__main__':
    unittest.main()
