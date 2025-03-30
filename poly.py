"""
Student information for this assignment:

Replace Cesar Monagas Romero with your name.
On my/our honor, Cesar Monagas Romero, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: cam9225
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """
    A linked list implementation for representing polynomials, where each node
    contains a coefficient and exponent representing a term in the polynomial.
    """
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        Insert a term with given coefficient and exponent into the polynomial.
        Terms are maintained in descending order by exponent. If a term with the
        same exponent exists, coefficients are added together.
        """
        if coeff == 0:
            return

        new_node = Node(coeff, exp)

        if self.head is None or exp > self.head.exp:
            new_node.next = self.head
            self.head = new_node
            return

        previous = None
        current = self.head
        while current is not None and current.exp >= exp:
            if current.exp == exp:
                current.coeff += coeff
                if current.coeff == 0:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                return
            previous = current
            current = current.next

        new_node.next = current
        previous.next = new_node

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        Add another polynomial p to this polynomial and return the sum as a new polynomial.
        
        Args:
            p: The polynomial to add to this one
        Returns:
            A new LinkedList representing the sum of the polynomials
        """
        result = LinkedList()
        current = self.head
        while current:
            result.insert_term(current.coeff, current.exp)
            current = current.next

        current = p.head
        while current:
            result.insert_term(current.coeff, current.exp)
            current = current.next

        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        Multiply this polynomial by another polynomial p and return the product.
        
        Args:
            p: The polynomial to multiply with this one
        Returns:
            A new LinkedList representing the product of the polynomials
        """
        result = LinkedList()
        node1 = self.head
        while node1:
            node2 = p.head
            while node2:
                product_coeff = node1.coeff * node2.coeff
                product_exp = node1.exp + node2.exp
                result.insert_term(product_coeff, product_exp)
                node2 = node2.next
            node1 = node1.next
        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        if self.head is None:
            return ""
        term_strings = []
        current = self.head
        while current:
            term_strings.append(f"({current.coeff}, {current.exp})")
            current = current.next
        return " + ".join(term_strings)


def main():
    """
    Read two polynomials from input, compute their sum and product,
    and print the results.
    """
    n_line = input().strip()
    while n_line == "":
        n_line = input().strip()
    n = int(n_line)
    poly_p = LinkedList()
    for _ in range(n):
        line = input().strip()
        if line == "":
            continue
        coeff, exp = map(int, line.split())
        poly_p.insert_term(coeff, exp)

    blank = input().strip()
    while blank == "":
        blank = input().strip()

    m = int(blank)
    poly_q = LinkedList()
    for _ in range(m):
        line = input().strip()
        if line == "":
            continue
        coeff, exp = map(int, line.split())
        poly_q.insert_term(coeff, exp)

    poly_sum = poly_p.add(poly_q)
    poly_product = poly_p.mult(poly_q)

    print(poly_sum)
    print(poly_product)


if __name__ == "__main__":
    main()
