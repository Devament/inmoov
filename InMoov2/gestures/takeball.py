def takeball():
  rest()
  inMoov.startedGesture()
  inMoov.setHandVelocity("right", 22.0, 13.0, 22.0, 31.0, 43.0, 31.0)
  inMoov.setArmVelocity("right", 43.0, 43.0, 43.0, 43.0)
  inMoov.setHeadVelocity(50.0, 50.0)
  inMoov.setTorsoVelocity(31.0, 13.0, -1)
  inMoov.moveHead(30,70)
  inMoov.moveArm("left",5,84,16,15)
  inMoov.moveArm("right",6,73,66,16)
  inMoov.moveHand("left",50,50,40,20,20,90)
  inMoov.moveHand("right",180,140,140,3,0,11)
  inMoov.moveTorso(95,95,90)
  sleep(1)
  inMoov.finishedGesture()