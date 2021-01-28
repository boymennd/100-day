def kich_thuoc(a,b):
    dien_tich = a * b
    son = float(dien_tich/5)
    if dien_tich%5 != 0:
        son +=1
        print(f"bạn cần mua {int(son)} lọ sơn!")
    else:
        print(f"bạn cần mua {son} lọ sơn!")

test_h = int(input("Chiều cao:"))
test_w = int(input("Chiều rộng:"))
kich_thuoc(test_h,test_w)
