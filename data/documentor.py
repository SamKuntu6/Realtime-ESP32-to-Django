from docx import Document
from docx.shared import Inches

def word_creator(checker, time1, time2, state, readings):
    document = Document()

    hedin = document.add_heading(f'XYZ Bridge Structural Health Monitoring {checker} Report', 0)
    hedin.bold = True

    paragraph1 = document.add_paragraph(f'Tabulation Time: {time1}')
    paragraph2 = document.add_paragraph(f'Analysis Time：{time2}')

    document.add_heading(' 1.System Self-Assessment', level=1)

    records = (
        ('', '', 'Wind', 'UAN', '0', '0%', 'Very Poor'),
        (1, 'Environment', 'Temp and Humid', 'THS', '0', '0%', 'Very Poor'),
        ('', '', 'Temperature', 'DTS', '0', '0%', 'Very Poor'),
        (2, 'Load', 'Earthquake', 'VIB', '0', '0%', 'Very Poor'),
        ('', '', 'Gider Deflection', 'DEF', '1', '100%', 'Excellent'),
        (3, 'Deformation', 'Pier and Abutt. Tilt', 'TIL', '0', '0%', 'Very Poor'),
        ('', '', 'Support Disp', 'MDS', '0', '0%', 'Very Poor'),
        (4, 'Response', 'Cable Force', 'MFS', '0', '0%', 'Very Poor'),
        ('', '', 'Concrete Strain', 'VWS', '0', '0%', 'Very Poor'),
        (5, 'Dynamic', 'Vibration', 'VIB', '0', '0%', 'Very Poor')
    )

    table = document.add_table(rows=1, cols=7)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'No.'
    hdr_cells[1].text = 'Category'
    hdr_cells[2].text = 'Monitoring'
    hdr_cells[3].text = 'Sensor Type'
    hdr_cells[4].text = 'Num'
    hdr_cells[5].text = 'Integrity'
    hdr_cells[6].text = 'Conclusion'
    for num, cat, descr, sen, nu, integ, conc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(num)
        row_cells[1].text = cat
        row_cells[2].text = descr
        row_cells[3].text = sen
        row_cells[4].text = nu
        row_cells[5].text = integ
        row_cells[6].text = conc

    paragraph3 = document.add_paragraph('Monitoring Conclusions：')
    paragraph4 = document.add_paragraph(
        f'Today the health monitoring system for XYZ Bridge works: ', style='List Bullet')
    paragraph4.add_run(f'{state}').italic = True
    document.add_paragraph('Wind Scale: ', style='List Bullet')
    document.add_paragraph('Environment temperature and humidity：', style='List Bullet')
    document.add_paragraph('Pylon inside temperature and humidity：', style='List Bullet')
    document.add_paragraph('Girder inside temperature and humidity：', style='List Bullet')
    document.add_paragraph('Stayed-cable inside temperature and humidity：', style='List Bullet')
    document.add_paragraph('Cable force deviation：', style='List Bullet')
    document.add_paragraph('Stress：', style='List Bullet')

    # document.add_page_break()

    heading2 = document.add_heading(' 2.General Monitoring Conclusions.', level=1)
    if readings:
        document.add_paragraph('All of the measuring displacement have not exceed the threshold and the safety of bridge meet the requirements. ', style='List Bullet')
        document.add_paragraph('The correlation of sensors is good and the measuring data is accurate and effective.', style='List Bullet')
    else:
        document.add_paragraph('The measured displacement have exceed the threshold and the safety requirements of the bridge have is poor. ', style='List Bullet')
        document.add_paragraph('The correlation of sensors is good and the measuring data is accurate and effective.', style='List Bullet')

    heading3 = document.add_heading(' 3.Monitoring data analysis.', level=1)
    heading4 = document.add_heading('   3.1 Data analysis of wind', level=2)
    heading5 = document.add_heading('   3.2 Data analysis of temperature and humidity', level=2)
    heading6 = document.add_heading('   3.3 Data analysis of earthquake', level=2)
    heading7 = document.add_heading('   3.4 Data analysis of Deck deflection', level=2)

    if readings:
        document.add_paragraph('All of the measuring displacement have not exceed the threshold and the safety of bridge meet the requirements. (threshold = 50 mm)', style='List Bullet')
    else:
        document.add_paragraph('Traffic is larger than the capacity of the bridge (when more than five readings are above the threshold)', style='List Bullet')

    heading8 = document.add_heading('   3.5 Data analysis of pier inclination', level=2)
    heading9 = document.add_heading('   3.6 Data analysis of girder displacement in longitudinal', level=2)
    heading10 = document.add_heading('   3.7 Data analysis of concrete stress', level=2)
    heading11 = document.add_heading('   3.8 Data analysis of vibration', level=2)

    # document.save('doin.docx')
    return document