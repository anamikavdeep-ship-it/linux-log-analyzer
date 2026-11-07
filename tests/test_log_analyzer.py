import unittest
from log_analyzer import analyze_logs


class TestLogAnalyzer(unittest.TestCase):

    def test_log_counts(self):
        counts, errors = analyze_logs("logs/server.log")

        self.assertEqual(counts["INFO"], 5)
        self.assertEqual(counts["WARNING"], 2)
        self.assertEqual(counts["ERROR"], 4)

    def test_error_messages(self):
        counts, errors = analyze_logs("logs/server.log")

        self.assertEqual(len(errors), 3)
        self.assertIn("Database connection failed", errors[0])


if __name__ == "__main__":
    unittest.main()