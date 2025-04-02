
def test_chrome_cpu_value(dynamic_table_page):
    cpu_value_from_table = dynamic_table_page.get_chrome_cpu_value()
    cpu_value_from_label = dynamic_table_page.get_chrome_cpu_label()
    assert cpu_value_from_table == cpu_value_from_label, f"Expected {cpu_value_from_label}, but got {cpu_value_from_table}"
