from inputs import inputs
from send_alerts import send_alerts


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'



def check_and_alert(alertTarget, batteryChar, temperatureInC):
  lowerlimit, upperlimit = inputs[batteryChar['coolingType']]
  breachType = infer_breach(temperatureInC, lowerlimit, upperlimit)
  send_alerts(alertTarget, breachType)
