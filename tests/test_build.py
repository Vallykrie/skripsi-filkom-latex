import tempfile
import unittest
from pathlib import Path

from scripts.build import clean_build_dir, write_entry


class SafeBuildTests(unittest.TestCase):
    def test_clean_preserves_manual_files_and_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build = root / 'build'
            build.mkdir()
            (build / 'skripsi-preview.aux').write_text('generated')
            (build / 'notes.txt').write_text('student notes')
            (build / 'manual').mkdir()
            clean_build_dir(build, root)
            self.assertFalse((build / 'skripsi-preview.aux').exists())
            self.assertEqual('student notes', (build / 'notes.txt').read_text())
            self.assertTrue((build / 'manual').is_dir())

    def test_write_rejects_symlink_build_before_touching_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            external = root / 'outside'
            external.mkdir()
            (root / 'build').symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                write_entry('preview', root / 'build', root)
            self.assertEqual([], list(external.iterdir()))

    def test_entry_symlink_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build = root / 'build'
            build.mkdir()
            outside = root / 'personal.tex'
            outside.write_text('keep this thesis')
            (build / 'entry-preview.tex').symlink_to(outside)
            with self.assertRaises(ValueError):
                write_entry('preview', build, root)
            self.assertEqual('keep this thesis', outside.read_text())

    def test_unknown_mode_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                write_entry('publish', root / 'build', root)
            self.assertFalse((root / 'build').exists())


if __name__ == '__main__':
    unittest.main()
