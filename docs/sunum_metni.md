# 🎙️ Capstone Projesi Sunum Metni (20 Dakika)

**Hedef Kitle:** Mentörler / Teknik Ekip
**Sunum Tarzı:** Kendinden emin, teknik terimlere hakim, karşılaşılan sorunları ve çözümlerini dürüstçe anlatan bir DevOps Mühendisi.

---

## 🕒 0-3. Dakika: Giriş ve Proje Amacı (Buz Kırıcı)

**[Ekranda Slayt 1: Başlık ve Mimari Diyagramı]**

"Herkese merhaba. Bugün sizlere staj süresince geliştirdiğim 'Cloud Native URL Shortener' projesini sunacağım. 

Bu projeye başlarken amacım sadece çalışan bir kod yazmak değil; bir uygulamanın fikirden çıkıp, güvenli bir şekilde sunuculara otomatik olarak taşındığı, izlendiği ve kendi kendini yönetebildiği gerçek bir 'Production' (Canlı) ortamı tasarlamaktı.

Python (FastAPI) ve PostgreSQL kullanarak yazdığım URL kısaltıcı uygulamamı, uçtan uca modern DevOps pratikleriyle nasıl paketlediğimi, dağıttığımı ve gözlemlediğimi adım adım anlatacağım."

---

## 🕒 3-7. Dakika: Mimari Tasarım ve Altyapı Kararları (IaC)

**[Ekranda Slayt 2: Mimari (Mermaid) Grafiği]**

"Mimari tasarıma baktığımızda klasik bir 3 katmanlı yapı yerine tamamen bulut yerleşik (cloud-native) bir yaklaşım izledim. 

Altyapıyı ayağa kaldırmak için **Terraform** kullandım. AWS üzerinde VPC, Security Group, RDS (Veritabanı) ve EC2 instance'larını kod (IaC) olarak saniyeler içinde oluşturabildim.

**Önemli Bir Mühendislik Kararı:** Kubernetes ortamı olarak AWS'in yönetilen hizmeti olan EKS'i kullanmak yerine, EC2 üzerine hafif sıklet bir Kubernetes dağıtımı olan **K3s** kurmayı tercih ettim. Bunun en büyük sebebi, EKS'in getirdiği yüksek aylık maliyetlerden kaçınırken, gerçek ve %100 uyumlu bir Kubernetes deneyimini yaşamak istememdi. K3s sayesinde çok düşük RAM tüketimiyle tam teşekküllü bir cluster elde ettim. Uygulamayı dış dünyaya açmak için ise Ingress controller olarak Traefik kullandım."

---

## 🕒 7-12. Dakika: CI/CD Boru Hattı (Otomasyonun Gücü)

**[Ekranda Slayt 3: GitHub Actions Ekranı veya CI/CD Şeması]**

"Uygulamanın dağıtımı için **GitHub Actions** ile kapsamlı bir CI/CD boru hattı (pipeline) inşa ettim. Boru hattımız 3 ana adımdan oluşuyor: Test, Build & Push ve Deploy.

1. **Test ve Lint (CI):** Geliştirici kodu pushladığında önce Python testleri (Pytest) ve Lint (Ruff) çalışıyor. Kod standartlara uymazsa boru hattı kırılıyor ve bozuk kodun canlıya çıkması engelleniyor.
2. **Build ve AWS ECR (CI):** Testler geçerse kod, Docker imajına dönüştürülüyor ve AWS ECR'a her seferinde GitHub SHA etiketi (benzersiz bir kimlik) ile pushlanıyor.
3. **Continuous Deployment (CD):** İşte en sevdiğim kısım burası. K3s, AWS ECR'dan imaj çekerken kimlik doğrulamaya ihtiyaç duyar. Pipeline'ımız, AWS'den anlık bir ECR şifresi üretiyor ve bunu K3s'e bir 'Secret' olarak enjekte ediyor. Ardından **Helm** devreye girerek yeni imaj versiyonunu sıfır kesintiyle (zero-downtime) sunucuya dağıtıyor. Biz sadece kodu pushluyoruz, arkada her şey otomatik güncelleniyor."

---

## 🕒 12-16. Dakika: Gözlemlenebilirlik (Observability) ve Hata Ayıklama

**[Ekranda Slayt 4: Grafana Dashboard'u ve Slack Bildirimleri]**

"Sistemi kurup bırakmadım, çünkü kör bir sistem yönetilemez. Gözlemlenebilirlik (Observability) için **Prometheus, Grafana ve Loki** üçlüsünü yine Helm ile K3s üzerine kurdum.

*(Dürüstlük anı:)* Burada çok öğretici bir hata yaşadım. Prometheus'u kurduktan sonra uygulamadan veri çekmediğini fark ettim. Logları incelediğimde sorunun kodlarda değil, uygulamanın Kubernetes `Service` objesinde 'port name' (port ismi) ve 'label' eksikliğinden kaynaklandığını buldum. Prometheus isimsiz portlara kördü! Bunu düzeltip repoya pushladığımda CI/CD devreye girdi ve grafikler anında fırladı.

- Grafana'da **RED (Rate, Error, Duration)** metriklerini izlediğim özel bir PromQL paneli tasarladım.
- **Loki** ile logları toplayarak, kasıtlı olarak attığım 404 hatalarını LogQL ile nokta atışı bulabildim.
- **Alertmanager** ile bir kural tanımladım: 'Eğer uygulamanın podu çökerse ve 1 dakika boyunca kapalı kalırsa Slack'ten beni uyar'. 

**[Canlı Demo veya Screenshot:]** Görebileceğiniz gibi, uygulamayı kasıtlı olarak kapattığımda (scale 0), 1 dakika sonra Slack kanalıma Kırmızı renkli bir **FIRING** mesajı düşüyor. Uygulamayı ayağa kaldırdığımda ise anında Yeşil renkli **RESOLVED** mesajı geliyor."

---

## 🕒 16-18. Dakika: Bonus Görev - Custom Domain & HTTPS

**[Ekranda Slayt 5: ahmetops.com kilit ikonu ve Cert-Manager]**

"Son olarak projeyi tam bir 'Production Ready' seviyeye çıkarmak için **Bonus** görevini tamamladım. 

Cloudflare üzerinden `ahmetops.com` alan adımı satın aldım ve DNS Only (Gri bulut) olarak AWS EC2 public IP adresime yönlendirdim. 
Kubernetes içine **Cert-Manager** kurdum ve Let's Encrypt ile konuşan bir `ClusterIssuer` yapılandırdım. Ingress ayarlarıma TLS eklediğim an, Cert-Manager otomatik olarak HTTP-01 challenge yaptı ve benim için gerçek bir SSL sertifikası üretti. Artık uygulamam tamamen güvenli ve kilit ikonuna sahip."

---

## 🕒 18-20. Dakika: Ne Öğrendim ve Kapanış (Q&A)

**[Ekranda Slayt 6: Ne Öğrendim?]**

"Bu devasa projeyi toparlamak gerekirse, edindiğim en büyük tecrübeler şunlar oldu:
1. **CrashLoopBackOff korkutucu değildir:** K8s'te hata okumayı, `kubectl describe` ve `logs` kullanmayı öğrendim. Hatalar aslında sistemin bizimle konuşma şekliymiş.
2. **Otomasyonun Gücü:** Altyapıyı Terraform ile kodlamak ve deployment'ı GitHub Actions'a bırakmak, bana aynı altyapıyı 100 kere bile olsa hatasız kurabilme güveni verdi.
3. **Secret Yönetimi:** Sistemlerin birbiriyle (örneğin K3s ve AWS ECR) konuşurken yetkilendirme süreçlerinin ne kadar hassas olduğunu kavradım.

Beni dinlediğiniz için çok teşekkür ederim. Tasarım veya karşılaştığım zorluklarla ilgili sorularınız varsa memnuniyetle cevaplayabilirim."
