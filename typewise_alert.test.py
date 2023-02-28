import unittest
import typewise_alert
from send_alerts import send_alerts
from send_alerts_stub import send_alerts_stub


class TypewiseTest(unittest.TestCase):
  def limits(self):
      #PASSIVE
    self.assertTrue(typewise_alert.infer_breach(0, 0, 35) == 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(35, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(-1, 0, 35) , 'TOO_LOW')
    self.assertEqual(typewise_alert.infer_breach(1, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(34, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(36, 0, 35), 'TOO_HIGH')
    #ACTIVE
    self.assertTrue(typewise_alert.infer_breach(0, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(45, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(44, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(46, 0, 45) == 'TOO_HIGH')
    #MED
    self.assertTrue(typewise_alert.infer_breach(0, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(40, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 40) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(39, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(41, 0, 40) == 'TOO_HIGH')
    
    #SEND_ALERTS TEST
    send_alerts = send_alerts_stub
    self.assertTrue(send_alerts('TO_CONTROLLER','NORMAL') == 1)
    self.assertTrue(send_alerts('TO_EMAIL', 'TOO_LOW') == 1)
    self.assertTrue(send_alerts('TO_EMAIL', 'TOO_HIGH') == 1)
    self.assertTrue(send_alerts('TO_EMAIL', 'NORMAL') == 0)

if __name__ == '__main__':
  unittest.main()
