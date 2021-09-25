import unittest
from ChargeCard import ChargeCard

class StandardTest(unittest.TestCase):

    def test01_Initialization(self):
        visa = ChargeCard(10000)
        self.assertEqual(visa.getBalance(), 0)
        self.assertEqual(visa.getLimit(), 10000)

    def test02_InitializationMultiple(self):
        visa = ChargeCard(10000)
        mc = ChargeCard(20000)
        self.assertEqual(visa.getBalance(), 0)
        self.assertEqual(visa.getLimit(), 10000)
        self.assertEqual(mc.getBalance(), 0)
        self.assertEqual(mc.getLimit(), 20000)
        
    def test03_InitializationOptional(self):
        visa = ChargeCard(10000, 500)
        self.assertEqual(visa.getBalance(), 500)
        self.assertEqual(visa.getLimit(), 10000)

    def test04_ChargeBasic(self):
        mc = ChargeCard(1000)
        visa = ChargeCard(1000)
        visa.charge(500)
        self.assertEqual(visa.getBalance(), 500)
        visa.charge(300)
        self.assertEqual(visa.getBalance(), 800)
        self.assertEqual(mc.getBalance(), 0)

    def test05_ChargePreciseLimit(self):
        visa = ChargeCard(3000)
        self.assertTrue(visa.charge(3000))
        self.assertEqual(visa.getBalance(), 3000)

    def test06_ChargeBigReject(self):
        visa = ChargeCard(1000)
        self.assertFalse(visa.charge(1001))
        self.assertEqual(visa.getBalance(), 0)

    def test07_ChargeMultiReject(self):
        visa = ChargeCard(2000)
        self.assertTrue(visa.charge(1001))
        self.assertFalse(visa.charge(1000))
        self.assertEqual(visa.getBalance(), 1001)

    def test08_ChargeReturnValue(self):
        visa = ChargeCard(1000)
        self.assertTrue(visa.charge(500))
        self.assertEqual(visa.getBalance(), 500)
        self.assertTrue(visa.charge(300))
        self.assertEqual(visa.getBalance(), 800)

    def test09_DepositBasic(self):
        visa = ChargeCard(500)
        visa.charge(300)
        visa.deposit(250)
        self.assertEqual(visa.getBalance(), 50)
        visa.deposit(50)
        self.assertEqual(visa.getBalance(), 0)
        visa.deposit(50)
        self.assertEqual(visa.getBalance(), -50)

    def test10_DepositReturnValue(self):
        visa = ChargeCard(500)
        visa.charge(300)
        self.assertIsNone(visa.deposit(250))
        self.assertEqual(visa.getBalance(), 50)

    def test11_DebitCard(self):
        visa = ChargeCard(0, -500)
        self.assertEqual(visa.getLimit(), 0)
        self.assertEqual(visa.getBalance(), -500)
        self.assertFalse(visa.charge(501))
        self.assertEqual(visa.getBalance(), -500)
        self.assertTrue(visa.charge(200))
        self.assertEqual(visa.getBalance(), -300)
        self.assertFalse(visa.charge(400))
        self.assertEqual(visa.getBalance(), -300)
        self.assertTrue(visa.charge(300))
        self.assertEqual(visa.getBalance(), 0)


class ExtraTest(unittest.TestCase):

    def testEXTRA01_InitializationStringLimit(self):
        self.assertRaises(TypeError,ChargeCard,'10000')

    def testEXTRA02_InitializationNegativeLimit(self):
        self.assertRaises(ValueError,ChargeCard,-1)

    def testEXTRA03_InitializationStringBalance(self):
        self.assertRaises(TypeError,ChargeCard,1000,'500')

    def testEXTRA04_ChargeIntegerAmount(self):
        visa = ChargeCard(5000)
        self.assertRaises(TypeError,visa.charge, 'ten')

    def testEXTRA05_ChargeAmountPositive(self):
        visa = ChargeCard(5000)
        self.assertRaises(ValueError,visa.charge, 0)
        self.assertRaises(ValueError,visa.charge, -1)

    def testEXTRA06_DepositIntegerAmount(self):
        visa = ChargeCard(5000)
        self.assertRaises(TypeError,visa.deposit, 'ten')

    def testEXTRA07_DepositAmountPositive(self):
        visa = ChargeCard(5000)
        self.assertRaises(ValueError,visa.deposit, 0)
        self.assertRaises(ValueError,visa.deposit, -1)
        self.assertIsNone(visa.deposit(1))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StandardTest))
#    suite.addTest(unittest.makeSuite(ExtraTest))
    unittest.TextTestRunner(verbosity=2).run(suite)

