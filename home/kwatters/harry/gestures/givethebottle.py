def givethebottle():
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.75)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.80, 0.80, 0.85, 0.80)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(0,92)
  i01.moveHead(20,107,82,78,65)
  i01.moveArm("left",77,85,45,20)
  i01.moveArm("right",80,62,38,10)
  i01.moveHand("left",80,90,90,90,180,80)
  i01.moveHand("right",145,112,127,105,143,150)
  i01.moveTorso(90,82,90)

