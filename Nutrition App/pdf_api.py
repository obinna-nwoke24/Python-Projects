import fpdf
from fpdf import FPDF
import Client
import food_list

pdf_file_extension = '.pdf'


def client_to_pdf(client: Client.Client,
                  preset: bool = True,
                  file_name: str = "file_name"):
    """
    Creates a pdf of the client based on the entries

    :param client: True if you want to use the preset food list, false for user entry
    :param preset:
    :param file_name:
    :return:
    """
    flist = food_list.FoodList(client, preset=preset)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    line_num = 1

    # Coaching heading
    coach_heading(line_num, pdf)

    # heading content
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="{}'s Program".format(client.split_name()[0]), ln=line_num, align='C')

    # body

    # create splits
    nutrition_split = client.nutrition_split.splitlines()
    maintenance_split = nutrition_split[2:6]
    weight_loss_split = nutrition_split[7:11]
    weight_gain_split = nutrition_split[12:]
    all_splits = [maintenance_split, weight_loss_split, weight_gain_split]

    for split in all_splits:
        for line in split:
            pdf.cell(200, 5, txt=line, ln=line_num)
            line_num += 1
        pdf.cell(200, 5, txt="", ln=line_num)

    # create food table
    pdf.cell(200, 5, ln=line_num)
    line_num += 1
    pdf.cell(189, 8, txt="{}'s Nutritional Food List".format(client.split_name()[0]), ln=line_num, border=1, align='C')
    line_num += 1
    pdf.multi_cell(189, 6, txt=flist.carb_list, border=1)
    pdf.multi_cell(189, 6, txt=flist.protein_list, border=1)
    pdf.multi_cell(189, 6, txt=flist.fat_list, border=1)
    # Saving the pdf
    file_name = "{}_program{}".format(client.split_name()[0], pdf_file_extension)
    pdf.output(file_name)


def coach_heading(line_num=1, pdf=fpdf.FPDF()):
    """
    Creates the coach heading for the page
    :param line_num:
    :param pdf:
    :return:
    """
    pdf.cell(10, 5, txt='Coach/Personal Trainer: Jason Nwoke', ln=line_num)
    line_num += 1
    pdf.cell(10, 5, txt='Email: contactjayfit@gmail.com', ln=line_num)
    line_num += 1
    pdf.cell(10, 5, txt='Phone #: +1(347)639-6120', ln=line_num)
    line_num += 1
    pdf.cell(10, 5, txt='Instagram: @fitlife.jay', ln=line_num, link="https://instagram.com/fitlife.jay")
    line_num += 1
