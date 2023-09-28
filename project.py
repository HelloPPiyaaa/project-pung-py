print("="*7,"โปรแกรมร้านสะดวกซื้อ","="*7)
name = input("กรอกชื่อของท่าน :")
print("สวัสดีคุณ",name,"คุณต้องการทำสิ่งใด?")
market = []  #เก็บรหัสสินค้าที่เลือก
sumprice = 0 #ราคาสินค้า*จำนวนสินค้า
total = 0    #จำนวนเงินรวม

while True:
    print("="*31)
    print("กด1 เพื่อเลือกซื้อสินค้า")
    print("กด2 เพื่อดูโปรโมชั่น")
    print("กด3 เพื่อดูการสั่งซื้อ")
    print("กด0 เพื่อจบการสั่งซื้อ")
    try:
        listwant =[0,1,2,3]
        want = int(input("กรุณากดหมายเลขที่ต้องการทำรายการ :"))
        if want not in listwant :
            print("ไม่มีหมายเลขที่ท่านกด!!")
    except:
        print("กรุณากรอกเฉพาะตัวเลข!")
        continue
   
    if want == 1 :
        print("="*7,"หมวดหมู่สินค้า","="*12)
        print("กด1 => หมวดหมู่เครื่องดื่ม")
        print("กด2 => หมวดหมู่ขนม")
        print("กด3 => หมวดหมู่ของใช้")
        print("กด4 => ย้อนกลับ")
        print("="*31)
        Round = 0
        while Round != 1 :
            try:
                listchoose = [1,2,3,4]
                choose = int(input("ท่านต้องการเลือกหมวดหมู่ใด : "))
                if choose not in listchoose :
                    print("ไม่มีหมายเลขที่ท่านกด!!")
                    continue
            except:
                print("กรุณากรอกเฉพาะตัวเลข!")
            else:
                Round=Round+1
        if choose == 4 :
            pass
        elif choose == 1:    
            file1 = open("choose1.txt","r",encoding="utf8")
            print("-"*9,"หมวดหมู่เครื่องดื่ม","-"*9)
            for i in file1 :
                i = i.split(",")
                print(i[0]+"\t"+i[1]+"\t\t"+i[2])
            file1.close()
            step = input("ท่านต้องการทำรายการที่หมวดหมู่นี้หรือไม่? หากต้องการให้กรอก y หากไม่กรุณากดตัวอื่น :")
            step = step.lower()
            Round = 0
            while  step == "y" and Round != 1:
                try:
                    choose1=[11,12,13,14,15,16,17,18,19,20]
                    select = int(input('กรอกรหัสสินค้าที่ต้องการ :'))
                    if select not in choose1 :
                        print("ไม่มีรหัสที่ท่านเลือก กรุณากรอกใหม่!")
                        continue
                    count =  int(input('จำนวนสินค้า :'))

                except :
                    print("กรุณากรอกเฉพาะตัวเลข!")

                else:
                    market.append(select)
                    Round = Round+1

                    if select == 11 :
                        sumprice = 6*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"น้ำเปล่า 600มิลลิลิตร","จำนวน :",count,"ขวด")   
                    elif select == 12 :
                        sumprice = 15*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"เป๊บซี่ 450มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 13 :
                        sumprice = 14*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"นมรสจืด 250มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 14 :
                        sumprice = 16*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"น้ำผลไม้ 300มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 15 :
                        sumprice = 50*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"เบียร์  475มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 16 :
                        sumprice = 25*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ชาเขียว 500มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 17 :
                        sumprice = 10*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"M150 150มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 18 :
                        sumprice = 14*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"นมเปรี้ยว 250มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 19 :
                        sumprice = 15*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"กาแฟ 180มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 20 :
                        sumprice = 20*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"น้ำส้ม 300มิลลิตร","จำนวน :",count,"ขวด")
                
        elif choose == 2:    
            file2 = open("choose2.txt","r",encoding="utf8")
            print("-"*10,"หมวดหมู่ขนม","-"*11)
            for i in file2 :
                i = i.split(",")
                print(i[0]+"\t"+i[1]+"\t\t"+i[2])
            file2.close()
            step = input("ท่านต้องการทำรายการที่หมวดหมู่นี้หรือไม่? หากต้องการให้กรอก y หากไม่กรุณากดตัวอื่น:")
            step = step.lower()
            Round = 0
            while  step == "y" and Round != 1:
                try:
                    choose2=[21,22,23,24,25,26,27,28,29,30]
                    select = int(input('กรอกรหัสสินค้าที่ต้องการ :'))
                    if select not in choose2 :
                        print("ไม่มีรหัสที่ท่านเลือก กรุณากรอกใหม่!")
                        continue
                    count =  int(input('จำนวนสินค้า :'))
                except :
                    print("กรุณากรอกเฉพาะตัวเลข!")
                else:
                    market.append(select)
                    Round = Round+1

                    if select == 21 :
                        sumprice = 20*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"เลย์รสออรินอล 50กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 22 :
                        sumprice = 33*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ช็อกโกแลต  40กรัม","จำนวน :",count,"ชิ้น")               
                    elif select == 23 :
                        sumprice = 15*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ลูกอมกลิ่นแตงโม 12กรัม","จำนวน :",count,"ชิ้น")              
                    elif select == 24 :
                        sumprice = 34*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"เยลลี่กลิ่นองุ่น 80กรัม","จำนวน :",count,"ชิ้น")            
                    elif select == 25 :
                        sumprice = 39*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"สาหร่ายเกาหลี 30กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 26 :
                        sumprice = 22*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"คุ๊กกี้เนยสด 45กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 27 :
                        sumprice = 14*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"นมอัดเม็ดหวาน 240กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 28 :
                        sumprice = 5*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"โอริโอ้ 36กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 29 :
                        sumprice = 15*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"หมากฝรั่งกลิ่นมิ้นต์ 13กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 30 :
                        sumprice = 20*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"เลย์รสสาหร่าย 50กรัม","จำนวน :",count,"ชิ้น")
                    
                
        elif choose == 3:    
            file3 = open("choose3.txt","r",encoding="utf8")
            print("-"*10,"หมวดหมู่ของใช้","-"*10)
            for i in file3 :
                i = i.split(",")
                print(i[0]+"\t"+i[1]+"\t\t"+i[2])
            file3.close()
            step = input("ท่านต้องการทำรายการที่หมวดหมู่นี้หรือไม่? หากต้องการให้กรอก y หากไม่กรุณากดตัวอื่น:")
            step = step.lower()
            Round = 0
            while  step == "y" and Round != 1:
                try:
                    choose3=[31,32,33,34,35,36,37,38,39,40]
                    select = int(input('กรอกรหัสสินค้าที่ต้องการ :'))
                    if select not in choose3 :
                        print("ไม่มีรหัสที่ท่านเลือก กรุณากรอกใหม่!")
                        continue
                    count = int(input('จำนวนสินค้า :'))
                except :
                    print("กรุณากรอกเฉพาะตัวเลข!")

                else:
                    market.append(select)
                    Round = Round+1

                    if select == 31 :
                        sumprice = 39*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"สำลีแผ่น 100แผ่น","จำนวน :",count,"ชิ้น")
                    elif select == 32 :
                        sumprice = 10*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ผงซักฟอก  90กรัม","จำนวน :",count,"ชิ้น")              
                    elif select == 33 :
                        sumprice = 24*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ผ้าอนามัยกลางคืน 5ชิ้น","จำนวน :",count,"ชิ้น")
                    elif select == 34 :
                        sumprice = 22*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ผ้าอนามัยกลางวัน  5ชิ้น","จำนวน :",count,"ชิ้น")
                    elif select == 35 :
                        sumprice = 95*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"สบู่เหลว 500มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 36 :
                        sumprice = 48*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ยาสีฟัน 150กรัม","จำนวน :",count,"ชิ้น")
                    elif select == 37 :
                        sumprice = 20*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"สบู่ก้อน 73กรัม","จำนวน :",count,"ก้อน")
                    elif select == 38 :
                        sumprice = 139*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"แชมพู 450มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 39 :
                        sumprice = 139*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ครีมนวดผม 450มิลลิลิตร","จำนวน :",count,"ขวด")
                    elif select == 40 :
                        sumprice = 10*count
                        total+=sumprice
                        print('ท่านได้เลือกสินค้ารหัส :',select,"ทิชชู่ 100แผ่น","จำนวน :",count,"ชิ้น")
            
    elif want == 2 :
        filepro = open("promotion.txt","r",encoding="utf8")
        print("="*10,"PROMOTION!!!","="*10)
        for i in filepro:
            print("\t"+i)
        filepro.close()

    
            
    elif want == 3 :
       print("="*10,"คำสั่งซื้อของคุณ","="*10)
       for i in market :
           print("รหัสสินค้าที่ท่านเลือก : ",i)
       print("ราคาสินค้าไม่รวมส่วนลด =",total,"บาท")
       if total >=150 and total <200 :
           total = total - 5
           print("ราคาสินค้าหลังหักส่วนลด 5 บาท =",total,"บาท")
       elif total >=200 and total <250 :
           total = total - 10
           print("ราคาสินค้าหลังหักส่วนลด 10 บาท =",total,"บาท")
       elif total >= 250 :
           total = total - 20
           print("ราคาสินค้าหลังหักส่วนลด 20 บาท =",total,"บาท")
       else:
           print("ยอดคำสั่งซื้อของท่านไม่ถึงกำหนด ไม่สามารถใช้ส่วนลดได้ =",total,"บาท")

    elif want == 0 :
        print("="*10,"จบการสั่งซื้อ","="*10)
        if len(market) > 0 :
            print("หากต้องการทราบราคาสินค้า กรุณากดย้อนกลับ และเลือกหมายเลข3 เพื่อดูการสั่งซื้อ ค่ะ")
            restart = input("ต้องการกลับไปหรือไม่ ? หากต้องการกด y หากไม่กด n :")
            restart = restart.lower()
            if restart == "y" :
                pass
            elif restart == "n" :
                print(">>ท่านสามารถเลือกจ่ายเงินโดยสแกนคิวอาร์โค้ดหรือชำระเงินสดได้ที่จุดรับสินค้าค่ะ<<")
                print("\t"+"กรุณารอสินค้าสักครู่ค่ะ"+"\t"+"ขอบคุณที่ใช้บริการค่ะ")
                break
        elif len(market) <= 0 :
            restart = input("ท่านไม่ได้เลือกสินค้า ต้องการกลับไปเลือกหรือไม่ ? หากต้องการกด y หากไม่กด n :")
            restart = restart.lower()
            if restart == "y" :
                pass
            elif restart == "n" :
                print("ท่านไม่ได้เลือกสินค้าใด")
                break
       
   
        
    
    
       
       

           
            
    
   
            
            

