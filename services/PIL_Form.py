from PIL import Image,ImageDraw,ImageFont


def schedule_img(total):
    Image1 = Image.open(r"F:\Sayotest2\sources\aaa.jpg")

    draw =ImageDraw.Draw(Image1)
    for i in range(0,9):
        draw.line((i*199+1,0 ,i*199, 1000), 'cyan')

    for i in range(0,8):
        draw.line((0,i*140 ,1600, i*140), 'cyan')

    font = ImageFont.truetype("F:\Sayotest2\sources\STZHONGS.TTF", 25, encoding="unic")#设置字
    k = 0
    for i in range(0,7):
        for j in range(0,8):
            str1=str(i)
            str2=str(j)
            str3="["+str1+","+str2+"]"
            try:
                if k == 51 :
                    break
                # draw.text((j*213, i*150), str(k), 'fuchsia', font)
                decor_total = total[k]
                draw.text((j*213, i*150), decor_total, 'fuchsia', font)
            except Exception as e:
                try:
                    decor_total = total[k][0]+"\n"+ total[k][1]+"\n" + total[k][2]
                    draw.text((j * 213, i * 150), decor_total, 'fuchsia', font)
                    k = k+1
                    continue
                except Exception:
                    try:
                        decor_total = total[k][0] + "\n" + total[k][1]
                        draw.text((j * 213, i * 150), decor_total, 'fuchsia', font)
                        k = k + 1
                        continue
                    except Exception:
                        decor_total = total[k][0]
                        draw.text((j * 213, i * 150), decor_total, 'fuchsia', font)
                        k = k + 1
                        continue

            k = k + 1



    #draw.line((0,0) +Image1.size, fill=128)
    Image1.save(r"F:\Sayotest2\sources\new.jpg", "JPEG")