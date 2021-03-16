from add_gg_form import AddGgForm
from bs4_data import DataInZillow
import time

if __name__ == "__main__":
    data = DataInZillow()
    add_to_gg = AddGgForm()
    data_dict = data.dict_zillow
    for i in data_dict:
        time.sleep(1.5)
        address = data_dict[i]['address']
        price = data_dict[i]['price']
        link = data_dict[i]['link']
        add_to_gg.add_form(address=address, price=price, link=link)
    add_to_gg.driver.quit()