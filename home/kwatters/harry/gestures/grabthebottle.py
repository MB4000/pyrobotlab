def grabthebottle():
  i01.setHandSpeed("left", 1.0, 0.80, 0.80, 0.80, 1.0, 0.80)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.80)
  i01.setTorsoSpeed(1.0,0.80,1.0)
  i01.moveHead(20,107)
  i01.moveArm("left",77,85,45,20)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",180,138,140,164,180,60)
  i01.moveHand("right",0,0,0,0,0,90)
  i01.moveTorso(90,84,90)

