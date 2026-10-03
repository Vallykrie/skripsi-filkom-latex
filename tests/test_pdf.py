import unittest

from scripts.check_pdf import (
    FRONT,
    HEADINGS,
    validate_document_structure,
    validate_fonts,
)


class PdfValidationTests(unittest.TestCase):
    def test_body_prose_is_not_mistaken_for_appendix_heading(self):
        pages = [*FRONT, *HEADINGS, 'LAMPIRAN A CONTOH', 'LAMPIRAN B CONTOH']
        pages[10] += ' Nomor bab berubah setelah penyuntingan.'
        self.assertEqual(validate_document_structure('\f'.join(pages)), [])

    def test_toc_mentions_do_not_replace_missing_result_chapter(self):
        pages = ['DAFTAR ISI BAB 4 HASIL', 'BAB 1 PENDAHULUAN',
                 'BAB 2 LANDASAN KEPUSTAKAAN', 'BAB 3 METODOLOGI',
                 'BAB 5 PEMBAHASAN', 'BAB 6 PENUTUP', 'DAFTAR REFERENSI',
                 'LAMPIRAN A CONTOH']
        self.assertTrue(validate_document_structure('\f'.join(pages)))

    def test_wrong_appendix_prefix_is_rejected(self):
        self.assertTrue(validate_document_structure('BAB A LAMPIRAN'))

    def test_appendices_must_follow_references_in_alphabetical_order(self):
        wrong = [*FRONT, 'LAMPIRAN B CONTOH', 'LAMPIRAN A CONTOH', *HEADINGS]
        self.assertTrue(validate_document_structure('\f'.join(wrong)))
        wrong = [*FRONT, *HEADINGS, 'LAMPIRAN B CONTOH', 'LAMPIRAN A CONTOH']
        self.assertTrue(validate_document_structure('\f'.join(wrong)))

    def test_official_rejects_carlito(self):
        fonts = {'Carlito', 'Carlito-Bold', 'Carlito-Italic'}
        self.assertTrue(validate_fonts(fonts, 'official'))
        self.assertFalse(validate_fonts(fonts, 'preview'))


if __name__ == '__main__':
    unittest.main()
