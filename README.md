# 墨尔本人行道人流监测系统

> Mohr's traffic monitoring project — Melbourne pedestrian volume visualization

## 项目简介

本项目使用 Python 对墨尔本市中心多个监测点的人行道人流数据进行读取、处理和可视化。通过
`folium` 地图库生成带时间轴的热力图动画,直观展示人流分布随时段的变化趋势。

## 功能特点

- 多源 CSV 数据融合(2009-2012 年逐小时数据)
- 18 个监测站点实时人流密度展示
- 可播放的时序热力图动画
- 交互式地图浏览(缩放、标记点弹出)
- 离线资源加速(foliumacc 模块)

## 环境要求

- Python 3.8+
- folium >= 0.14

## 快速开始

### 1. 创建虚拟环境(首次使用)

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 2. 运行

```bash
python main.py
```

程序会自动读取所有 CSV 数据,生成 `墨尔本人行道人流情况.html` 并在浏览器中打开。

## 文件说明

| 文件 | 说明 |
|------|------|
| `main.py` | 主程序入口,包含数据读取、地图生成逻辑 |
| `foliumacc.py` | Folium 资源加速模块,替换 CDN 地址以加快加载 |
| `requirements.txt` | Python 依赖列表 |
| `2009_05-2012_03-HOUR.CSV` ~ `2012_09-HOUR.CSV` | 原始人流数据文件 |
| `jquery.min.js` | jQuery 库(本地加速) |
| `leaflet-heat.js` | Leaflet 热力图插件 |
| `墨尔本人行道人流情况.html` | 生成的可视化地图文件 |

## 监测站点

| 站点 | 坐标 |
|------|------|
| Town Hall West | [-37.8152, 144.9660] |
| Collins Place South | [-37.8186, 144.9553] |
| Australia on Collins | [-37.8182, 144.9566] |
| Bourke Street Mall South | [-37.8149, 144.9612] |
| Bourke Street Mall North | [-37.8132, 144.9666] |
| Melbourne Central | [-37.8101, 144.9627] |
| Flagstaff Station | [-37.8118, 144.9564] |
| State Library | [-37.8094, 144.9652] |
| Collins Place North | [-37.8088, 144.9724] |
| Southern Cross Station | [-37.8182, 144.9524] |
| Victoria Point | [-37.8047, 144.9452] |
| New Quay | [-37.8137, 144.9427] |
| Waterfront City | [-37.8139, 144.9396] |
| Webb Bridge | [-37.8231, 144.9473] |
| Birrarung Marr | [-37.8179, 144.9744] |
| Princes Bridge | [-37.8190, 144.9682] |
| Flinders St Station Underpass | [-37.8181, 144.9670] |
| Sandridge Bridge | [-37.8202, 144.9629] |

## 技术栈

- **Python** — 数据处理
- **folium** — 地图可视化
- **Leaflet / HeatMapWithTime** — 前端地图引擎和热力图动画
- **CSV** — 数据存储

## 数据集

数据来源于墨尔本市政府人行道监测系统,涵盖 2009 年 5 月至 2012 年 9 月的小时级人流计数。

## 作者

JachynRen
