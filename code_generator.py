import qrcode

features = qrcode.QRCode(version=1,
                         box_size=40,
                         border=3)

features.add_data('https://www.youtube.com/c/GeeksForGeeksVideos')

features.make(fit= True)

generator_image = features.make_image(fill_color= "blue",back_color = "white")

generator_image.save('image2.png')
