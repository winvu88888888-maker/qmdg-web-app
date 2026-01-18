from pypdf import PdfReader
import json
import os

pdfs = [
    "Đạo Gia Âm Bàn-KMĐG-VƯƠNG PHƯỢNG LÂN (1).pdf",
    "Kỳ môn độn giáp ( lưu bá ôn ).pdf",
    "Kỳ môn độn giáp phần 1 ( lưu bá ôn ).pdf",
    "Kỳ môn độn giáp.pdf"
]

inspection_results = {}

for pdf_path in pdfs:
    if not os.path.exists(pdf_path):
        inspection_results[pdf_path] = "File not found"
        continue
    
    try:
        reader = PdfReader(pdf_path)
        info = {
            "pages": len(reader.pages),
            "metadata": dict(reader.metadata) if reader.metadata else {},
            "sample_content": []
        }
        
        # Take first 10 pages or less
        for i in range(min(10, len(reader.pages))):
            text = reader.pages[i].extract_text()
            if text:
                info["sample_content"].append({
                    "page": i + 1,
                    "text": text[:1000] # Limit per page
                })
        
        inspection_results[pdf_path] = info
    except Exception as e:
        inspection_results[pdf_path] = f"Error: {str(e)}"

with open("pdf_inspection.json", "w", encoding="utf-8") as f:
    json.dump(inspection_results, f, ensure_ascii=False, indent=2)

print("Inspection completed. Results saved to pdf_inspection.json")
