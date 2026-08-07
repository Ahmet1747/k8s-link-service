# ⭐ (Bonus) HTTPS / Custom Domain 🔒

**Süre:** ~yarım–1 gün · **Ön koşul:** Milestone 4 (canlı URL) · **Amaç:** "Gerçek site"
hissini tamamlamak: TLS (https) ve/veya kendi alan adı.

Branch: `git checkout -b bonus/https`

## Seçenek A — HTTPS (TLS) — cert-manager + Let's Encrypt
1. k3s'e **cert-manager** kurun (Helm).
2. Let's Encrypt için bir **ClusterIssuer** (HTTP-01 challenge — public 80 portu gerekir).
3. Ingress'e TLS ekleyin → `https://` çalışsın (geçerli sertifika).
   > Not: Let's Encrypt bir **hostname** ister (IP'ye sertifika vermez). Bir domain'iniz
   > yoksa ücretsiz bir subdomain (ör. nip.io/sslip.io) kullanabilirsiniz.

## Seçenek B — Custom Domain
1. Bir alan adı (ör. Route 53 veya ücretsiz bir servis) → EC2 public IP'ye **A kaydı**.
2. Ingress host'unu domain'e ayarlayın; (A ile birleştirip) `https://alanadi/` yapın.

## Definition of Done ✅
- [ ] Uygulamaya **https** ile erişiliyor (geçerli sertifika) VEYA custom domain çalışıyor
- [ ] Ingress/host yapılandırması repoda · PR (mentor review) → merge
- [ ] 📸 Adres çubuğunda kilit/domain görünen ekran görüntüsü → portfolyo

## Neden önemli? 🎯
HTTPS ve gerçek bir alan adı, projeyi "demo" olmaktan çıkarıp **üretim gibi** gösterir —
portfolyoda ekstra güven verir.
