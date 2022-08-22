testdata_searchbox = [
    ("Drukarka", "Gdańsk", "Drukarka w Gdańsk"),
    ("Aparat", "Toruń", "Aparat w Toruń")
]

testdata_advert_form_fields = [{
    "title": "Smartwach Samsung Galaxy 3 - Nowy, gwarancja",
    "description": ("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    "Mauris gravida quam eget ligula erat curae."),
    "price": "3000",  # Might be also "free", "exchange"
    "negotiable": False,
    "advert_type": "private",  # Might be also "business"
    "item_condition": 1,  # 1-Używane, 2-Nowe, 3-Uszkodzone, 4-Outlet
    "auto_reneval": False,
    "location": "Gdańsk, Przymorze Małe"
}]
