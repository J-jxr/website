import os
import fileinput

# 需要处理的文件列表
files_to_process = [
    "docs/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.10/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.11/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.12/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.13/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.14/reference/karmadactl/karmadactl-commands/karmadactl_index.md",
    "versioned_docs/version-v1.14/userguide/service/working-with-eriecanal.md",
    "versioned_docs/version-v1.15/userguide/service/working-with-eriecanal.md"
]

def fix_variables_in_file(file_path):
    if not os.path.exists(file_path):
        print(f"警告: 文件不存在 - {file_path}")
        return
    
    # 直接替换内容（原地修改）
    with fileinput.FileInput(file_path, inplace=True, encoding='utf-8') as file:
        for line in file:
            line = line.replace("<fieldName>", "`<fieldName>`")
            line = line.replace("<member_cluster_entry_ip>", "`<member_cluster_entry_ip>`")
            print(line, end='')
    
    print(f"已处理: {file_path}")

if __name__ == "__main__":
    print("开始处理MDX文件...")
    for file_path in files_to_process:
        fix_variables_in_file(file_path)
    print("处理完成!")
    