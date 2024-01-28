import unittest
from src.process_monitor import ProcessMonitor

class TestProcessMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = ProcessMonitor()

    def test_get_top_processes(self):
        processes = self.monitor.get_top_processes()
        self.assertEqual(len(processes), 10)
        for process in processes:
            self.assertIn('pid', process)
            self.assertIn('name', process)
            self.assertIn('cpu_usage', process)

if __name__ == '__main__':
    unittest.main()