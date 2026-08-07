# 🎓 Capstone Rehberi — Uçtan Uca Bulut Platformu

Bu hafta yeni bir konu **öğrenmiyoruz**; 5 haftada öğrendiğimiz her şeyi **tek, gerçeğe yakın
bir projede** birleştiriyoruz. Sonuç: **portfolyonuzda / LinkedIn'de paylaşabileceğiniz**,
canlı çalışan bir sistem.

> **Her stajyer kendi repo'sunda, kendi AWS hesabında** bu projeyi kurar (bireysel portfolyo).
> Mentor, milestone PR'larını review eder.

---

## 🎯 Proje: "URL Kısaltıcı" Bulut-Native Platformu
Küçük ama **gerçek** bir uygulama (URL kısaltıcı) sıfırdan alınıp production-benzeri bir hatta
oturtulur:

```
GitHub repo
   → GitHub Actions CI/CD   (test → Docker image build → ECR push)
   → Terraform              (AWS: VPC/EC2/SG + RDS Postgres)
   → EC2 üzerinde k3s       (hafif, gerçek Kubernetes)
   → Helm ile deploy + Ingress (Traefik)  →  CANLI PUBLIC URL
   → Prometheus + Grafana + Loki           (metrik / log / alert)
```

**Hangi hafta nerede:** Docker (imaj) · CI/CD (pipeline) · Terraform (altyapı) · Helm/k8s→k3s
(deploy) · Observability (izleme). Hepsi tek projede.

---

## 🧑‍💻 Senaryo: "Dev ekibi yazdı, DevOps deploy eder"
Bu capstone bir **rol simülasyonudur**: uygulamayı **dev ekibi yazıp teslim etti** (`app/`
klasörü, `app/README-DEV.md` handoff notuyla). **Siz DevOps ekibisiniz** — uygulama koduna
**dokunmazsınız**; işiniz onu **containerize edip CI/CD'ye sokmak, AWS'e deploy etmek ve
izlemek**.

## 🧱 Uygulama (verilmiş — Python / FastAPI · URL kısaltıcı)
- `POST /shorten` → kısa kod üretir, **Postgres (RDS)**'e yazar
- `GET /{code}` → **301** yönlendirir · `GET /health` (liveness) · `GET /ready` (DB'ye bağlı mı)
- `GET /metrics` → **Prometheus** metrikleri · `GET /` → basit web arayüzü
- Config: **`DATABASE_URL`** ortam değişkeninden · Port: **8000** · Testleri hazır (`pytest`)

> Detaylar: [../app/README-DEV.md](../app/README-DEV.md). **Kod yazmıyorsunuz** — Dockerfile,
> pipeline, IaC, Helm chart, monitoring **sizin** işiniz.

---

## 🗺️ Milestone'lar (aşamalı — her biri bir PR)

| # | Milestone | Ana çıktı |
|---|-----------|-----------|
| 0 | Kurulum & Mimari | repo, mimari diyagram, plan, **budget alarm** |
| 1 | Verilen app'i containerize | Dockerfile + compose (siz yazarsınız), local çalışan app |
| 2 | CI/CD → ECR | GitHub Actions: test→build→**ECR**'a versiyonlu push |
| 3 | Terraform → AWS | IaC ile EC2 + **k3s** + RDS Postgres |
| 4 | Deploy + Ingress → **Canlı URL** | Helm ile k3s'e deploy, public erişilebilir uygulama |
| 5 | Observability | Prometheus + Grafana **dashboard** + **alert** + Loki log |
| 6 | Cila + README + Demo + **Teardown** | portfolyo-README, ekran görüntüleri, sunum |
| ⭐ | (Bonus) HTTPS / Domain | cert-manager veya custom domain → "gerçek site" |

Detaylar `milestones/` klasöründe.

---

## 💸 Maliyet & Güvenlik (net kurallar — 2. hafta disiplini)
- **EN BAŞTA** (Milestone 0): aylık **$10 / $25 / $50** budget alarmları + Billing alerts.
- Bölge: **`us-east-1`**.
- Boyutlar: EC2 **`t3.small`** (k3s ~2GB) + RDS **`db.t3.micro`**. → **Free Tier değil**,
  ücretlidir. **Kısa kullanın.**
- **Secret'lar** GitHub Secrets / ortam değişkeni; repoya/AI'a **asla** yazılmaz (DB şifresi, AWS key).
- CI için **dar yetkili IAM kullanıcısı**; hazır **AWS managed policy** eklenir (kendi policy'nizi yazmayın).
- **Milestone 6'da `terraform destroy`** ile her şey silinir. Ama **README + ekran görüntüleri
  + (varsa) demo videosu portfolyoda KALIR** — canlı URL kapansa bile projeniz durur.

---

## 🌟 Portfolyo Odağı (bu haftanın farkı)
Amaç sadece "çalıştı" değil, **gösterebileceğiniz** bir iş çıkarmak:
- **Portfolyo-kalite README** (bu repo'daki `README.md` şablonu): mimari diyagram, tech-stack
  rozetleri, canlı URL, ekran görüntüleri, "ne öğrendim".
- `docs/screenshots/` altına: çalışan uygulama + Grafana dashboard + pipeline (yeşil) görüntüleri.
- `docs/mimari.md`: mimari diyagram.
- `docs/paylasim-taslagi.md`: hazır **LinkedIn/sosyal medya** paylaşım taslağı.

> İpucu: Teardown'dan **önce** tüm ekran görüntülerini ve kısa bir demo kaydını alın.

---

## ✅ Nasıl çalışılır
- Her milestone kendi **branch**'inde → **PR** → mentor review → merge (git hijyeni korunur).
- Takıldığınızda: ilgili haftanın repo'suna geri bakın (her parça orada öğretildi) → mentor.
- "Kopyala-çalıştır" değil; her adımın **neden** orada olduğunu anlatabilecek olun (sunumda sorulacak).
