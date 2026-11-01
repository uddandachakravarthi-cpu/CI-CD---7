import unittest
import os
import joblib


class TestMLPipeline(unittest.TestCase):

    def test_model_file_exists(self):
        self.assertTrue(
            os.path.exists("student_result_model.pkl")
        )

    def test_model_can_be_loaded(self):
        model = joblib.load("student_result_model.pkl")
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()
