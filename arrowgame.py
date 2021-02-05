from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
myID = mc.getPlayerEntityId('BLADEHTML')

points = 0
i=0
j=0
k=0




x,y,z= mc.player.getPos()
mc.setBlocks(x,y-1,z,x+3,y-1,z+3,24)
mc.setSign(x+3,y,z+2,63,4,"遊戲規則","使用弓箭 以拋物線","在30秒內擊中目標得分",)
mc.setSign(x+3,y,z+3,63,4,"第一層 分數+1", "第二層 分數+2"," 第三層 分數+3","三層全中 總分數乘2")




mc.postToTitle(myID,'10秒後開始遊戲')
time.sleep(1)
mc.postToTitle(myID,'10')
time.sleep(1)
mc.postToTitle(myID,'9')
time.sleep(1)
mc.postToTitle(myID,'8')
time.sleep(1)
mc.postToTitle(myID,'7')
time.sleep(1)
mc.postToTitle(myID,'6')
time.sleep(1)
mc.postToTitle(myID,'5')
time.sleep(1)
mc.postToTitle(myID,'4')
time.sleep(1)
mc.postToTitle(myID,'3')
time.sleep(1)
mc.postToTitle(myID,'2')
time.sleep(1)
mc.postToTitle(myID,'1')
time.sleep(1)
mc.postToTitle(myID,'遊戲開始!!')






x=x+20
y=y+5
for i in range (1,4):
    mc.setBlocks(x,y,z,x+4,y+1,z+4,24) 
    mc.setBlocks(x+1,y+1,z+1,x+3,y+1,z+3,i+2)
    x+=5
    y+=3


t=30
while t>0:
   
    
    
    hs = mc.events.pollProjectileHits()
    time.sleep(1)
    t-=1
    if len(hs) > 0:
        h = hs[0]
        x,y,z = h.pos
        y-=1
        a=mc.getBlockWithData(x,y,z)
        a=a.id
        if a == 3 :
            points+=1
            i+=1
            mc.postToTitle(myID,'+1')
        elif a==4:
            points+=2
            j+=1
            mc.postToTitle(myID,'+2')
        elif a == 5:
            points+=3
            k+=1
            mc.postToTitle(myID,'+3')
        
        
        
        
mc.postToTitle(myID,'遊戲結束~')            
        
if i>0 and j>0 and k>0:
    points*=2 
    
mc.postToTitle(myID,'玩家1獲得 '+str(points))    
    