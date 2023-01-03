import re

email_pattern = re.compile(r'[\w._%+-]+@[\w\.-]+\.[a-zA-Z]{2,4}')
phone_pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4,6}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4,6}|\d{3,4}[-\.\s]??\d{4,6})')
plat_pattern = re.compile(r'[A-Z]{1,2}\s\d{1,4}\s[A-Z]{1,3}')

text = 'Halo semua, namaku Andy Joe. Kemarin smartphoneku mendapat SMS tagihan Pinjaman Online dari nomor 08004398499. Selain itu emailku juga mendapatkan pesan serupa dari debtcollector@pinjolninuninu.com. Ternyata salah satu temanku menjadikan nomor telepon dan emailku sebagai penanggungjawab pinjaman onlinenya :(. Tak lama sosok pria berbadan bongsor datang ke rumahku dengan menggunakan mogenya. Ia menanyakan keberadaan temanku yang meminjam uang di perusahaan Pinjol tersebut. Aku yang tak tahu keberadaannya pun menjawab apa adanya. Tak lama kemudian pria tersebut pergi dan segera kuambil gambar mogenya dengan plat PO 3030 AY. Setelah itu aku menghubungi temanku dan meminta penjelasan kepadanya'
text

emails = re.findall(email_pattern, text)
emails

phone = re.findall(phone_pattern, text)
phone

plat = re.findall(plat_pattern, text)
plat

news = 'Halo Fauzi, Aku tadi habis didatangi debtcollector. Dia mengirimiku pesan lewat nomornya yaitu nomor_debtcollector dan emailnya yaitu email_debtcollector. Dia bilang kamu jadiin nomorku dan emailku sebagai penanggungjawab. Bisa tolong jelasin? Terus aku tadi juga sempet foto motor yg dipake mas debtcollector. Plat nomornya plat'
news

x = re.sub('nomor_debtcollector', phone[0], news)
x1 = re.sub('email_debtcollector', emails[0], x)
x2 = re.sub('plat', plat[0], x1)

x2

"""Tugas 2 (Hapus Tanda [?.,])"""

news1 = re.sub('[?,.]', '', x2)
news1