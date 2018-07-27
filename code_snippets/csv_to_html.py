def csv2html_file(csv_file, delimiter=None, html_file=None, header=None):
    html_file = html_file or r"C:\Data\Development\etl_batch\bin\binPython\locals\md_report.html"
    delimiter = delimiter or ','
    with open(csv_file) as csv_in:
        with open(html_file, mode='w') as html_out:
            row = "<tr>{0}</tr>"
            header = header or "<tr>" \
                               "<td>DB COLUMN</td>" \
                               "<td>DB VALUE</td>" \
                               "<td>RULE STATUS</td>" \
                               "</tr>"
            for line in csv_in:
                line = line.strip()
                print(line)
                if line and line.startswith('['):
                    # table name encountered
                    html_out.write("%s<br><table border=1>" % line)
                    html_out.write(header)
                elif line and len(line.split(delimiter)) > 2:
                    # table row encountered
                    line = "<td>" + line.replace(delimiter,
                                                 "</td><td>") + "</td>"
                    html_out.write(row.format(line))
                else:
                    html_out.write("%s </table><br><br>" % line)
    return html_file
