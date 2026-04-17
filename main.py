#!/usr/bin/env python3
"""YOTIME 悠享家 MCP Skill — 让 AI 读懂悠享家"""

import json
from mcp.server.fastmcp import FastMCP
from data import BRAND, STORES, PRODUCTS, PROMOTIONS

mcp = FastMCP("yotime")


@mcp.tool()
def get_brand_info() -> str:
    """获取悠享家品牌介绍、联系热线和客服微信"""
    return json.dumps(BRAND, ensure_ascii=False, indent=2)


@mcp.tool()
def list_stores(district: str = "") -> str:
    """
    查询悠享家门店列表。
    district: 可选，按区域筛选，支持"鹿城区"、"瓯海区"、"龙湾区"，不填返回全部。
    """
    stores = STORES
    if district:
        stores = [s for s in stores if district in s["district"]]
    return json.dumps(stores, ensure_ascii=False, indent=2)


@mcp.tool()
def find_store(keyword: str) -> str:
    """
    按关键词搜索门店（门店名称或地址均可匹配）。
    keyword: 搜索关键词，例如"印象城"、"时代"、"学院路"。
    """
    results = [
        s for s in STORES
        if keyword in s["name"] or keyword in s["address"]
    ]
    if not results:
        return json.dumps({"message": f"未找到包含'{keyword}'的门店"}, ensure_ascii=False)
    return json.dumps(results, ensure_ascii=False, indent=2)


@mcp.tool()
def get_products() -> str:
    """获取悠享家主推产品列表，含名称、描述和产品图片链接"""
    return json.dumps(PRODUCTS, ensure_ascii=False, indent=2)


@mcp.tool()
def get_delivery_links(store_name: str = "") -> str:
    """
    获取门店外卖平台链接（美团/饿了么）。
    store_name: 可选，指定门店名称；不填则返回所有已配置外卖链接的门店。
    """
    if store_name:
        matches = [s for s in STORES if store_name in s["name"]]
        if not matches:
            return json.dumps({"message": f"未找到门店'{store_name}'"}, ensure_ascii=False)
        store = matches[0]
        if not store["delivery"]:
            return json.dumps(
                {"store": store["name"], "message": "该门店外卖链接暂未收录，请致电或加微信咨询",
                 "phone": store["phone"], "wechat": store["wechat"]},
                ensure_ascii=False
            )
        return json.dumps({"store": store["name"], **store["delivery"]}, ensure_ascii=False, indent=2)

    result = [
        {"store": s["name"], **s["delivery"]}
        for s in STORES if s["delivery"]
    ]
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def get_contact() -> str:
    """获取悠享家客服联系方式，包括全国热线和官方客服企微号"""
    return json.dumps({
        "hotline": BRAND["hotline"],
        "wechat_service": BRAND["wechat_service"],
        "tip": "添加企微客服号 yotime-wm1，可咨询产品、定制蛋糕及门店信息",
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def get_new_products() -> str:
    """获取悠享家最新上架产品"""
    new_items = [p for p in PRODUCTS if p.get("is_new")]
    return json.dumps(new_items, ensure_ascii=False, indent=2)


@mcp.tool()
def get_promotions() -> str:
    """获取悠享家当前优惠活动（抖音团购、美团、门店活动等）"""
    if not PROMOTIONS:
        return json.dumps({"message": "暂无进行中的优惠活动，请关注官方客服企微号 yotime-wm1 获取最新活动信息"}, ensure_ascii=False)
    return json.dumps(PROMOTIONS, ensure_ascii=False, indent=2)


@mcp.tool()
def get_wifi() -> str:
    """获取悠享家门店 Wi-Fi 账号和密码"""
    wifi = BRAND["wifi"]
    return json.dumps({
        "wifi_name": wifi["name"],
        "wifi_password": wifi["password"],
        "tip": "全部门店通用，进店即可连接",
    }, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    mcp.run()
