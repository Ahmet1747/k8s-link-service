# Milestone 6 — Cila + README + Demo + Teardown 🎁

**Süre:** ~yarım–1 gün · **Amaç:** Projeyi **portfolyo-kalite** hâline getirmek, sunmak ve
kaynakları **güvenle kapatmak**.

Branch: `git checkout -b milestone/06-cila`

## Yapılacaklar

### A) Portfolyo README (en önemli çıktı)
`README.md`'yi tamamlayın:
- [ ] Mimari diyagram (mermaid) gömülü
- [ ] Tech-stack rozetleri, canlı URL (kapanmadan önce)
- [ ] **Ekran görüntüleri** (`docs/screenshots/`): çalışan uygulama, Grafana dashboard, yeşil CI/CD
- [ ] "Nasıl çalışır" özeti + "Ne öğrendim" (kendi cümlenizle 3-5 madde)

### B) Demo hazırlığı
- [ ] **Teardown'dan ÖNCE**: tüm ekran görüntülerini ve kısa bir **demo kaydı** (1-2 dk) alın.
- [ ] Sunum akışı: problem → mimari → canlı demo (kısalt + yönlendir) → pipeline → Grafana.

### C) Sosyal medya
- [ ] [docs/paylasim-taslagi.md](../docs/paylasim-taslagi.md)'yi kendinize göre uyarlayın.

### D) Teardown (maliyet güvenliği) — ZORUNLU
- [ ] `terraform destroy` → EC2 + RDS + SG silindi.
- [ ] ECR image'ları (gerekmiyorsa) temizlendi; CI IAM access key **rotate/sil**.
- [ ] **Billing kontrolü**: bu ayki harcama + budget durumu; açık kaynak kalmadı.

## Definition of Done ✅
- [ ] Portfolyo README tamam (diyagram + görüntüler + "ne öğrendim")
- [ ] Ekran görüntüleri + demo kaydı alındı (kalıcı portfolyo)
- [ ] Sunum yapıldı
- [ ] **Tüm AWS kaynakları destroy edildi**, fatura kontrol edildi
- [ ] PR (mentor review) → merge

## Neden önemli? 🎯
Teknik iş kadar **anlatımı** da önemli: iyi bir README + demo, aynı projeyi bir mülakatta
"kazanan" hâle getirir. Teardown ise mühendisliğin görünmez ama kritik disiplinidir.
