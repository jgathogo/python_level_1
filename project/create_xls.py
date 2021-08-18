import os
import sys
import docx
import xlsxwriter

"""
- Import Questionnaire from MS Word document
- Extract text from each row, return as dictionary
    - If text contains Section text, this is begin_group type
    - Column 0 - if text 'Q' this is a question. Strangely, docx is not importing the question numbers?
        - Autonumber each question. May not match the numbering in the questionnaire
    - Column 1 - this is question label
    - Column 2(quest_choices) - If not empty, assume this is a select_one or select_multiple question
    - Column 3 - if not empty, these are the choice values of the question
- Survey dictionary - create 'survey' and 'choices' sheets from this dictionary
    - Survey sheet - has the following fields
        - type - if quest_choices not empty, type should be select_one. Otherwise, integer or text. 
        Each select_one needs a list_name
        - name - unique name for each question. For now add Q to question number e.g., Q1
        - label - question_label
    - Choices sheet - has the following fields:
        - list_name - this is repeating field depending on the number of choice values
        - name - unique number/text for each choice value within the list_name
        - label - quest_choices
        
"""


def main():
    doc = docx.Document("data/survey.docx")
    print(len(doc.tables))

    # question_num = []
    # question_label = []
    # question_choices = []
    survey = {}
    num = 1

    for table in doc.tables:
        for row in table.rows:
            if row.cells[0].text == 'Q':
                quest_id = num
                quest_label = row.cells[1].text
                quest_choices = row.cells[2].text.split('\n')
                quest_choice_labels = row.cells[3].text.split('\n')
                survey[quest_id] = quest_label, quest_choices, quest_choice_labels
                num += 1
    print(survey)
    # Survey sheet
    survey_sheet = {}
    choices_sheet = []
    for quest_id, quest in survey.items():
        print(quest_id, quest)
        quest_label = quest[0]
        if len(quest[1]) <= 1:
            quest_type = 'text'
        else:
            list_name = 'Q' + str(quest_id)
            list_num = quest[2]
            # Choices sheet
            choices = quest[1]
            quest_type = 'select_one ' + list_name
            for i in range(len(choices)):
                choices_sheet.append((list_name, choices[i], list_num[i]))
        survey_sheet[quest_id] = quest_type, quest_label
    print(survey_sheet)
    print(choices_sheet)

    # Write to Excel Sheet
    wb = xlsxwriter.Workbook('data/survey.xlsx')
    survey_ws = wb.add_worksheet('survey')
    choices_ws = wb.add_worksheet('choices')

    row = 0
    col = 0

    survey_header = ['type', 'name', 'label', 'relevant']

    for header in survey_header:
        survey_ws.write_string(row, col, header)
        col += 1
    row, col = 1, 0

    for unique_id, quest in survey_sheet.items():
        name_text = 'Q' + str(unique_id)
        type_text = quest[0]
        label_text = name_text + '- ' + quest[1]
        survey_ws.write_string(row, col, type_text)
        col += 1
        survey_ws.write_string(row, col, name_text)
        col += 1
        survey_ws.write_string(row, col, label_text)
        col = 0
        row += 1

    wb.close()

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
