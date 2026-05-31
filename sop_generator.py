"""一人公司 SOP 生成器 - 自动生成标准化操作流程"""

def generate_sop(business_type: str, stages: list, output: str = "markdown"):
    """生成 SOP 文档"""
    templates = {
        "内容创作": [
            ("选题策划", "热点监控 → 选题评估 → 确定方向", "日/周"),
            ("素材收集", "关键词搜索 → 资料整理 → 下载归档", "随时"),
            ("内容生产", "大纲 → 初稿 → 修改 → 定稿", "日"),
            ("发布分发", "平台适配 → 定时发布 → 多平台同步", "日"),
            ("数据复盘", "数据采集 → 分析 → 优化迭代", "周"),
        ],
        "电商运营": [
            ("选品调研", "市场分析 → 竞品研究 → 利润测算", "月"),
            ("供应链管理", "供应商筛选 → 样品确认 → 批量采购", "按需"),
            ("店铺运营", "商品上架 → 活动报名 → 客服管理", "日"),
            ("营销推广", "渠道选择 → 预算分配 → 效果追踪", "周"),
            ("售后服务", "退换货处理 → 评价管理 → 客户回访", "日"),
        ],
        "知识付费": [
            ("课程设计", "需求调研 → 大纲规划 → 课程定位", "月"),
            ("内容制作", "逐节录制 → 素材制作 → 校对审核", "周"),
            ("平台入驻", "平台选择 → 资质准备 → 课程上架", "一次性"),
            ("运营推广", "社群预热 → 限时优惠 → 联合推广", "持续"),
            ("学员服务", "社群互动 → 答疑 → 反馈收集", "日"),
        ],
    }

    stages_data = templates.get(business_type, [
        (s, "待完善", "按需") for s in (stages or ["阶段1", "阶段2", "阶段3"])
    ])

    if output == "markdown":
        lines = [
            f"# {business_type} SOP 标准流程\n",
            f"> 生成日期: 自动生成\n",
            "## 流程总览\n",
            "| 阶段 | 核心动作 | 频率 | 输出物 |",
            "|------|----------|------|--------|",
        ]
        for name, actions, freq in stages_data:
            lines.append(f"| {name} | {actions} | {freq} | 待定 |")
        lines.append(f"\n## 检查清单\n")
        for name, actions, freq in stages_data:
            lines.append(f"- [ ] {name}: {actions}")
            for action in actions.split(" → "):
                lines.append(f"  - [ ] {action.strip()}")
        return "\n".join(lines)
    return stages_data


if __name__ == "__main__":
    print(generate_sop("内容创作"))
