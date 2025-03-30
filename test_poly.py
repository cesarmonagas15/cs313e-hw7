"""Polynomial Test Suite"""

import unittest
from poly import LinkedList


def checker(list1, expected):
    """Checks if resulting polynomial (linked list) is equal to the
    correct polynomial (list of tuples) after an operation is performed."""
    try:
        cur1 = list1.head
    except AttributeError:
        cur1 = list1.dummy.next
    index = 0
    # Iterate through the linked list and the list of tuples simultaneously
    while cur1 is not None and index < len(expected):
        # Compare the coefficient and exponent of the current node with the tuple
        coeff, exp = expected[index]
        if cur1.coeff != coeff or cur1.exp != exp:
            return False
        # Move to the next node in the linked list and the next tuple
        cur1 = cur1.next
        index += 1

    # If there are still nodes in the linked list or unmatched tuples, return False
    if cur1 is not None or index < len(expected):
        return False
    return True


class TestInsertTerm(unittest.TestCase):
    """insert_term Test Suite"""

    def test_1(self):
        """Basic insertion with different exponents."""
        poly = LinkedList()
        poly.insert_term(5, 3)  # 5x^3
        poly.insert_term(3, 2)  # 3x^2
        poly.insert_term(1, 1)  # x

        correct_poly = [(5, 3), (3, 2), (1, 1)]
        self.assertTrue(checker(poly, correct_poly))

    def test_2(self):
        """Inserting terms that combine due to matching exponents."""
        poly = LinkedList()
        poly.insert_term(4, 2)  # 4x^2
        poly.insert_term(3, 2)  # +3x^2 should combine to 7x^2

        correct_poly = [(7, 2)]
        self.assertTrue(checker(poly, correct_poly))

    def test_3(self):
        """Inserting a zero coefficient term, which should be ignored."""
        poly = LinkedList()
        poly.insert_term(0, 4)  # 0x^4 should not appear

        correct_poly = []
        self.assertTrue(checker(poly, correct_poly))

    def test_4(self):
        """Inserting terms with descending exponents."""
        poly = LinkedList()
        poly.insert_term(5, 5)  # 5x^5
        poly.insert_term(3, 4)  # 3x^4
        poly.insert_term(1, 2)  # x^2

        correct_poly = [(5, 5), (3, 4), (1, 2)]
        self.assertTrue(checker(poly, correct_poly))

    def test_5(self):
        """Inserting terms with negative coefficients."""
        poly = LinkedList()
        poly.insert_term(-4, 3)  # -4x^3
        poly.insert_term(-5, 1)  # -5x

        correct_poly = [(-4, 3), (-5, 1)]
        self.assertTrue(checker(poly, correct_poly))

    def test_6(self):
        """Inserting terms with a zero exponent."""
        poly = LinkedList()
        poly.insert_term(6, 0)  # constant term 6

        correct_poly = [(6, 0)]
        self.assertTrue(checker(poly, correct_poly))


class TestAdd(unittest.TestCase):
    """add Test Suite"""

    def test_1(self):
        """Basic addition with no overlap in exponents."""
        poly1 = LinkedList()
        poly1.insert_term(3, 2)  # 3x^2
        poly2 = LinkedList()
        poly2.insert_term(4, 1)  # 4x

        result = poly1.add(poly2)
        correct_poly = [(3, 2), (4, 1)]
        self.assertTrue(checker(result, correct_poly))

    def test_2(self):
        """Adding two polynomials with matching exponents."""
        poly1 = LinkedList()
        poly1.insert_term(2, 3)  # 2x^3
        poly2 = LinkedList()
        poly2.insert_term(3, 3)  # 3x^3

        result = poly1.add(poly2)
        correct_poly = [(5, 3)]
        self.assertTrue(checker(result, correct_poly))

    def test_3(self):
        """Adding polynomials where all terms cancel out."""
        poly1 = LinkedList()
        poly1.insert_term(3, 2)  # 3x^2
        poly2 = LinkedList()
        poly2.insert_term(-3, 2)  # -3x^2

        result = poly1.add(poly2)
        correct_poly = []
        self.assertTrue(checker(result, correct_poly))

    def test_4(self):
        """Adding with negative coefficients."""
        poly1 = LinkedList()
        poly1.insert_term(-4, 3)  # -4x^3
        poly2 = LinkedList()
        poly2.insert_term(2, 3)  # 2x^3

        result = poly1.add(poly2)
        correct_poly = [(-2, 3)]
        self.assertTrue(checker(result, correct_poly))

    def test_5(self):
        """Adding two polynomials with terms in descending order."""
        poly1 = LinkedList()
        poly1.insert_term(3, 2)  # 3x^2
        poly2 = LinkedList()
        poly2.insert_term(1, 0)  # 1

        result = poly1.add(poly2)
        correct_poly = [(3, 2), (1, 0)]
        self.assertTrue(checker(result, correct_poly))

    def test_6(self):
        """Adding polynomials where one polynomial is empty."""
        poly1 = LinkedList()
        poly2 = LinkedList()

        result = poly1.add(poly2)
        correct_poly = []
        self.assertTrue(checker(result, correct_poly))


class TestMult(unittest.TestCase):
    """mult Test Suite"""

    def test_1(self):
        """Test multiplying two simple positive polynomials"""
        # Student's input polynomials
        poly1 = LinkedList()
        poly1.insert_term(3, 2)  # 3x^2
        poly1.insert_term(2, 1)  # 2x
        poly1.insert_term(1, 0)  # 1

        poly2 = LinkedList()
        poly2.insert_term(1, 1)  # x
        poly2.insert_term(2, 0)  # 2

        # Perform the student's multiply operation
        result = poly1.mult(poly2)

        correct_poly = [(3, 3), (8, 2), (5, 1), (2, 0)]
        self.assertTrue(checker(result, correct_poly))

    def test_2(self):
        """Test multiplying polynomials with a negative coefficient"""
        poly1 = LinkedList()
        poly1.insert_term(-3, 2)  # -3x^2
        poly1.insert_term(4, 1)  # 4x

        poly2 = LinkedList()
        poly2.insert_term(2, 1)  # 2x
        poly2.insert_term(5, 0)  # 5

        result = poly1.mult(poly2)

        correct_poly = [(-6, 3), (-7, 2), (20, 1)]
        self.assertTrue(checker(result, correct_poly))

    def test_3(self):
        """Test multiplying a polynomial by zero"""
        poly1 = LinkedList()
        poly1.insert_term(4, 3)  # 4x^3
        poly1.insert_term(5, 5)  # 5x^5

        poly2 = LinkedList()  # Zero polynomial

        result = poly1.mult(poly2)

        correct_poly = []
        self.assertTrue(checker(result, correct_poly))

    def test_both_4(self):
        """Test multiplying two zero polynomials"""
        poly1 = LinkedList()
        poly2 = LinkedList()

        result = poly1.mult(poly2)

        correct_poly = []
        self.assertTrue(checker(result, correct_poly))

    def test_5(self):
        """Test multiplying polynomials with large exponents"""
        poly1 = LinkedList()
        poly1.insert_term(1, 1000)  # x^1000

        poly2 = LinkedList()
        poly2.insert_term(1, 500)  # x^500

        result = poly1.mult(poly2)

        correct_poly = [(1, 1500)]
        self.assertTrue(checker(result, correct_poly))

    def test_6(self):
        """Test multiplying polynomials where terms result in similar exponents"""
        poly1 = LinkedList()
        poly1.insert_term(2, 2)  # 2x^2

        poly2 = LinkedList()
        poly2.insert_term(3, 1)  # 3x

        result = poly1.mult(poly2)

        correct_poly = [(6, 3)]
        self.assertTrue(checker(result, correct_poly))


class TestStr(unittest.TestCase):
    """__str__ Test Suite"""

    def test_1(self):
        """Test the string representation"""
        poly = LinkedList()
        poly.insert_term(5, 3)  # 5x^3
        poly.insert_term(7, 2)  # 7x^2
        poly.insert_term(1, 1)  # x
        self.assertEqual(str(poly), "(5, 3) + (7, 2) + (1, 1)")

    def test_2(self):
        """Test string representation with negative coefficients"""
        poly = LinkedList()
        poly.insert_term(-3, 4)  # -3x^4
        poly.insert_term(-2, 2)  # -2x^2
        poly.insert_term(-5, 1)  # -5x
        self.assertEqual(str(poly), "(-3, 4) + (-2, 2) + (-5, 1)")

    def test_3(self):
        """Test string representation with a constant term"""
        poly = LinkedList()
        poly.insert_term(4, 0)  # 4
        self.assertEqual(str(poly), "(4, 0)")

    def test_4(self):
        """Test string representation with a zero polynomial"""
        poly = LinkedList()
        self.assertEqual(str(poly), "")

    def test_5(self):
        """Test string representation with mixed terms and zero coefficients"""
        poly = LinkedList()
        poly.insert_term(0, 3)  # 0x^3
        poly.insert_term(5, 2)  # 5x^2
        poly.insert_term(-5, 1)  # -5x
        poly.insert_term(4, 0)  # 4
        self.assertEqual(str(poly), "(5, 2) + (-5, 1) + (4, 0)")

    def test_6(self):
        """Test string representation after adding two polynomials"""
        poly1 = LinkedList()
        poly1.insert_term(1, 2)  # x^2
        poly1.insert_term(3, 1)  # 3x

        poly2 = LinkedList()
        poly2.insert_term(2, 2)  # 2x^2
        poly2.insert_term(-3, 1)  # -3x

        result = poly1.add(poly2)
        self.assertEqual(str(result), "(3, 2)")

if __name__ == "__main__":
    unittest.main()
