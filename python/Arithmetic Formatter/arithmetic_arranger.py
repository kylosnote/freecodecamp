def arithmetic_arranger(problems,answer=False):
  inputs =problems
  if len(inputs) > 5:
    return "Error: Too many problems."

  first_line, second_line, third_line,answer_line = "","","",""
  for each in inputs:
    if each.find("+") < 0 and each.find("-") < 0:
      return "Error: Operator must be '+' or '-'."

    check_digit = each.replace("+","")
    check_digit = check_digit.replace("-","")
    check_digit = check_digit.replace(" ","")

    if not check_digit.isdigit():
        return "Error: Numbers must only contain digits."


    if each.find("+") > 0:

        each_list = each.split("+")
        each_list_int = [int(x.strip()) for x in each_list]
        first = each_list[0].strip()
        second = each_list[1].strip()
        max_length = len(str(max(each_list_int)))

        if not (check_number_length(first) and check_number_length(second)):
            return "Error: Numbers cannot be more than four digits."


        each_total = int(first) + int(second)

        second = ("+ "+second.rjust(max_length)+"    ")
        first_line += first.rjust(max_length+2)+"    "
        second_line +=second


        third_line += "-"*(max_length+2)+"    "
        answer_line += (str(each_total)).rjust(max_length+2)+"    "

        #print(each," = ",each_total)

    if each.find("-") > 0:
        #print(each.find("-"))
        #print(each,"minus")
        each_list = each.split("-")
        each_list_int = [int(x.strip()) for x in each_list]
        first = each_list[0].strip()
        second = each_list[1].strip()
        max_length = len(str(max(each_list_int)))

        if not (check_number_length(first) and check_number_length(second)):
            return "Error: Numbers cannot be more than four digits."

        each_total = int(first) - int(second)

        second = ("- "+second.rjust(max_length)+"    ")
        first_line += first.rjust(max_length+2)+"    "
        second_line +=second


        third_line += "-"*(max_length+2)+"    "
        answer_line += (str(each_total)).rjust(max_length+2)+"    "
  if answer:
      return first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip() + "\n" + answer_line.rstrip()
  else:
      return first_line.rstrip()+"\n"+second_line.rstrip()+"\n"+third_line.rstrip()


def check_number_length(number):
    if len(number) < 5:
        return True
    else:
        return False