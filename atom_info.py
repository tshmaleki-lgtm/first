from mendeleev import element
import math

def get_atom_info(symbol_or_name):
    try:
        # Get element data using mendeleev
        elem = element(symbol_or_name)
        
        # Calculate number of neutrons (atomic mass rounded to nearest integer minus atomic number)
        atomic_mass = round(float(elem.mass))
        number_of_neutrons = atomic_mass - elem.atomic_number
        
        # Determine if the element is alkaline metal, halogen, or noble gas (as examples)
        group_name = ""
        if elem.group_id in [1, 2]:  # Group 1 and 2 elements (alkali and alkaline earth metals)
            group_name = "فلز قلیایی" if elem.group_id == 1 else "فلز قلیایی خاکی"
        elif elem.group_id == 17:  # Halogens
            group_name = "هالوژن"
        elif elem.group_id == 18:  # Noble gases
            group_name = "گاز نجیب"
        elif elem.group_id in [13, 14, 15, 16]:
            # Check if it forms acidic or basic oxides
            if elem.electronegativity('pauling') > 2.0:
                group_name = "اسیدی"
            else:
                group_name = "قلیایی"
        else:
            group_name = "دیگر"
        
        # Determine common charge (oxidation state) based on group
        common_charge = ""
        if elem.group_id == 1:
            common_charge = "+1"
        elif elem.group_id == 2:
            common_charge = "+2"
        elif elem.group_id == 17:
            common_charge = "-1"
        elif elem.group_id == 16:
            common_charge = "-2"
        elif elem.group_id == 15:
            common_charge = "-3" if elem.period <= 2 else "+3 or -3"
        elif elem.group_id == 14:
            common_charge = "+4 or -4"
        elif elem.group_id == 13:
            common_charge = "+3"
        else:
            common_charge = "متغیر"
        
        # Print the information
        print(f"عنصر: {elem.name}")
        print(f"نماد: {elem.symbol}")
        print(f"عدد اتمی: {elem.atomic_number}")
        print(f"جرم اتمی: {elem.mass}")
        print(f"تعداد الکترون: {elem.atomic_number}")
        print(f"تعداد پروتون: {elem.atomic_number}")
        print(f"تعداد نوترون: {number_of_neutrons}")
        print(f"ساختار الکترونی: {elem.econf}")  # electron configuration
        print(f"قائی یا اسیدی بودن: {group_name}")
        print(f"بار متداول: {common_charge}")
        
    except Exception as e:
        print(f"خطا در یافتن اطلاعات برای '{symbol_or_name}': {str(e)}")
        print("لطفاً نماد یا نام صحیح عنصر را وارد کنید.")

def main():
    # For demonstration purposes, we'll use command line argument or default to hydrogen
    import sys
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("لطفاً نماد یا نام یک عنصر را وارد کنید: ").strip()
    get_atom_info(user_input)

if __name__ == "__main__":
    main()