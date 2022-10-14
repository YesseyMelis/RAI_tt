import unittest


from main import read_file, validate_dataset


class TestDatasetValidate(unittest.TestCase):
    def test_validate_dataset_csv(self):
        with open("10000 Sales Records.csv", "rb") as f:
            ds = read_file(f)
            issues = validate_dataset(ds)
        self.assertEqual(
            issues,
            ['Total Cost value should be not bigger than 5000000 on row: 62', 'Total Cost value should be not bigger than 5000000 on row: 226', 'Total Cost value should be not bigger than 5000000 on row: 419', 'Total Cost value should be not bigger than 5000000 on row: 549', 'Total Cost value should be not bigger than 5000000 on row: 640', 'Total Cost value should be not bigger than 5000000 on row: 722', 'Total Cost value should be not bigger than 5000000 on row: 943', 'Total Profit value should be not less than 1000 on row: 1038', 'Total Profit value should be not less than 1000 on row: 1195', 'Total Cost value should be not bigger than 5000000 on row: 1539', 'Total Cost value should be not bigger than 5000000 on row: 1721', 'Total Profit value should be not less than 1000 on row: 1784', 'Total Cost value should be not bigger than 5000000 on row: 1924', 'Total Profit value should be not less than 1000 on row: 1938', 'Total Cost value should be not bigger than 5000000 on row: 2072', 'Total Cost value should be not bigger than 5000000 on row: 2324', 'Total Profit value should be not less than 1000 on row: 2448', 'Total Profit value should be not less than 1000 on row: 2523', 'Total Cost value should be not bigger than 5000000 on row: 2684', 'Total Cost value should be not bigger than 5000000 on row: 2816', 'Total Profit value should be not less than 1000 on row: 2819', 'Total Cost value should be not bigger than 5000000 on row: 2820', 'Total Profit value should be not less than 1000 on row: 2831', 'Total Cost value should be not bigger than 5000000 on row: 3077', 'Total Profit value should be not less than 1000 on row: 3195', 'Total Cost value should be not bigger than 5000000 on row: 3329', 'Total Cost value should be not bigger than 5000000 on row: 3416', 'Total Cost value should be not bigger than 5000000 on row: 3506', 'Total Profit value should be not less than 1000 on row: 3687', 'Total Profit value should be not less than 1000 on row: 3723', 'Total Profit value should be not less than 1000 on row: 3880', 'Total Profit value should be not less than 1000 on row: 3947', 'Total Profit value should be not less than 1000 on row: 4011', 'Total Profit value should be not less than 1000 on row: 4031', 'Total Profit value should be not less than 1000 on row: 4039', 'Total Cost value should be not bigger than 5000000 on row: 4044', 'Total Cost value should be not bigger than 5000000 on row: 4112', 'Total Cost value should be not bigger than 5000000 on row: 4129', 'Total Profit value should be not less than 1000 on row: 4141', 'Total Cost value should be not bigger than 5000000 on row: 4214', 'Total Profit value should be not less than 1000 on row: 4217', 'Total Profit value should be not less than 1000 on row: 4363', 'Total Profit value should be not less than 1000 on row: 4382', 'Total Profit value should be not less than 1000 on row: 4749', 'Total Cost value should be not bigger than 5000000 on row: 4853', 'Total Profit value should be not less than 1000 on row: 4870', 'Total Cost value should be not bigger than 5000000 on row: 4892', 'Total Profit value should be not less than 1000 on row: 5340', 'Total Cost value should be not bigger than 5000000 on row: 5362', 'Total Cost value should be not bigger than 5000000 on row: 5470', 'Total Cost value should be not bigger than 5000000 on row: 5471', 'Total Profit value should be not less than 1000 on row: 5502', 'Total Cost value should be not bigger than 5000000 on row: 5563', 'Total Cost value should be not bigger than 5000000 on row: 5571', 'Total Profit value should be not less than 1000 on row: 5846', 'Total Profit value should be not less than 1000 on row: 5861', 'Total Cost value should be not bigger than 5000000 on row: 5952', 'Total Profit value should be not less than 1000 on row: 6358', 'Total Cost value should be not bigger than 5000000 on row: 6367', 'Total Cost value should be not bigger than 5000000 on row: 6410', 'Total Profit value should be not less than 1000 on row: 6513', 'Total Cost value should be not bigger than 5000000 on row: 6525', 'Total Profit value should be not less than 1000 on row: 6810', 'Total Profit value should be not less than 1000 on row: 6909', 'Total Profit value should be not less than 1000 on row: 7027', 'Total Profit value should be not less than 1000 on row: 7162', 'Total Profit value should be not less than 1000 on row: 7224', 'Total Cost value should be not bigger than 5000000 on row: 7326', 'Total Cost value should be not bigger than 5000000 on row: 7455', 'Total Cost value should be not bigger than 5000000 on row: 7548', 'Total Profit value should be not less than 1000 on row: 7768', 'Total Profit value should be not less than 1000 on row: 7957', 'Total Profit value should be not less than 1000 on row: 8099', 'Total Profit value should be not less than 1000 on row: 8106', 'Total Profit value should be not less than 1000 on row: 8115', 'Total Cost value should be not bigger than 5000000 on row: 8119', 'Total Profit value should be not less than 1000 on row: 8370', 'Total Cost value should be not bigger than 5000000 on row: 8433', 'Total Profit value should be not less than 1000 on row: 8443', 'Total Profit value should be not less than 1000 on row: 8563', 'Total Cost value should be not bigger than 5000000 on row: 8603', 'Total Cost value should be not bigger than 5000000 on row: 8674', 'Total Cost value should be not bigger than 5000000 on row: 8785', 'Total Profit value should be not less than 1000 on row: 8950', 'Total Cost value should be not bigger than 5000000 on row: 9068', 'Total Profit value should be not less than 1000 on row: 9267', 'Total Cost value should be not bigger than 5000000 on row: 9330', 'Total Cost value should be not bigger than 5000000 on row: 9518']
        )

    def test_validate_dataset_partial_csv(self):
        with open("10000 Sales Records.csv", "rb") as f:
            ds = read_file(f)
            issues = validate_dataset(ds[:100])
        self.assertEqual(
            issues,
            ['Total Cost value should be not bigger than 5000000 on row: 62']
        )

    def test_validate_xlsx(self):
        with open("10000-Sales-Records.xlsx", "rb") as f:
            ds = read_file(f)
            issues = validate_dataset(ds[:100])
        self.assertEqual(
            issues,
            ['Total Cost value should be not bigger than 5000000 on row: 62']
        )


if __name__ == '__main__':
    unittest.main()
