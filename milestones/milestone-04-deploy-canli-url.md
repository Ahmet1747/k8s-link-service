# Milestone 4 — Helm Deploy + Ingress → CANLI URL 🚀

**Süre:** ~1 gün · **Amaç:** ECR'daki image'ı k3s'e **Helm** ile deploy edip **public bir URL**'den
erişilebilir yapmak. (Projenin "canlı" olduğu an!)

Branch: `git checkout -b milestone/04-deploy`

> Referans: 4. hafta (k8s/Helm/Ingress). k3s'in dahili **Traefik** ingress'i kullanılır.

## Yapılacaklar (`helm/` altında)
1. Uygulamanız için bir **Helm chart** yazın:
   - **Deployment:** image = **ECR** image'ınız (`:github.sha`), `replicas: 2`.
   - **Service** + **Ingress** (Traefik): EC2'nin public IP'si / (varsa) host üzerinden erişim.
   - **ConfigMap/Secret:** `DATABASE_URL` → RDS endpoint (şifre **Secret**, dummy değil gerçek
     ama repoda **değil** — `--set` veya Secret ile).
   - **liveness/readiness probe:** `/health`.
2. EC2'nin ECR'dan image çekebilmesi için erişim (IAM role veya `ecr login`).
3. Deploy edin:
   ```bash
   helm install url-shortener ./helm/url-shortener --set image.tag=<sha> ...
   kubectl get pods,svc,ingress
   ```
4. **Canlı URL'yi test edin:** `http://<ec2-public-ip>/` → arayüzü açın, bir URL kısaltın,
   kısa linkin yönlendirdiğini görün. (Uygulama RDS'e yazıyor.)
5. **Rolling update denemesi:** yeni bir image tag deploy edin (`helm upgrade`), kesintisiz geçişi görün.

## Definition of Done ✅
- [ ] Uygulama k3s'te çalışıyor ve **public URL'den erişiliyor** (uçtan uca: UI → API → RDS)
- [ ] Helm ile deploy + probe'lar + rolling update çalışıyor
- [ ] DB şifresi repoda **yok** · PR (mentor review) → merge
- [ ] 📸 **Ekran görüntüsü alın** (çalışan uygulama) → `docs/screenshots/`

## Neden önemli? 🎯
Bu, projenin "gösterilebilir" olduğu andır: gerçek bir sunucuda, gerçek bir DB ile, public bir
adresten çalışan bir uygulama. Portfolyonuzun kalbi burası.
