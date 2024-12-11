import os
import time
import logging
import requests
import random
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import signal
import sys

'''
Бот, который открывает whatsapp и делает рассылку картинки.
'''

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

good_morning_list = ['https://wishpics.ru/site-images/wishpics_ru_14585.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14563.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14481.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14596.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14738.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14584.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14587.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14705.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14609.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14678.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14726.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14723.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14750.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14598.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14576.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14610.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14613.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14731.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14454.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14565.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14633.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14583.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14632.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14485.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14467.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14763.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14740.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14462.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14702.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14624.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14643.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14457.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14575.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14762.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14607.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14720.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14710.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14717.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14594.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14733.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14735.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14625.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14592.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14464.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14461.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14476.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14639.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14558.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14709.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14600.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14694.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14581.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14616.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14628.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14631.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14716.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14560.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14630.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14759.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14589.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14460.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14591.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14728.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14588.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14659.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14465.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14682.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14683.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14675.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14774.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14673.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14708.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14640.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14627.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14745.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14574.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14724.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14746.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14447.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14442.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14611.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14736.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14571.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14755.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14572.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14614.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14599.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14775.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14568.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14621.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14562.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14693.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14714.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14721.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14771.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14444.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14604.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14704.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14634.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14483.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14458.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14757.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14466.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14772.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14459.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14907.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14698.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14612.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14582.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14734.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14770.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14688.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14748.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14619.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14570.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14636.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14747.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14679.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14766.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14727.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14692.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14685.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14707.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14617.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14662.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14471.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14559.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14468.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14751.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14686.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14469.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14665.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14606.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14477.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14601.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14666.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14718.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14450.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14732.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14578.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14761.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14773.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14638.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14663.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14615.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14687.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14647.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14753.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14854.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14480.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14451.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14744.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14635.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14623.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14567.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14769.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14580.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14577.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14725.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14646.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14868.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14741.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_22103.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14696.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14660.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14590.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14817.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16767.jpeg',
                     'https://wishpics.ru/site-images/wishpics_ru_14573.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14473.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14752.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14711.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14448.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14475.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14765.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14579.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14479.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14791.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14602.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14620.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14593.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14561.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14676.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14691.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16788.jpeg',
                     'https://wishpics.ru/site-images/wishpics_ru_14446.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14837.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14768.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14719.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14699.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14790.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14856.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14597.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14713.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14667.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14566.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14690.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14668.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14482.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14443.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14715.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14926.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14661.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14670.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14730.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14463.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14760.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14677.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14470.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14680.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_17007.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16782.jpeg',
                     'https://wishpics.ru/site-images/wishpics_ru_14700.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14722.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14808.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14637.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14626.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14778.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14452.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14453.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14695.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14674.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16744.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14445.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14608.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14729.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14664.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14564.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14944.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14689.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14569.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14712.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14642.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14474.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14797.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14841.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14472.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14672.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14449.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16868.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14812.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16768.jpeg',
                     'https://wishpics.ru/site-images/wishpics_ru_14703.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14622.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14767.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14456.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14756.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14701.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14884.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14852.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14737.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14684.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14706.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14800.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14878.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14918.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14478.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14641.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_17005.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14669.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14595.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14455.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14758.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14853.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14916.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14831.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14857.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14484.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14739.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14605.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14742.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14629.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14586.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14603.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16859.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14911.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14743.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14749.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14648.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14754.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14896.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14764.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14697.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16741.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16766.jpeg',
                     'https://wishpics.ru/site-images/wishpics_ru_14681.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14644.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14645.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14927.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_17014.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14917.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_16750.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14890.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14933.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14824.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14850.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14947.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14919.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14928.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14860.jpg',
                     'https://wishpics.ru/site-images/wishpics_ru_14815.jpg']


def handle_exit(signal, frame):
    logging.info("Программа завершена пользователем.")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)


def load_phone_numbers(file_path):
    """
    Читает номера телефонов из текстового файла и возвращает их в виде списка.
    """
    try:
        with open(file_path, 'r') as file:
            phone_numbers = [line.strip() for line in file.readlines()]
            logging.info(f"Загружено {len(phone_numbers)} номеров.")
            return phone_numbers
    except FileNotFoundError:
        logging.error(f"Файл с номерами не найден: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Ошибка при загрузке номеров: {e}")
        return []


def clear_search_box(data_browser, position_search_box):
    """
    Очистка поля поиска перед отправкой следующего сообщения
    """
    try:
        actions = ActionChains(data_browser)
        actions.click(position_search_box).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()
        logging.info("Поле поиска очищено")
    except Exception:
        logging.exception("Ошибка очистки поля поиска")


def preview_image(save_path="processed_image.jpg"):
    """
    Скачивание и сохранение изображения в файл.
    """
    # url изображения
    image_url = random.choice(good_morning_list)
    try:
        # Скачивание изображения
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Проверка на ошибки HTTP

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        logging.info(f"Изображение скачано и сохранено: {save_path}")

        img = Image.open(save_path)
        img.show()

        return os.path.abspath(save_path)

    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка загрузки изображения: {e}")
        return None
    except Exception as e:
        logging.error(f"Ошибка обработки изображения: {e}")
        return None


def convert_image(save_path="processed_image.jpg"):
    """
    Преобразует изображение в формат JPG, если это нужно.
    """
    try:
        # Если изображение уже сохранено в save_path, проверим его формат
        img = Image.open(save_path)

        # Преобразование в формат RGB, если это необходимо
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Перезаписываем файл в том же месте
        img.save(save_path, "JPEG")
        logging.info(f"Изображение пересохранено как JPG: {save_path}")

        return os.path.abspath(save_path)

    except Exception as e:
        logging.error(f"Ошибка обработки изображения: {e}")
        return None


def wait_for_element(driver, by, locator, timeout=30):
    """
    Ожидание появления элемента на странице.
    """
    try:
        return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((by, locator)))
    except Exception:
        logging.exception(f"Ошибка ожидания элемента: {locator}")
        return None


def send_image(data_browser, position_search_box, phone_number, image):
    """
    Отправка изображения по указанному номеру телефона через WhatsApp Web.
    """
    try:
        # Шаг 1: Очистка поля поиска
        clear_search_box(data_browser, position_search_box)

        # Шаг 2: Поиск контакта
        actions = ActionChains(data_browser)
        actions.click(position_search_box).send_keys(phone_number).send_keys(Keys.ENTER).perform()
        logging.info(f"Поиск контакта: {phone_number}")

        # Шаг 3: Ожидание загрузки чата
        wait_for_element(data_browser, By.XPATH, '//*[@id="main"]/footer')

        # Шаг 4: Нажатие кнопки прикрепления
        attach_button = wait_for_element(
            data_browser, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div'
        )
        if attach_button:
            attach_button.click()
            logging.info("Кнопка прикрепления нажата")

        # Шаг 5: Выбор файла
        file_input = wait_for_element(data_browser, By.XPATH, "(//input[@type='file'])[2]")
        if file_input:
            file_input.send_keys(image)
            logging.info(f"Изображение загружено: {image}")

        wait_for_element(data_browser, By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[2]/span/div')

        # Шаг 6: Отправка сообщения
        # actions.send_keys(Keys.ENTER).perform()
        logging.info(f"Изображение отправлено контакту: {phone_number}")

        # Ожидание загрузки изображения
        time.sleep(1)

    except Exception:
        logging.exception(f"Ошибка при отправке изображения контакту {phone_number}")


if __name__ == "__main__":
    try:
        phone_numbers = load_phone_numbers('Phone Numbers.txt')

        if not phone_numbers:
            raise ValueError("Список номеров пуст или не удалось загрузить.")

        temp_image = preview_image()
        if not temp_image:
            raise ValueError("Не удалось загрузить изображение.")

        while input("Отправьте:\n1.Отправить Изображение\n2.Следующее Изображение\n==>> ") != '1':
            temp_image = preview_image()
            if not temp_image:
                raise ValueError("Не удалось загрузить изображение.")

        local_image_path = convert_image(temp_image)
        if not local_image_path:
            raise ValueError("Не удалось преобразовать изображение.")

        options = webdriver.ChromeOptions()
        profile_path = r"C:\Users\ReSmus\AppData\Local\Google\Chrome\User Data"
        profile_name = "Default"
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument(f"--profile-directory={profile_name}")

        with webdriver.Chrome(options=options) as browser:
            browser.get('https://web.whatsapp.com/')
            search_box = wait_for_element(browser, By.XPATH, '//*[@id="side"]/div[1]/div/div[2]')
            if not search_box:
                raise ValueError("Поле поиска не найдено")

            for number in phone_numbers:
                send_image(browser, search_box, number, local_image_path)

            if os.path.exists("processed_image.jpg"):
                os.remove("processed_image.jpg")
                logging.info("Файл удален")

            logging.info("Программа успешно завершила свою работу")
    except FileNotFoundError as e:
        logging.error(f"Файл не найден: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
    except Exception as e:
        logging.exception(f"Непредвиденная ошибка: {e}")
