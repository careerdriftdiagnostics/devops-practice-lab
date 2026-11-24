import unittest

from deployment_check import deployment_allowed


class DeploymentCheckTests(unittest.TestCase):
    def test_lab_allowed_when_checks_pass(self):
        self.assertTrue(deployment_allowed("lab", True))

    def test_lab_blocked_when_checks_fail(self):
        self.assertFalse(deployment_allowed("lab", False))

    def test_production_blocked(self):
        self.assertFalse(deployment_allowed("production", True))


if __name__ == "__main__":
    unittest.main()
