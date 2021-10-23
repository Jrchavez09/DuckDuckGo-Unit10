
import requests
import pytest

DUCKDUCKGO_API  = "https://api.duckduckgo.com"
response = requests.get(DUCKDUCKGO_API + "/?q=presidents+of+the+united+states&format=json")
response_dt = response.json()

""" Presidents of the United States"""
def test_ddg0():
    assert "Presidents of the United States" in response_dt["Heading"]

"""Abraham Lincoln 16th U.S. President"""
def test_ddg1():
    assert "Lincoln" in response_dt["RelatedTopics"][0]["Text"]

"""Andrew Jackson 7th U.S. President"""
def test_ddg2():
    assert "Jackson" in response_dt["RelatedTopics"][2]["Text"]

"""Andrew Johnson 17th U.S. President"""
def test_ddg3():
    assert "Johnson" in response_dt["RelatedTopics"][3]["Text"]

"""Barack Obama 44th U.S. President"""
def test_ddg4():
    assert "Obama" in response_dt["RelatedTopics"][4]["Text"]

"""William Henry Harrison 9th U.S. President"""
"""Benjamin Harrison 23th U.S. President"""
def test_ddg5():
    assert "Harrison" in response_dt["RelatedTopics"][5]["Text"]
    assert "Harrison" in response_dt["RelatedTopics"][55]["Text"]

"""Martin Van Buren 8th U.S. President"""
def test_ddg6():
    assert "Van Buren" in response_dt["RelatedTopics"][6]["Text"]

"""William J. Clinton 42th U.S. President"""
def test_ddg7():
    assert "Clinton" in response_dt["RelatedTopics"][7]["Text"]

"""Calvin Coolidge 30th U.S. President"""
def test_ddg8():
    assert "Coolidge" in response_dt["RelatedTopics"][8]["Text"]

"""Chester A. Arthur 21th U.S. President"""
def test_ddg9():
    assert "Arthur" in response_dt["RelatedTopics"][9]["Text"]

"""Donald Trump 45th U.S. President"""
def test_ddg10():
    assert "Trump" in response_dt["RelatedTopics"][12]["Text"]

"""Dwight D. Eisenhower 34th U.S. President"""
def test_ddg11():
    assert "Eisenhower" in response_dt["RelatedTopics"][13]["Text"]

"""Franklin D. Roosevel 32th U.S. Presidentt"""
def test_ddg12():
    assert "Roosevelt" in response_dt["RelatedTopics"][14]["Text"]

"""Franklin Pierce 14th U.S. President"""
def test_ddg13():
    assert "Pierce" in response_dt["RelatedTopics"][15]["Text"]

"""George H. W. Bush 41th U.S. President"""
"""George W. Bush 43th U.S. President"""
def test_ddg14():
    assert "Walker Bush" in response_dt["RelatedTopics"][17]["Text"]
    assert "Walker Bush" in response_dt["RelatedTopics"][19]["Text"]

"""George Washington 1st U.S. President"""
def test_ddg15():
    assert "Washington" in response_dt["RelatedTopics"][18]["Text"]

"""Gerald R. Ford 38th U.S. President"""
def test_ddg16():
    assert "Ford" in response_dt["RelatedTopics"][20]["Text"]

"""Grover Cleveland 24th U.S. President"""
def test_ddg17():
    assert "Cleveland" in response_dt["RelatedTopics"][21]["Text"]

"""Harry S. Truman 33rd U.S. President"""
def test_ddg18():
    assert "Truman" in response_dt["RelatedTopics"][22]["Text"]

"""Herbert Hoover 31st U.S. President"""
def test_ddg19():
    assert "Hoover" in response_dt["RelatedTopics"][23]["Text"]

"""James Garfield 20th U.S. President"""
def test_ddg20():
    assert "Garfield" in response_dt["RelatedTopics"][26]["Text"]

"""James Buchanan 15th U.S. President"""
def test_ddg21():
    assert "Buchanan" in response_dt["RelatedTopics"][27]["Text"]

"""James K. Polk 11th U.S. President"""
def test_ddg22():
    assert "Polk" in response_dt["RelatedTopics"][28]["Text"]

"""James Madison 4th U.S. President"""
def test_ddg22():
    assert "Madison" in response_dt["RelatedTopics"][29]["Text"]

"""James Monroe 5th U.S. President"""
def test_ddg24():
    assert "Monroe" in response_dt["RelatedTopics"][30]["Text"]

"""James Carter 39th U.S. President"""
def test_ddg25():
    assert "Carter" in response_dt["RelatedTopics"][31]["Text"]

"""Joseph R. Biden Jr. 46th U.S. President"""
def test_ddg26():
    assert "Biden" in response_dt["RelatedTopics"][32]["Text"]

"""John Adams 2n U.S. President"""
"""John Quincy Adams 6th U.S. President"""
def test_ddg27():
    assert "Adams" in response_dt["RelatedTopics"][33]["Text"]
    assert "Adams" in response_dt["RelatedTopics"][35]["Text"]

"""Jonh f. Kennedy 35th U.S. President"""
def test_ddg28():
    assert "Kennedy" in response_dt["RelatedTopics"][34]["Text"]

"""John Tyler 10th U.S. President"""
def test_ddg29():
    assert "Tyler" in response_dt["RelatedTopics"][36]["Text"]

"""Lyndon B. Johnson 36th U.S. President"""
def test_ddg30():
    assert "Johnson" in response_dt["RelatedTopics"][39]["Text"]

"""Millard Fillmore 13th U.S. President"""
def test_ddg31():
    assert "Fillmore" in response_dt["RelatedTopics"][42]["Text"]

"""Richard M. Nixon 37th U.S. President"""
def test_ddg32():
    assert "Nixon" in response_dt["RelatedTopics"][44]["Text"]

"""Ronald Reagan 40th U.S. President"""
def test_ddg33():
    assert "Reagan" in response_dt["RelatedTopics"][45]["Text"]

"""Rutherford B. Hayes 19th U.S. President"""
def test_ddg34():
    assert "Hayes" in response_dt["RelatedTopics"][46]["Text"]

"""Theodore Roosevelt 26th U.S. President"""
def test_ddg35():
    assert "Roosevelt Jr." in response_dt["RelatedTopics"][49]["Text"]

"""Thomas Jefferson 3rd U.S. President"""
def test_ddg36():
    assert "Jefferson" in response_dt["RelatedTopics"][50]["Text"]

"""Ulysses S. Grant 18th U.S. President"""
def test_ddg37():
    assert "Grant" in response_dt["RelatedTopics"][51]["Text"]

"""Warren G. Harding 29th U.S. President"""
def test_ddg38():
    assert "Harding" in response_dt["RelatedTopics"][53]["Text"]

"""William Howard Taft 27th U.S. President"""
def test_ddg39():
    assert "Howard Taft" in response_dt["RelatedTopics"][56]["Text"]

"""William McKinley 25th U.S. President"""
def test_ddg40():
    assert "McKinley" in response_dt["RelatedTopics"][57]["Text"]

"""Woodrow Wilson 28th U.S. President"""
def test_ddg41():
    assert "Woodrow Wilson" in response_dt["RelatedTopics"][58]["Text"]

"""Zachary Taylor 12th U.S. President"""
def test_ddg42():
    assert "Taylor" in response_dt["RelatedTopics"][59]["Text"]
