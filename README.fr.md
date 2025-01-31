<div align="center">
  <a name="readme-top"></a>
  <a href="https://jumpserver.org/index-en.html"><img src="https://download.jumpserver.org/images/jumpserver-logo.svg" alt="JumpServer" width="300" /></a>
  
## An open-source PAM tool (Bastion Host)

[![][license-shield]][license-link][![][discord-shield]][discord-link][![][docker-shield]][docker-link][![][github-release-shield]][github-release-link][![][github-stars-shield]][github-stars-link]

**Anglais**·[Chinois simplifié](./README.zh-CN.md)

</div>
<br/>

## Qu'est-ce que JumpServer ?

JumpServer est un outil open source de gestion des accès privilégiés (PAM) qui fournit aux équipes DevOps et informatiques un accès à la demande et sécurisé aux points de terminaison SSH, RDP, Kubernetes, Database et RemoteApp via un navigateur Web.

![JumpServer Overview](https://github.com/jumpserver/jumpserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## Démarrage rapide

Préparez un serveur Linux propre (64 bits, >= 4c8g)

```sh
curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh | bash
```

Accédez à JumpServer dans votre navigateur à l'adresse`http://your-jumpserver-ip/`

-   Nom d'utilisateur:`admin`
-   Mot de passe:`ChangeMe`

[![JumpServer Quickstart](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "JumpServer Quickstart")

## Captures d'écran

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="JumpServer Console"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="JumpServer Audits"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="JumpServer Workbench"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="JumpServer Settings"   /></td>
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

## Composants

JumpServer se compose de plusieurs composants clés, qui forment collectivement le cadre fonctionnel de JumpServer, offrant aux utilisateurs des fonctionnalités complètes de gestion des opérations et de contrôle de sécurité.

| Projet                                                 | Statut                                                                                                                                               | Description                                               |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [Lina](https://github.com/jumpserver/lina)             | <a href="https://github.com/jumpserver/lina/releases"><img alt="Lina release" src="https://img.shields.io/github/release/jumpserver/lina.svg" /></a> | Interface utilisateur Web de JumpServer                   |
| [Officier](https://github.com/jumpserver/luna)         | <a href="https://github.com/jumpserver/luna/releases"><img alt="Luna release" src="https://img.shields.io/github/release/jumpserver/luna.svg" /></a> | Terminal Web JumpServer                                   |
| [Taille](https://github.com/jumpserver/koko)           | <a href="https://github.com/jumpserver/koko/releases"><img alt="Koko release" src="https://img.shields.io/github/release/jumpserver/koko.svg" /></a> | Connecteur de protocole de caractères JumpServer          |
| [Lion](https://github.com/jumpserver/lion)             | <a href="https://github.com/jumpserver/lion/releases"><img alt="Lion release" src="https://img.shields.io/github/release/jumpserver/lion.svg" /></a> | Connecteur de protocole graphique JumpServer              |
| [Chen](https://github.com/jumpserver/chen)             | <a href="https://github.com/jumpserver/chen/releases"><img alt="Chen release" src="https://img.shields.io/github/release/jumpserver/chen.svg" />     | Base de données Web JumpServer                            |
| \[Rasoir](https&#x3A;//github.com/jumpserver/razor)    | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                            | Connecteur proxy RDP JumpServer EE                        |
| \[Bricoler](https&#x3A;//github.com/jumpserver/tinker) | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                          | Connecteur d'application distante JumpServer EE (Windows) |
| \[Panda](https&#x3A;//github.com/jumpserver/Panda)     | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                           | Connecteur d'application distante JumpServer EE (Linux)   |
| \[Magnus](https&#x3A;//github.com/jumpserver/magnus)   | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                          | Connecteur proxy de base de données JumpServer EE         |

## Contribuer

Bienvenue à soumettre des PR pour contribuer. Veuillez vous référer à \[CONTRIBUTING.md]\[contributing-link] pour les directives.

## Sécurité

JumpServer est un produit critique. Veuillez vous référer aux recommandations de sécurité de base pour l'installation et le déploiement. Si vous rencontrez des problèmes liés à la sécurité, veuillez nous contacter directement :

-   E-mail : support@fit2cloud.com

## Licence

Copyright (c) 2014-2024 FIT2CLOUD, Tous droits réservés.

Sous licence GNU General Public License version 3 (GPLv3) (la « Licence ») ; vous ne pouvez pas utiliser ce fichier sauf en conformité avec la licence. Vous pouvez obtenir une copie de la licence à

https&#x3A;//www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

<!-- JumpServer official link -->

[docs-link]: https://jumpserver.com/docs

[discord-link]: https://discord.com/invite/W6vYXmAQG2

[contributing-link]: https://github.com/jumpserver/jumpserver/blob/dev/CONTRIBUTING.md

<!-- JumpServer Other link-->

[license-link]: https://www.gnu.org/licenses/gpl-3.0.html

[docker-link]: https://hub.docker.com/u/jumpserver

[github-release-link]: https://github.com/jumpserver/jumpserver/releases/latest

[github-stars-link]: https://github.com/jumpserver/jumpserver

[github-issues-link]: https://github.com/jumpserver/jumpserver/issues

<!-- Shield link-->

[github-release-shield]: https://img.shields.io/github/v/release/jumpserver/jumpserver

[github-stars-shield]: https://img.shields.io/github/stars/jumpserver/jumpserver?color=%231890FF&style=flat-square

[docker-shield]: https://img.shields.io/docker/pulls/jumpserver/jms_all.svg

[license-shield]: https://img.shields.io/github/license/jumpserver/jumpserver

[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb

<!-- Image link -->
