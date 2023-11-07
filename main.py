from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
if __name__ == "__main__":
  with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


    rez_list = []
    result = []
    pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    subst = r'+7(\2)\3-\4-\5 \6\7'


    for i in contacts_list:

      full_name = ' '.join(i[:3]).split(' ')
      result_item = [full_name[0], full_name[1], full_name[2], i[3], i[4], re.sub(pattern, subst, i[5]),i[6]]
      rez_list.append(result_item)

    for i in rez_list:
      name = i[0]
      surname = i[1]
      for i_2 in rez_list:
        name_2 =  i_2[0]
        surname_2 = i_2[1]
        if name == name_2 and surname == surname_2:
          if i[2] == "":
            i[2] = i_2[2]

          if i[3] == "":
            i[3] = i_2[3]

          if i[4] == "":
            i[4] = i_2[4]

          if i[5] == "":
            i[5] = i_2[5]

          if i[6] == "":
            i[6] = i_2[6]

    for i in rez_list:
          if i not in result:
              result.append(i)

  with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    
  ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(result)