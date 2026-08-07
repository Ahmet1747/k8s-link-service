# Milestone 3 — Terraform → AWS (EC2 + k3s + RDS) 🏗️

**Süre:** ~1–1.5 gün · **Amaç:** Altyapıyı **kod olarak** (Terraform) kurmak: bir EC2 (üzerinde
k3s) + RDS Postgres.

Branch: `git checkout -b milestone/03-terraform`

> Referans: 2. hafta (EC2/RDS) + 3. hafta (Terraform). Kurallar: `us-east-1`, teardown, secret yok.
> 💸 **`t3.small` + `db.t3.micro` Free Tier değildir** — kısa kullanın, budget alarmları açık.

## 🧰 Ön Gereksinim
- **Terraform** + **AWS CLI** (yapılandırılmış).

## Yapılacaklar (`infra/` altında)
1. Terraform ile:
   - **Security Group:** SSH (22) sadece kendi IP; HTTP (80/443) public (uygulama erişimi);
     app portu gerekiyorsa.
   - **EC2** (`t3.small`, Ubuntu), tag'li (`Owner`, `Project=capstone`), key pair.
   - **RDS Postgres** (`db.t3.micro`, public access **No**, sadece EC2 SG'sinden erişim).
   - **Output:** EC2 public IP + RDS endpoint.
2. **k3s kurulumu** (EC2'ye): SSH ile bağlanıp tek satır: `curl -sfL https://get.k3s.io | sh -`
   (veya Terraform `user_data`/`remote-exec` ile otomatik). `kubectl get nodes` → Ready.
   > k3s Ingress için dahili **Traefik** ile gelir (ekstra kurulum yok).
3. `terraform plan` → `apply`; kaynakların oluştuğunu doğrulayın.
4. **state'i commit'lemeyin** (`*.tfstate` gitignore'da).

## Definition of Done ✅
- [ ] EC2 + SG + RDS **Terraform ile** oluştu (konsoldan elle değil), tag'li
- [ ] EC2'de **k3s** çalışıyor (`kubectl get nodes` Ready)
- [ ] RDS private (sadece EC2'den erişilir); `*.tfstate` repoda yok
- [ ] PR (mentor review) → merge · (denemeler sonrası `terraform destroy`, Milestone 6'da final teardown)

## Neden önemli? 🎯
Altyapının kodla, tekrar üretilebilir ve gözden geçirilebilir şekilde kurulması, capstone'u
"elle tıklanmış bir demo"dan **gerçek bir sistem**e dönüştürür.
