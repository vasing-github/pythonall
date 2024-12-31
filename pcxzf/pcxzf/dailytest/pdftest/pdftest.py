import PyPDF2

# 打开PDF文件
with open('input.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # 获取PDF文件的页数
    num_pages = len(reader.pages)
    # 读取每一页的内容
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"Page {page_num + 1}:")
        print(text)
