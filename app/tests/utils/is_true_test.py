from unittest import main, TestCase


class TestIfIsResultTrueSuite(TestCase):
    def test_should_be_true(self):
        self.assertEqual('1', '1')


if __name__ == "__main__":
    main()