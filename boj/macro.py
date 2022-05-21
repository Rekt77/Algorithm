import macroClass

if __name__ == "__main__":
    id = "timtaeil"
    pw = "123abc!@#"
    user = macroClass.Naver(id,pw)
    user.add_urls("reservation","https://booking.naver.com/booking/6/bizes/140836")
    wb = macroClass.webDriver(user.urls["reservation"])
    wb.NaverReserv(user)