<div align="center">
  <a name="readme-top"></a>
  <a href="https://jumpserver.org/index-en.html"><img src="https://download.jumpserver.org/images/jumpserver-logo.svg" alt="JumpServer" width="300" /></a>
  
## 開源的 PAM 工具 (堡壘主機)

[![][license-shield]][license-link]
[![][discord-shield]][discord-link]
[![][docker-shield]][docker-link]
[![][github-release-shield]][github-release-link]
[![][github-stars-shield]][github-stars-link]

**英文** · [簡體中文](./README.zh-CN.md)
</div>
<br/>

## 什麼是 JumpServer？

JumpServer 是一個開源的特權訪問管理 (PAM) 工具，為 DevOps 和 IT 團隊提供按需和安全的 SSH、RDP、Kubernetes、數據庫和遠端應用端點的網頁瀏覽器訪問。

![JumpServer 概述](https://github.com/jumpserver/jumpserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## 快速開始

準備一台乾淨的 Linux 伺服器 (64 位, >= 4c8g)

```sh
curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh | bash
```

在瀏覽器中訪問 JumpServer 網址 `http://your-jumpserver-ip/`
- 用戶名: `admin`
- 密碼: `ChangeMe`

[![JumpServer 快速開始](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "JumpServer 快速開始")

## 畫面截圖

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="JumpServer 控制台"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="JumpServer 審計"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="JumpServer 工作台"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="JumpServer 設定"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="JumpServer SSH"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="JumpServer RDP"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="JumpServer K8s"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/jumpserver/jumpserver/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="JumpServer 數據庫"   /></td>
  </tr>
</table>

## 元件

JumpServer 由多個關鍵組件組成，這些組件共同構成 JumpServer 的功能框架，為用戶提供操作管理和安全控制的全面能力。

| 專案                                                  | 狀態                                                                                                                                                                 | 說明                                                                                                 |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/jumpserver/lina)             | <a href="https://github.com/jumpserver/lina/releases"><img alt="Lina 發佈" src="https://img.shields.io/github/release/jumpserver/lina.svg" /></a>                   | JumpServer 網頁 UI                                                                                   |
| [Luna](https://github.com/jumpserver/luna)             | <a href="https://github.com/jumpserver/luna/releases"><img alt="Luna 發佈" src="https://img.shields.io/github/release/jumpserver/luna.svg" /></a>                   | JumpServer 網頁終端                                                                                 |
| [KoKo](https://github.com/jumpserver/koko)             | <a href="https://github.com/jumpserver/koko/releases"><img alt="Koko 發佈" src="https://img.shields.io/github/release/jumpserver/koko.svg" /></a>                   | JumpServer 字元協議連接器                                                                           |
| [Lion](https://github.com/jumpserver/lion)             | <a href="https://github.com/jumpserver/lion/releases"><img alt="Lion 發佈" src="https://img.shields.io/github/release/jumpserver/lion.svg" /></a>                   | JumpServer 圖形協議連接器                                                                           |
| [Chen](https://github.com/jumpserver/chen)             | <a href="https://github.com/jumpserver/chen/releases"><img alt="Chen 發佈" src="https://img.shields.io/github/release/jumpserver/chen.svg" />                       | JumpServer 網頁數據庫                                                                                 |  
| [Razor](https://github.com/jumpserver/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | JumpServer EE RDP 代理連接器                                                                          |
| [Tinker](https://github.com/jumpserver/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | JumpServer EE 遠端應用連接器 (Windows)                                                              |
| [Panda](https://github.com/jumpserver/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | JumpServer EE 遠端應用連接器 (Linux)                                                                |
| [Magnus](https://github.com/jumpserver/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | JumpServer EE 數據庫代理連接器                                                                       |

## 貢獻

歡迎提交 PR 進行貢獻。請參考 [CONTRIBUTING.md][contributing-link] 了解指導方針。

## 安全

JumpServer 是一個關鍵任務產品。請參考基本安全建議進行安裝和部署。如果遇到任何安全相關的問題，請直接聯繫我們：

- 電子郵件: support@fit2cloud.com

## 授權

版權 (c) 2014-2024 飛致雲 FIT2CLOUD 保留所有權利。

遵循 GNU 通用公共許可證第 3 版 (GPLv3) (以下簡稱「許可證」) 授權。除非遵守許可證的規定，否則不得使用本文件。您可以在以下網址獲得許可證的副本

https://www.gnu.org/licenses/gpl-3.0.html

除非適用法律要求或書面同意，根據許可證發佈的軟體是在「按現狀」基礎上發佈的，無任何形式的保證或者條件，無論明示或暗示。請參閱許可證了解管理權限和限制的具體語言。

<!-- JumpServer 官方連結 -->
[docs-link]: https://jumpserver.com/docs
[discord-link]: https://discord.com/invite/W6vYXmAQG2
[contributing-link]: https://github.com/jumpserver/jumpserver/blob/dev/CONTRIBUTING.md

<!-- JumpServer 其他連結-->
[license-link]: https://www.gnu.org/licenses/gpl-3.0.html
[docker-link]: https://hub.docker.com/u/jumpserver
[github-release-link]: https://github.com/jumpserver/jumpserver/releases/latest
[github-stars-link]: https://github.com/jumpserver/jumpserver
[github-issues-link]: https://github.com/jumpserver/jumpserver/issues

<!-- 標誌鏈接-->
[github-release-shield]: https://img.shields.io/github/v/release/jumpserver/jumpserver
[github-stars-shield]: https://img.shields.io/github/stars/jumpserver/jumpserver?color=%231890FF&style=flat-square
[docker-shield]: https://img.shields.io/docker/pulls/jumpserver/jms_all.svg
[license-shield]: https://img.shields.io/github/license/jumpserver/jumpserver
[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb

<!-- 圖片鏈接 -->