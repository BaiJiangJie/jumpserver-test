<div align="center">
  <a name="readme-top"></a>
  <a href="https://jumpserver.org/index-en.html"><img src="https://download.jumpserver.org/images/jumpserver-logo.svg" alt="JumpServer" width="300" /></a>
  
## JumpServer nedir?

JumpServer, DevOps ve IT ekiplerine web tarayıcısı aracılığıyla SSH, RDP, Kubernetes, Veritabanı ve RemoteApp uç noktalarına talep üzerine güvenli erişim sağlayan açık kaynaklı Yetkili Erişim Yönetimi (PAM) aracıdır.

![JumpServer Genel Görünüm](https://github.com/jumpserver/jumpserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## Hızlı Başlangıç

Temiz bir Linux Sunucusu hazırlayın ( 64 bit, >= 4c8g )

```sh
curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh | bash
```

Tarayıcınızdan JumpServer'a `http://your-jumpserver-ip/` adresiyle erişin
- Kullanıcı Adı: `admin`
- Şifre: `ChangeMe`

[![JumpServer Hızlı Başlangıç](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "JumpServer Hızlı Başlangıç")

## Ekran Görüntüleri

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="JumpServer Konsol"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="JumpServer Denetimleri"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="JumpServer Çalışma Masası"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="JumpServer Ayarları"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="JumpServer SSH"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="JumpServer RDP"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="JumpServer K8s"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="JumpServer DB"   /></td>
  </tr>
</table>

## Bileşenler

JumpServer, kullanıcıların operasyon yönetimi ve güvenlik kontrolü için kapsamlı yeteneklere sahip olmasını sağlayan işlevsel çerçeveyi oluşturan birden fazla ana bileşenden oluşur.

| Proje                                                  | Durum                                                                                                                                                                  | Tanım                                                                                                |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/jumpserver/lina)             | <a href="https://github.com/jumpserver/lina/releases"><img alt="Lina sürümü" src="https://img.shields.io/github/release/jumpserver/lina.svg" /></a>                   | JumpServer Web UI                                                                                    |
| [Luna](https://github.com/jumpserver/luna)             | <a href="https://github.com/jumpserver/luna/releases"><img alt="Luna sürümü" src="https://img.shields.io/github/release/jumpserver/luna.svg" /></a>                   | JumpServer Web Terminal                                                                                |
| [KoKo](https://github.com/jumpserver/koko)             | <a href="https://github.com/jumpserver/koko/releases"><img alt="Koko sürümü" src="https://img.shields.io/github/release/jumpserver/koko.svg" /></a>                   | JumpServer Karakter Protokol Bağlayıcı                                                                   |
| [Lion](https://github.com/jumpserver/lion)             | <a href="https://github.com/jumpserver/lion/releases"><img alt="Lion sürümü" src="https://img.shields.io/github/release/jumpserver/lion.svg" /></a>                   | JumpServer Grafikal Protokol Bağlayıcı                                                                |
| [Chen](https://github.com/jumpserver/chen)             | <a href="https://github.com/jumpserver/chen/releases"><img alt="Chen sürümü" src="https://img.shields.io/github/release/jumpserver/chen.svg" />                       | JumpServer Web DB                                                                                     |  
| [Razor](https://github.com/jumpserver/razor)           | <img alt="Chen" src="https://img.shields.io/badge/sürüm-gizli-kırmızı" />                                                                                              | JumpServer EE RDP Proxy Bağlayıcı                                                                      |
| [Tinker](https://github.com/jumpserver/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/sürüm-gizli-kırmızı" />                                                                                            | JumpServer EE Uzaktan Uygulama Bağlayıcı (Windows)                                                    |
| [Panda](https://github.com/jumpserver/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/sürüm-gizli-kırmızı" />                                                                                             | JumpServer EE Uzaktan Uygulama Bağlayıcı (Linux)                                                     |
| [Magnus](https://github.com/jumpserver/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/sürüm-gizli-kırmızı" />                                                                                           | JumpServer EE Veritabanı Proxy Bağlayıcı                                                               |

## Katkı

Katkıda bulunmak için PR göndermeye hoş geldiniz. Lütfen kılavuzlar için [CONTRIBUTING.md][contributing-link] bağlantısına bakın.

## Güvenlik

JumpServer, kritik öneme sahip bir üründür. Kurulum ve dağıtım için Temel Güvenlik Önerilerine bakın. Herhangi bir güvenlik ile ilgili sorunla karşılaşırsanız, doğrudan bizimle iletişime geçin:

- E-posta: support@fit2cloud.com

## License

Copyright (c) 2014-2024 飞致云 FIT2CLOUD, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

<!-- JumpServer resmi bağlantısı -->
[docs-link]: https://jumpserver.com/docs
[discord-link]: https://discord.com/invite/W6vYXmAQG2
[contributing-link]: https://github.com/jumpserver/jumpserver/blob/dev/CONTRIBUTING.md

<!-- JumpServer Diğer bağlantı-->
[license-link]: https://www.gnu.org/licenses/gpl-3.0.html
[docker-link]: https://hub.docker.com/u/jumpserver
[github-release-link]: https://github.com/jumpserver/jumpserver/releases/latest
[github-stars-link]: https://github.com/jumpserver/jumpserver
[github-issues-link]: https://github.com/jumpserver/jumpserver/issues

<!-- Shield bağlantısı -->
[github-release-shield]: https://img.shields.io/github/v/release/jumpserver/jumpserver
[github-stars-shield]: https://img.shields.io/github/stars/jumpserver/jumpserver?color=%231890FF&style=flat-square
[docker-shield]: https://img.shields.io/docker/pulls/jumpserver/jms_all.svg
[license-shield]: https://img.shields.io/github/license/jumpserver/jumpserver
[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb

<!-- Resim bağlantısı -->