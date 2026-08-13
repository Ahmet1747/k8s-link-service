<!--
  ⚠️ BU DOSYA SİZİN PORTFOLYO README'NİZDİR — capstone bitince bunu paylaşacaksınız.
  Aşağıdaki [KÖŞELİ] alanları kendinize göre doldurun, örnekleri güncelleyin,
  ekran görüntülerini ekleyin. Amaç: birinin repoya girince "vay" demesi.
  Capstone'u NASIL yapacağınız: docs/capstone-rehberi.md + milestones/
-->

# 🔗 Cloud-Native URL Shortener

Küçük bir URL kısaltıcının **uçtan uca DevOps hattıyla** AWS'de çalıştırılması: CI/CD ile
build, Terraform ile altyapı, k3s (Kubernetes) ile deploy, Prometheus/Grafana/Loki ile izleme.

> Bir DevOps stajının capstone projesi — 6 haftalık öğrenimin tek çatı altında birleşimi.

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonaws&logoColor=white)
![Kubernetes](https://img.shields.io/badge/k3s-FFC61C?logo=kubernetes&logoColor=black)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

**🌐 Canlı:** `https://ahmetops.com/`  ·  **👤 Yapan:** [Ahmet Can Bezikoğlu](https://github.com/Ahmet1747)

---

## ✨ Özellikler
- `POST /shorten` ile uzun URL → kısa kod; `GET /{code}` ile yönlendirme
- Postgres (AWS RDS) ile kalıcı depolama
- `/health` (probe) + `/metrics` (Prometheus) + basit web arayüzü
- **Tam otomatik CI/CD**: push → test → image → ECR → deploy
- **Kod olarak altyapı** (Terraform) ve **izlenebilirlik** (Grafana dashboard + alert)

## 🏗️ Mimari
> Diyagram: [docs/mimari.md](docs/mimari.md)

```mermaid
flowchart LR
    dev[git push] --> ci[GitHub Actions] --> ecr[(ECR)]
    ci -->|helm deploy| app[URL Shortener @ k3s/EC2]
    app --> rds[(RDS Postgres)]
    user[Kullanıcı] --> ing[Ingress] --> app
    app --> mon[Prometheus/Grafana/Loki]
```

## 🧰 Tech Stack
Python (FastAPI) · Docker · GitHub Actions · AWS (ECR, EC2, RDS) · Terraform · k3s + Helm ·
Prometheus · Grafana · Loki

## 🚀 Nasıl Çalışır (özet)
1. `git push` → GitHub Actions testleri çalıştırır, Docker image build edip **ECR**'a push eder.
2. **Terraform** AWS altyapısını (EC2+k3s, RDS) kurar.
3. **Helm** uygulamayı k3s'e deploy eder; **Ingress** ile public URL açılır.
4. **Prometheus/Grafana/Loki** metrikleri ve logları toplar; alarm kuralları uyarır.


## 📸 Ekran Görüntüleri
- Çalışan uygulama: `![app](docs/screenshots/app.png)`
- Grafana dashboard: `![grafana](docs/screenshots/grafana.png)`
- Yeşil CI/CD pipeline: `![ci](docs/screenshots/pipeline.png)`

## 📚 Ne Öğrendim
- 1. Önceden sadece `kubectl get pods` yazıp geçerdim. Ancak bu projede karşılaştığım *CrashLoopBackOff* ve *ImagePullBackOff* hataları sayesinde `kubectl logs` ve `kubectl describe` komutlarıyla loglara bakarak hata ayıklamayı  öğrendim.

- 2.  GitHub Actions üzerinden CI/CD pipeline otomatik bir şekilde yapmayı öğrendim. AWS ECR'a bağlanıp, oradan aldığım token'ı K3s içindeki Helm'e güvenli bir şekilde aktarmak ise projenin zorlandığım yerlerindendi.

- 3.  Prometheus, Grafana ve Loki üçlüsü ile bir sistemin her saniyesi izlenebilen canlı bir organizmaya dönüştüğünü öğrendim. 

- 4. AWS konsolundan elle tıklayarak EC2 veya RDS açmak yerine, bunu Terraform ile kodlayarak yapmak başlarda zor geldi. Ancak tüm altyapımın tek bir `terraform apply` komutuyla ayağa kalkması gerçekten çok kullanışlı onu öğrendim.

- 5.  Projemin en sonunda Cert-Manager kullanarak Let's Encrypt'ten tamamen otomatize bir şekilde SSL sertifikası basmak ve bunu `ahmetops.com` özel alan adıma bağlamak gibi profesyonel bir uygulama haline gettirmeyi öğrendim.

## ⚙️ Yerel Geliştirme
```bash
# uygulamayı local çalıştır
docker compose up   # veya: uvicorn app.main:app --reload
```

---

*Bu proje bir eğitim/capstone çalışmasıdır. Altyapı maliyet nedeniyle demo sonrası kapatılmıştır
(`terraform destroy`); ekran görüntüleri ve kod referans içindir.*
