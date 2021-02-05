from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
ID = input('Tell me your name: ')
ID2 = mc.getPlayerEntityId(ID)
mc.player.setTilePos(343,74,112)
while True:
    x,y,z = mc.player.getPos()
    standingAt = mc.getBlock(x,y-1,z)
    shotOn = mc.events.pollProjectileHits()
    if standingAt == 152:
        mc.executeCommand('kill '+ID)
        time.sleep(3)
    if standingAt == 133:
        mc.executeCommand('spawnpoint '+ID)
        time.sleep(0.5)
    if standingAt == 22:
        mc.executeCommand('effect '+ID+' jump_boost 3 5')
    if standingAt == 41:
        mc.executeCommand('effect '+ID+' speed 3 6')
    if standingAt == 57:
        mc.postToTitle(ID2,'Thanks for playing!')
        break
    if standingAt == 42:
        mc.executeCommand('effect '+ID+' slowness 3 2')
    if standingAt == 48:
        mc.setBlock(x,y-1,z,0)
    if len(shotOn) > 0:
        shotPos = shotOn[0]
        x1,y1,z1=shotPos.pos
        z1+=1
        shotBlockData = mc.getBlockWithData(x1,y1,z1)
        #print(shotBlockData)
        if shotBlockData.id == 251 and shotBlockData.data == 5:
            mc.executeCommand('tp '+ID+' '+str(x1)+' '+str(y1)+' '+str(z1-1))
            time.sleep(0.2)