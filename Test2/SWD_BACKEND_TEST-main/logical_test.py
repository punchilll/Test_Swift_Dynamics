
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def cal(num):
    numc = [0,0,0,0,0,0,0]
    lennumc = len(numc);
    arr = []
    for i in str(num):
        arr.append(i)
        
    lenarr = len(arr);
    for i in str(num):
        lenarr = lenarr-1
        lennumc = lennumc-1
        numc[lennumc] = int(arr[lenarr])
        
    #print(numc)
    string = tran(numc);
    return string

def tran(arr):
    word1 = ["ล้าน","แสน","หมื่น","พัน","ร้อย","สิบ",""]
    word2 = [[1,"หนึ่ง"],[2,"สอง"],[3,"สาม"],[4,"สี่"],[5,"ห้า"],[6,"หก"],[7,"เจ็ด"],[8,"แปด"],[9,"เก้า"],[0,""]]
    string = ""
    i=0
    while i<len(word1):
        for x in word2:
            if arr[i] == x[0] and arr[i] != 0:
                if i == 5 and arr[i] == 2:
                    string = string+"ยี่"+word1[i]
                elif i == 6 and arr[i] == 1:
                    string = string+"เอ็ด"
                else:
                    string = string+x[1]+word1[i]

        i+=1
    #print(string)
    return string

i = 0
while i < 1:
    print('Input number : ')
    x = int(input())
    if x < 10000000 and x >= 0:
        string = cal(x)
        print(string)
        i = 1;
    else:
        print("กรุณาใส่ใหม่ ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน")
