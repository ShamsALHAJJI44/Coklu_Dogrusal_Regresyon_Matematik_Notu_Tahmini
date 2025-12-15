# ML Matematik Notu Tahmini

Bu projenin amacı, *StudentsPerformance* veri seti kullanılarak öğrencilerin **matematik notlarını** tahmin eden bir **Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli geliştirmek ve eğitilen modeli **Flask tabanlı bir web uygulaması** aracılığıyla kullanıma sunmaktır.

---

## Veri Seti

**StudentsPerformance.csv**

Veri seti aşağıdaki değişkenleri içermektedir:

- Cinsiyet  
- Irk / Etnik grup  
- Ebeveyn eğitim seviyesi  
- Öğle yemeği türü  
- Test hazırlık kursu  
- Okuma (Reading) notu  
- Yazma (Writing) notu  
- **Matematik notu (hedef değişken)**  

---

## Veri Ön İşleme

Colab Notebook içerisinde aşağıdaki veri ön işleme adımları uygulanmıştır:

- Eksik veri analizi yapılmış, veri setinde eksik değer bulunmadığı görülmüştür  
- Kategorik değişkenler için **One-Hot Encoding** uygulanmıştır  
- Dummy trap oluşmaması için `drop_first=True` kullanılmıştır  
- Bağımsız değişkenler (X) ve hedef değişken (y) ayrılmıştır  

---

## Özellik Seçimi – Backward Elimination

**Backward Elimination** yöntemi, *statsmodels* kütüphanesinin **OLS (Ordinary Least Squares)** metodu kullanılarak uygulanmıştır.

- Değişkenlerin p-değerleri incelenmiştir  
- Değişkenlerin büyük bir kısmının istatistiksel olarak anlamlı olduğu gözlemlenmiştir  
- Bu nedenle ek bir özellik eleme işlemi yapılmamıştır  

---

## Model Eğitimi

- Kullanılan algoritma: **Çoklu Doğrusal Regresyon**  
- Eğitim / Test oranı: **%80 / %20**

### Model Performansı

Eğitilen model aşağıdaki performans değerlerine sahiptir:

- **R² Skoru:** ≈ 0.88  
- **MAE (Mean Absolute Error):** ≈ 4  
- **MSE (Mean Squared Error):** ≈ 29  

Bu sonuçlar, modelin matematik notlarını yüksek doğrulukla tahmin edebildiğini göstermektedir.

---

## Modelin Kaydedilmesi

Eğitilen regresyon modeli **pickle** kütüphanesi kullanılarak kaydedilmiştir:

model.pkl

Bu model, Flask web uygulaması içerisinde tekrar eğitilmeye gerek kalmadan kullanılmaktadır.

---

## Flask Web Uygulaması

Kullanıcıların öğrenci bilgilerini girerek matematik notu tahmini alabilmesi için **Flask tabanlı bir web arayüzü** geliştirilmiştir.

### Arayüz Özellikleri

- Açılır menüler (dropdown) ile kolay veri girişi  
- Tahmin sonucunun aynı sayfada gösterilmesi  
- Reset butonu ile form temizleme  
- Basit ve kullanıcı dostu tasarım  

Web uygulaması, `model.pkl` dosyasını yükleyerek tahmin işlemini gerçekleştirmektedir.

---

## Projenin Çalıştırılması

### 1. Gerekli kütüphanelerin yüklenmesi

pip install -r requirements.txt

### 2. Flask uygulamasının çalıştırılması

python app.py

### 3. Tarayıcıdan erişim

http://127.0.0.1:5000/


---

## Kullanılan Teknolojiler

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- StatsModels  
- Flask  
- HTML / CSS  

---

## Öğrenci Bilgileri

Ad Soyad: **Shams AL HAJJI**   
Ders: **Makine Öğrenmesi**  
Proje: **3. Proje – Çoklu Doğrusal Regresyon ve Flask Uygulaması**

---

## Sonuç

Bu projede, öğrencilerin matematik notlarını tahmin etmeye yönelik bir çoklu doğrusal regresyon modeli başarıyla geliştirilmiştir.  
Model, yüksek performans göstermiş ve Flask tabanlı bir web arayüzü ile kullanıma sunularak proje gereksinimleri eksiksiz şekilde karşılanmıştır.
