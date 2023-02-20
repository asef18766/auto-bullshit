from typing import Dict
import zipfile

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
docx_replace("template.docx", "report.docx",
{
    "{id}":"r11921a06",
    "{name}":"陳兆閔",
    "{group}":"資安"
    "{m}":"2",
    "{d}":"20",
    "{topic}":"meow",
    "{md}":"some md",
    "{report}":"some report"
})