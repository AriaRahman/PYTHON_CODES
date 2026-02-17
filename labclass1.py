print("hello awaheo")
"""
DOCSTTING for this project
this is an application for calculating  & storing student results 
this will run in the CLI
if possible will save it in .csv file

"""

def print_menu() -> None:
    print("CLI APPLICATION:")
    print("1. add student result + CALCULATE results")
    print("2. list all student result")
    print("3. search student by ID")
    print("4. Delete student by ID")
    print("5. save  .csv file")
    print("6. exit")

def main() -> None:
    #while choice != "6":
    while True:
      print_menu()
      choice: str = input("enter num as choice (1 to 6):").strip()
#match catch is only available after python 3.10

      match choice:
        case "1" :
          print("add student+ calculate results")
          pass
        case "2" :
          print("list out students")
          pass 
        case "3" :
          print("search student")
          pass
        case "4" :
          print("delete student")
          pass
        case "5" :
          print("saving .csv")
          pass
        case "6" :
          print("exit")
          break 
        case _:
          print("invalid")
               
      

if __name__ == "__main__":
    main()