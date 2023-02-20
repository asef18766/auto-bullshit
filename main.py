from typing import Dict
from chatgpt import generate_chinese_report
import zipfile
import json

def docx_replace(old_file:str,new_file:str,rep:Dict[str, str]):
    zin = zipfile.ZipFile (old_file, 'r')
    zout = zipfile.ZipFile (new_file, 'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename == 'word/document.xml'):
            res = buffer.decode("utf-8")
            for exp, it in rep.items():
                res = res.replace(exp,it)
            buffer = res.encode("utf-8")
        zout.writestr(item, buffer)
    zout.close()
    zin.close()

def main():
    md_fname = "test.md"
    template_fname = "template.docx"
    res_fname = "report.docx"

    report_txt = generate_chinese_report(md_fname)
    print("==========[AI replied]==========")
    print(report_txt)
    print("================================")
    with open("user_data.json", "r", encoding="utf-8") as fp:
        data:Dict[str, str] = json.loads(fp.read())
        with open(md_fname, "r", encoding="utf-8") as fp2:
            data.update(
            {
                "{md}":fp2.read(),
                "{report}":report_txt
            })
        docx_replace(template_fname, res_fname, data)

if __name__ == "__main__":
    main()