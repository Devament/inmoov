def lookatpeople():
  i01.setHeadVelocity(40, 40, 40)
  for y in range(0, 10):
    x = (random.randint(1, 5))
    if x == 1:
      fullspeed()
      i01.head.neck.moveTo(90)
      sleep(2)
      trackHumans()
      sleep(10)
      stopTracking()
    if x == 2:
      fullspeed()
      i01.head.rothead.moveTo(80)
      sleep(2)
      trackHumans()
      sleep(10)
      stopTracking()
    if x == 3:
      fullspeed()
      headdown()
      sleep(1)
      trackHumans()
      sleep(10)
      stopTracking()
    if x == 4:
      fullspeed()
      lookrightside()
      sleep(2)
      trackHumans()
      sleep(10)
      stopTracking()
    if x == 5:
      fullspeed()
      lookleftside()
      sleep(2)
      trackHumans()
      sleep(10)
      stopTracking()
  sleep(1)
  lookinmiddle()
  sleep(3)
  i01.mouth.speak("nice to meet you all")