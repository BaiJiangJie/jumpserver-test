<div align="center">
  <a name="readme-top"></a>
  <a href="https://jumpserver.org/index-en.html"><img src="https://download.jumpserver.org/images/jumpserver-logo.svg" alt="JumpServer" width="300" /></a>
  
## An open-source PAM tool (Bastion Host)

[![][license-shield]][license-link][![][discord-shield]][discord-link][![][docker-shield]][docker-link][![][github-release-shield]][github-release-link][![][github-stars-shield]][github-stars-link]

**英語**·[簡體中文](./README.zh-CN.md)

</div>
<br/>

## 什麼是JumpServer？

JumpServer 是一款開源特權存取管理 (PAM) 工具，可透過 Web 瀏覽器為 DevOps 和 IT 團隊提供對 SSH、RDP、Kubernetes、資料庫和 RemoteApp 端點的隨選安全存取。

![JumpServer Overview](https://github.com/jumpserver/jumpserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## 快速入門

準備一個乾淨的Linux伺服器（64位，> = 4c8g）

```sh
curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh | bash
```

在瀏覽器中造訪 JumpServer`http://your-jumpserver-ip/`

-   使用者名稱:`admin`
-   密碼：`ChangeMe`

[![JumpServer Quickstart](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "JumpServer Quickstart")

## 截圖

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

## 成分

JumpServer由多個關鍵元件組成，共同構成JumpServer的功能框架，為使用者提供全面的營運管理和安全控制能力。

| 專案                                                 | 地位                                                                                                                                                   | 描述                                |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [莉娜](https://github.com/jumpserver/lina)           | <a href="https://github.com/jumpserver/lina/releases"><img alt="Lina release" src="https://img.shields.io/github/release/jumpserver/lina.svg" /></a> | JumpServer Web UI                 |
| [官](https://github.com/jumpserver/luna)            | <a href="https://github.com/jumpserver/luna/releases"><img alt="Luna release" src="https://img.shields.io/github/release/jumpserver/luna.svg" /></a> | JumpServer Web 終端                 |
| [尺寸](https://github.com/jumpserver/koko)           | <a href="https://github.com/jumpserver/koko/releases"><img alt="Koko release" src="https://img.shields.io/github/release/jumpserver/koko.svg" /></a> | JumpServer 字元協定連接器                |
| [獅子](https://github.com/jumpserver/lion)           | <a href="https://github.com/jumpserver/lion/releases"><img alt="Lion release" src="https://img.shields.io/github/release/jumpserver/lion.svg" /></a> | JumpServer 圖形協定連接器                |
| [Chen](https://github.com/jumpserver/chen)         | <a href="https://github.com/jumpserver/chen/releases"><img alt="Chen release" src="https://img.shields.io/github/release/jumpserver/chen.svg" />     | JumpServer Web 資料庫                |
| \[剃刀](https&#x3A;//github.com/jumpserver/razor)    | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                            | JumpServer EE RDP 代理連接器           |
| \[修補匠](https&#x3A;//github.com/jumpserver/tinker)  | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                          | JumpServer EE 遠端應用程式連接器 (Windows) |
| \[熊貓](https&#x3A;//github.com/jumpserver/Panda)    | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                           | JumpServer EE 遠端應用程式連接器 (Linux)   |
| \[馬格努斯](https&#x3A;//github.com/jumpserver/magnus) | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                          | JumpServer EE 資料庫代理連接器            |

## 貢獻

歡迎提交PR來貢獻。請參閱 \[CONTRIBUTING.md]\[contributing-link] 以了解指南。

## 安全

JumpServer 是一款關鍵任務產品。安裝部署請參考基本安全建議。如果您遇到任何安全相關問題，請直接與我們聯絡：

-   電子郵件：support@fit2cloud.com

## 執照

Copyright (c) 2014-2024 飛致雲 FIT2CLOUD, All rights reserved.

根據 GNU 通用公共授權版本 3 (GPLv3) 授權（「授權」）；除非遵守許可證，否則您不得使用此文件。您可以在以下位置取得許可證副本：

https&#x3A;//www.gnu.org/licenses/gpl-3.0.html

除非適用法律要求或書面同意，否則根據許可證分發的軟體均以「原樣」分發，不附帶任何明示或暗示的保證或條件。請參閱許可證，了解許可證下管理權限和限制的特定語言。

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
