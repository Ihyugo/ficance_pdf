python make_screenshot.py
copy /Y convert_to_pdf.py combine.py
move /Y combine.py png
cd png
python combine.py