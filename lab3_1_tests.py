import unittest 
import lab3_1 as target 


class TestLab3(unittest.TestCase):
   def test_sum(self):
      secret = target.sums()
      self.assertEqual(secret, 42)

   def test_name(self):
      correct = ["DYLAN", "dylan", "Dylan", "an"]
      names = target.names("Dylan")
      self.assertEqual(correct, names)


if __name__ == "__main__":
   unittest.main()
