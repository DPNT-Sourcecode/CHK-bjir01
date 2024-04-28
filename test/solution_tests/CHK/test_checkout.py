from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AA') == 100

        #3A
        assert checkout_solution.checkout('AAA') == 130
        #5A
        assert checkout_solution.checkout('AAAAA') == 200
        #5A + 3A
        assert checkout_solution.checkout('AAAAAAAA') == 330

        assert checkout_solution.checkout('AABA') == 160
        
        #5A + 3A + A
        assert checkout_solution.checkout('AAAAAAAAA') == 380


        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEBB') == 110
        assert checkout_solution.checkout('EEBBB') == 125

        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('FFFFFF') == 40

        assert checkout_solution.checkout('STX') == 45

        assert checkout_solution.checkout('AxBA') == -1
        assert checkout_solution.checkout(5) == -1




