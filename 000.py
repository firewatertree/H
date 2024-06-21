tom_h,tom_w,tom_a = 1.8,133,70
meng_h,meng_w,meng_a=1.83,70,21

def compute_BMI(height, weight):
    bmi=weight/height**2
    return bmi
def heartrisk(bmi,age):
    table=[['medium','high'],['low','medium']]
    young=age<45
    heavy=bmi>=22
    '''
    9,10行是個布爾值用來判斷之後要取用TABLE中哪個資料
    EX 50歲 bmi>=22 第16行的young會得出false產出布爾值0 heavy會得出true產出布爾值1
    會對應到table中第0個列表中第1個元素'high'
    如果數值符合high最後會返還RISK
    '''

    risk=table[young][heavy]
    return risk

tom_bmi=compute_BMI(tom_h,tom_w)
print('tom:bmi=%.2f,risk=%s'%(tom_bmi,heartrisk(tom_bmi,tom_a)))
