print("KULLANICI GİRİŞİ")

sys_kullanıcı_adı="mmurat"
sys_parola="12345"

kullanıcı_adı=input("Kullanıcı Adınızı Giriniz : ")
parola=input("Parolanızı Giriniz : ")

if(kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola) :
    print("parola hatalı...")
elif(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola) :
    print("kullanıcı adı hatalı...")
elif(kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola) :
    print("kullanıcı adı ve parola hatalı...")
else :
    print("Giriş Yapıldı..")