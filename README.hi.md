<div align="center">
  <a name="readme-top"></a>
  <a href="https://jumpserver.org/index-en.html"><img src="https://download.jumpserver.org/images/jumpserver-logo.svg" alt="JumpServer" width="300" /></a>
  
## An open-source PAM tool (Bastion Host)
## Test Language
## Test Language2

[![][license-shield]][license-link][![][discord-shield]][discord-link][![][docker-shield]][docker-link][![][github-release-shield]][github-release-link][![][github-stars-shield]][github-stars-link]

**अंग्रेज़ी**·[सरलीकृत चीनी](./README.zh-CN.md)

</div>
<br/>

## जंपसर्वर क्या है?

जंपसर्वर एक ओपन-सोर्स प्रिविलेज्ड एक्सेस मैनेजमेंट (PAM) टूल है जो DevOps और IT टीमों को वेब ब्राउज़र के माध्यम से SSH, RDP, Kubernetes, डेटाबेस और रिमोटऐप एंडपॉइंट्स तक ऑन-डिमांड और सुरक्षित पहुंच प्रदान करता है।

![JumpServer Overview](https://github.com/jumpserver/jumpserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## त्वरित शुरुआत

एक साफ़ Linux सर्वर तैयार करें (64 बिट, >=4c8g)

```sh
curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh | bash
```

अपने ब्राउज़र में जंपसर्वर तक पहुंचें`http://your-jumpserver-ip/`

-   उपयोगकर्ता नाम:`admin`
-   पासवर्ड:`ChangeMe`

[![JumpServer Quickstart](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "JumpServer Quickstart")

## स्क्रीनशॉट

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

## अवयव

जंपसर्वर में कई प्रमुख घटक होते हैं, जो सामूहिक रूप से जंपसर्वर के कार्यात्मक ढांचे का निर्माण करते हैं, जो उपयोगकर्ताओं को संचालन प्रबंधन और सुरक्षा नियंत्रण के लिए व्यापक क्षमताएं प्रदान करते हैं।

| परियोजना                                             | स्थिति                                                                                                                                               | विवरण                                         |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [लीना](https://github.com/jumpserver/lina)           | <a href="https://github.com/jumpserver/lina/releases"><img alt="Lina release" src="https://img.shields.io/github/release/jumpserver/lina.svg" /></a> | जंपसर्वर वेब यूआई                             |
| [अफ़सर](https://github.com/jumpserver/luna)          | <a href="https://github.com/jumpserver/luna/releases"><img alt="Luna release" src="https://img.shields.io/github/release/jumpserver/luna.svg" /></a> | जंपसर्वर वेब टर्मिनल                          |
| [आकार](https://github.com/jumpserver/koko)           | <a href="https://github.com/jumpserver/koko/releases"><img alt="Koko release" src="https://img.shields.io/github/release/jumpserver/koko.svg" /></a> | जंपसर्वर कैरेक्टर प्रोटोकॉल कनेक्टर           |
| [शेर](https://github.com/jumpserver/lion)            | <a href="https://github.com/jumpserver/lion/releases"><img alt="Lion release" src="https://img.shields.io/github/release/jumpserver/lion.svg" /></a> | जंपसर्वर ग्राफिकल प्रोटोकॉल कनेक्टर           |
| [चेन](https://github.com/jumpserver/chen)            | <a href="https://github.com/jumpserver/chen/releases"><img alt="Chen release" src="https://img.shields.io/github/release/jumpserver/chen.svg" />     | जंपसर्वर वेब डीबी                             |
| \[रेजर](https&#x3A;//github.com/jumpserver/razor)    | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                            | जंपसर्वर ईई आरडीपी प्रॉक्सी कनेक्टर           |
| \[टिंकर](https&#x3A;//github.com/jumpserver/tinker)  | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                          | जंपसर्वर ईई रिमोट एप्लिकेशन कनेक्टर (विंडोज़) |
| \[पांडा](https&#x3A;//github.com/jumpserver/Panda)   | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                           | जम्पसर्वर ईई रिमोट एप्लीकेशन कनेक्टर (लिनक्स) |
| \[मैग्नस](https&#x3A;//github.com/jumpserver/magnus) | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                          | जंपसर्वर ईई डेटाबेस प्रॉक्सी कनेक्टर          |

## योगदान

योगदान देने के लिए पीआर सबमिट करने के लिए आपका स्वागत है। दिशानिर्देशों के लिए कृपया \[CONTRIBUTING.md]\[contributing-link] देखें।

## सुरक्षा

JumpServer is a mission critical product. Please refer to the Basic Security Recommendations for installation and deployment. If you encounter any security-related issues, please contact us directly:

-   ईमेल: support@fit2cloud.com

## लाइसेंस

कॉपीराइट (सी) 2014-2024 FIT2CLOUD, सर्वाधिकार सुरक्षित।

जीएनयू जनरल पब्लिक लाइसेंस संस्करण 3 (जीपीएलवी3) ("लाइसेंस") के तहत लाइसेंस प्राप्त; आप लाइसेंस के अनुपालन के अलावा इस फ़ाइल का उपयोग नहीं कर सकते। आप लाइसेंस की एक प्रति यहां प्राप्त कर सकते हैं

https&#x3A;//www.gnu.org/licenses/gpl-3.0.html

जब तक लागू कानून द्वारा आवश्यक न हो या लिखित रूप से सहमति न हो, लाइसेंस के तहत वितरित सॉफ्टवेयर "जैसा है" के आधार पर वितरित किया जाता है, किसी भी प्रकार की व्यक्त या निहित वारंटी या शर्तों के बिना। लाइसेंस के अंतर्गत अनुमतियों और सीमाओं को नियंत्रित करने वाली विशिष्ट भाषा के लिए लाइसेंस देखें।

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
