import unittest
import pandas as pd

class TestDataLoading(unittest.TestCase):
    def test_load_data(self):
        file_path = 'src/1600g_filtered_labels.csv'
        data = pd.read_csv(file_path, header=None, delimiter=',', engine='python')
        self.assertFalse(data.empty, "The loaded DataFrame is empty.")

if __name__ == '__main__':
    unittest.main()