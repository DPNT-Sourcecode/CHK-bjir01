from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AA') == 100
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AABA') == 160
        assert checkout_solution.checkout('AABA') == 160


