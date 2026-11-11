import json
import unittest
from pathlib import Path
from app.locale import read_page
class DomainTests(unittest.TestCase):
    def test_locale(self): self.assertEqual(read_page("fixtures/zh.json")["locale"],"zh")
    def test_optional_identity(self): self.assertNotIn("place_id",read_page("fixtures/ko.json"))
    def test_required(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as d:
            p=Path(d)/"p.json";p.write_text('{"url":"x"}')
            with self.assertRaises(ValueError): read_page(p)

class FixtureTests(unittest.TestCase):
    def test_fixture_directory(self): self.assertTrue(Path("fixtures").is_dir())
