import unittest
import lab1 as assignment

class TestPythonCrashCourse(unittest.TestCase):

    def test_part1_arithmetic(self):
        # Test basic operators
        result = assignment.exercise_arithmetic(10, 3)
        self.assertIsNotNone(result, "Part 1: Function returned None")
        self.assertEqual(result[0], 3, "Part 1: Floor division incorrect") # 10 // 3 = 3
        self.assertEqual(result[1], 1000, "Part 1: Power incorrect") # 10 ** 3 = 1000
        self.assertEqual(result[2], 1, "Part 1: Remainder incorrect") # 10 % 3 = 1
        
        # Test Hypotenuse
        hypo = assignment.calculate_hypotenuse(3, 4)
        self.assertEqual(hypo, 5.0, "Part 1: Hypotenuse calculation incorrect")

    def test_part2_variables(self):
        result = assignment.exercise_variables()
        self.assertIsNotNone(result, "Part 2: Function returned None")
        self.assertEqual(result[0], 10.50, "Part 2: Price is incorrect")
        self.assertEqual(result[1], 10, "Part 2: Integer cast is incorrect")
        self.assertEqual(result[2], "The price is low", "Part 2: String message incorrect")

    def test_part3_sequences(self):
        input_list = [1, 2]
        result = assignment.exercise_sequences("DataScience", input_list)
        
        self.assertEqual(result[0], "Data", "Part 3: String slicing incorrect")
        self.assertIn("Python", result[1], "Part 3: List append incorrect")
        self.assertEqual(result[2], (10, 20), "Part 3: Tuple creation incorrect")
        self.assertIsInstance(result[2], tuple, "Part 3: 'coords' is not a tuple")

    def test_part4_sets_dictionaries(self):
        # Test Sets
        nums = [1, 2, 2, 3, 3, 3]
        set_result = assignment.exercise_sets(nums)
        self.assertIsInstance(set_result, set, "Part 4: Did not return a set")
        self.assertEqual(len(set_result), 4, "Part 4: Duplicates not removed or item not added") # {1,2,3,100}
        self.assertIn(100, set_result, "Part 4: 100 not added to set")

        # Test Dictionaries
        student = {'name': 'John', 'score': 90}
        dict_result = assignment.exercise_dictionaries(student.copy())
        self.assertEqual(dict_result['score'], 95, "Part 4: Score not updated correctly")
        self.assertEqual(dict_result['passed'], True, "Part 4: New key 'passed' not added")

    def test_part5_logic(self):
        self.assertEqual(assignment.check_grade(95), "A", "Part 5: Logic for A")
        self.assertEqual(assignment.check_grade(80), "B", "Part 5: Logic for B")
        self.assertEqual(assignment.check_grade(79), "C", "Part 5: Logic for C")
        self.assertEqual(assignment.check_grade(50), "F", "Part 5: Logic for F")

    def test_part6_loops(self):
        nums = [10, 20, 5, 40, 2]
        # > 15: 20, 40 (Count = 2)
        self.assertEqual(assignment.count_high_values(nums, 15), 2, "Part 6: Count incorrect")
        self.assertEqual(assignment.count_high_values(nums, 50), 0, "Part 6: Should be 0")

    def test_part7_functions(self):
        self.assertIsNotNone(assignment.is_even, "Part 7: Lambda not defined")
        self.assertTrue(assignment.is_even(4), "Part 7: 4 is even")
        self.assertFalse(assignment.is_even(5), "Part 7: 5 is odd")

if __name__ == '__main__':
    unittest.main()