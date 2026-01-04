import os

# --- 配置 ---
SOURCE_DIR = "demo"      # 你的 demo 目录路径
OUTPUT_FILE = "index.md" # 生成的 Markdown 文件名

def generate_index():
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: 找不到目录 '{SOURCE_DIR}'")
        return

    # 1. 枚举所有子目录 (Enumerate all dirs)
    subdirs = [d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))]
    
    # 基础排序（按字母），方便你后续手动调整
    subdirs.sort()

    # 2. 生成 Markdown 内容
    md_content = "# 📂 项目导航索引\n\n"
    md_content += "> 💡 你可以在 VS Code 中选中行，使用 `Alt + Up/Down` 手动调整顺序。\n\n---\n\n"

    for folder in subdirs:
        # 自动识别入口文件（优先 run.py, 其次 app.py）
        entry_file = ""
        for f in ["run.py", "app.py"]:
            if os.path.exists(os.path.join(SOURCE_DIR, folder, f)):
                entry_file = f"{SOURCE_DIR}/{folder}/{f}"
                break
        
        # 格式化显示名称 (hello_world -> Hello World)
        display_name = folder.replace("_", " ").title()
        
        if entry_file:
            md_content += f"- [ ] [{display_name}]({entry_file})\n"
        else:
            md_content += f"- [ ] {display_name} *(未找到入口文件)*\n"

    # 3. 写入文件
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"✅ 已在当前目录生成 {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_index()