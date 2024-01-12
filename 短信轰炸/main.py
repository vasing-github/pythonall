
import website.xisai
import website.juren
import time

timesleep = 10
phone = ['15908347888','17336914441','13751555951','17818557653','13349002931','18382744516','18615708288','17790440080']
for p in phone:
    website.xisai.xisai(p)
    time.sleep(timesleep)
    website.juren.juren(p)
    time.sleep(timesleep)

