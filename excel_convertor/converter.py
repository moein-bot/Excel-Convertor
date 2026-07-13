"""
converter.py
"""
from pathlib import Path
from .io_handler import IOHandler
from .validator import Validator
from .data_mapper import DataMapper

def convert(template_path,user_path,output_path):
    io=IOHandler(template_path,user_path)
    io.load()
    user_sheet=io.user_sheet()
    template_sheet=io.template_sheet()
    headers=io.headers(user_sheet)
    rows=io.rows(user_sheet)
    Validator.validate(headers,rows)
    mapper=DataMapper()
    mapped=mapper.map_rows(rows)
    template_headers=io.headers(template_sheet)
    for r,row in enumerate(mapped,start=2):
        for k,v in row.items():
            if k in template_headers:
                io.write(template_sheet,r,template_headers[k],v)
    io.save(Path(output_path))
    return Path(output_path)
