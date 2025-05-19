import unittest
import json
import sys
import os

# Ensure root directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from index import extract_metadata
from validation.utility import validate_metadata

class TestPioSolverParser(unittest.TestCase):

    def test_metadata_structure_valid(self):
        """Ensure metadata is complete and passes validation."""
        metadata = extract_metadata()

        # Should not raise error
        validate_metadata(metadata)

        # Check structure types
        self.assertIsInstance(metadata, dict)
        self.assertIsInstance(metadata['board'], str)
        self.assertIsInstance(metadata['effective_stack'], float)
        self.assertIsInstance(metadata['ev_oop'], float)
        self.assertIsInstance(metadata['ev_ip'], float)
        self.assertIsInstance(metadata['range0'], list)
        self.assertIsInstance(metadata['range1'], list)
        self.assertIsInstance(metadata['solve_id'], str)

    def test_ranges_format(self):
        """Check that each range entry contains a colon (e.g., 'QQ:1.0')."""
        metadata = extract_metadata()

        for r in metadata['range0']:
            self.assertIn(':', r)
        for r in metadata['range1']:
            self.assertIn(':', r)

    def test_json_serializable(self):
        """Ensure output is valid JSON."""
        metadata = extract_metadata()
        try:
            json_str = json.dumps(metadata)
            self.assertIsInstance(json_str, str)
        except Exception as e:
            self.fail(f"Metadata not JSON serializable: {e}")

if __name__ == '__main__':
    unittest.main()
