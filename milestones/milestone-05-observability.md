# Milestone 5 — Observability 📈

**Süre:** ~1 gün · **Amaç:** Çalışan uygulamayı **izlenebilir** yapmak: Prometheus + Grafana
dashboard + alarm + Loki log.

Branch: `git checkout -b milestone/05-observability`

> Referans: 5. hafta (Prometheus/Grafana/Loki/Alertmanager). k3s'te kurulur.

## Yapılacaklar (`monitoring/` altında)
1. İzleme yığınını k3s'e kurun (Helm): **kube-prometheus-stack** + **loki-stack**.
   (k3s kaynak için: gerekiyorsa EC2 boyutunu/replica'ları küçük tutun.)
2. Uygulamanızın `/metrics`'ini **ServiceMonitor** ile Prometheus'a scrape ettirin.
3. **Grafana dashboard**: uygulamanız için en az 3 panel — istek oranı, hata oranı, p95 latency
   (RED). Dashboard JSON'unu `monitoring/dashboard.json` olarak repoya ekleyin.
4. **Loki**: uygulama loglarını Grafana'da LogQL ile sorgulayın; bir hata üretip bulun.
5. **Alert**: bir PrometheusRule (ör. "uygulama down" veya "hata oranı yüksek") + Alertmanager
   bir webhook'a (test) yönlendirsin. Bilerek tetikleyip Firing → bildirim → Resolved gösterin.

## Definition of Done ✅
- [ ] Prometheus uygulamanızı scrape ediyor; Grafana'da **RED dashboard** var
- [ ] Loki ile loglar sorgulanıyor
- [ ] En az 1 alarm çalışıyor (tetikleme → bildirim kanıtı)
- [ ] PR (mentor review) → merge
- [ ] 📸 **Grafana dashboard ekran görüntüsü** → `docs/screenshots/`

## Neden önemli? 🎯
"Deploy ettim" yeterli değil; **görebiliyor ve uyarılabiliyor** olmak sistemi production-kalite
yapar. Grafana ekran görüntüsü portfolyonuzun en etkileyici parçalarından biridir.
