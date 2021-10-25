def toThaiNumber(input_number):
    thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
    unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")
    number = input_number
    i = len(number)
    f = len(number) - 1
    tmp_number = ""
    result = ""
    print(f)
    for c in number:
        i -= 1
        if i > 6:
            x = i - 6
        else:
            x = i
        unit_part = unit[x];
        if c == '1' and x == 0 and tmp_number != '0':
            thai_part = "เอ็ด";
            print("i = {}, x = {} เอ็ด 1".format(i, x))
        elif c == '1' and i == 6 and f > 6 and tmp_number != '0':
            thai_part = "เอ็ด";
            print("i = {}, x = {} เอ็ด 2".format(i, x))
        elif c == '1' and x == 1:
            thai_part = "";
            print("i = {}, x = {}".format(i, x))
        elif c == '2' and x == 1:
            thai_part = "ยี่";
            print("i = {}, x = {} ยี่".format(i, x))
        elif c == '0':
            thai_part = "";
            unit_part = "";
            print("i = {}, x = {}".format(i, x))
        else:
            thai_part = thai_number[int(c)];
            print("i = {}, x = {} {}".format(i, x, thai_part))
            
        strnumber = thai_part + unit_part
        result = result + strnumber    
        tmp_number = c 
        # print("Index {}, number {} {} {}".format(x, c, thai_number[int(c)], unit[x]))
        
    return result
    
def coreThai(input_number):
    n = input_number
    arr = n.split('.')
    result = toThaiNumber(arr[0])
    if len(arr) > 1:
        result = result + "จุด" + toThaiNumber(arr[1])
    return result
    
print(coreThai('11213011.13'))
