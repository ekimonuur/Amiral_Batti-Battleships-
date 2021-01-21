# Amiral_Batti-Battleships-
Single Player  Battleship game against computer

Amiral Battı oyunu  Single Player olarak oynanmaktadır.

- Oyun 5x5'lik matris(oyun tahtası) üzerinde oynanmaktadır.
- Oyuncu ve bilgisayar 5'er adet gemiye sahiptir. Oyuncu kendi isteğine göre gemilerini yerleştirmektedir. 
- Oyuncudan 3 tane zorluk seviyesinden birini seçmesi istenir.
- kolay için 'k' --- Orta için 'o' --- Zor için 'z' harfine seçimine göre klavyeden giriş yapmalıdır.
- Kolay seviyesinde 15 atış hakkı, orta için 12 ve zor için 8 atış hakkı verilmiştir. 
- Oyuncu eğer isabetli atış yapmış ise atış hakkında değişiklik olmaz.
- Oyun sizden gemilerinizi yerleştirmek için birer birer  x ve ye koordinatında değerler girmenizi istemektedir. Bu değerler (0, 4) arasında değerler olmalıdır.
- Bilgisayar oyuncusunun gemileri rastgele yerleştirilmektedir.
- Oyun sırasında oyuncu kendi oyun tahtasnın güncel halini görmektedir.
- Atış yapmak için ise yine aynı şekilde sırasıyla x ve y koordinato (0,4) sayı aralığında girilmelidir.
- Oyun iki şekilde biter.
  1. Herhangi bir oyuncunun oyun tahtasında gemi kalmaz ise rakip kazanır
  2. Oyuncunun zorluk seçimyle ona atanan atış hakkı bittiğinde oyun kaybedilir.


-------********--------
Oyunda harita oluşturma, haritaya gemileri yerleştirme, atış yapma ve sonuç belirten fonksiyonlar çalışmaktadır.
Tek çalışmayan işlev bilgisayarın atış yapma algoritmasıdır. Bu algoritamada amacım satırları tek tek ele alarak , her satır içerisinde 1 değerini yani gemi olduğunu bulduğu anda
o satır içerisini girerek her el de doğru atışı yapma şansını en az yüzde 20 ye çıkarmıştır. Choice metodu ile satır içerisinden rastgele değer alınmışıtr. Daha hızlı bulunması için farklı bir algoritma gelişrilebilirdi ama ben oyunun daha uzun sürmesi için bu yolu seçtim. Bu algoritma olmadan düz bir şekilde maksimum yüzde 5'tir. Satır içerisinde birden çok 1 değeri var ise bu oran daha da artar. 
-- Programda class kullanmadım. Classlar ile de aynı şekilde yapabilir.
