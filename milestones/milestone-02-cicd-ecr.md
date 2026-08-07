# Milestone 2 — CI/CD → ECR ⚙️

**Süre:** ~1 gün · **Amaç:** Her push'ta otomatik **test → image build → ECR'a push**.

Branch: `git checkout -b milestone/02-cicd`

> Referans: 3. hafta (GitHub Actions). AWS erişimi **GitHub Secrets** + dar yetkili CI kullanıcısı.

## Yapılacaklar
1. **ECR repository** oluşturun (`url-shortener`).
2. **CI IAM kullanıcısı** (dar yetkili): kendi policy'nizi yazmayın — hazır **AWS managed
   policy** ekleyin: **`AmazonEC2ContainerRegistryPowerUser`** (ECR push/pull). Access key üretin.
3. GitHub → Secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` (region variable olarak).
   **YAML'a düz yazmayın.**
4. `.github/workflows/ci.yml`:
   - `on: push` (+ PR'da test).
   - **test** job: `pytest` + lint.
   - **build-push** job (`needs: test`): `configure-aws-credentials` (secret'larla) → ECR'a
     login → image'ı **`github.sha`** ile tag'leyip push (+ `latest`).
5. Push edip Actions'ta yeşili görün; ECR'da image'ı doğrulayın.

## Definition of Done ✅
- [ ] Push → test → build → **ECR'a versiyonlu image** otomatik çalışıyor
- [ ] AWS erişimi dar yetkili CI kullanıcısı + GitHub Secrets ile (YAML'da key yok)
- [ ] Image `github.sha` ile tag'li (izlenebilir) · PR (mentor review) → merge

## Neden önemli? 🎯
Otomatik, tutarlı, testten geçmiş image üretimi; güvenilir deploy'un ön koşuludur. Artık
"bende çalışıyordu" yok — her sürüm izlenebilir.
