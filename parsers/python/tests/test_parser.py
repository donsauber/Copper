from copper_parser.parser import parse_copr

def test_simple_file(tmp_path):
    test_file = tmp_path / "example.copr"
    test_file.write_text("""
{Section One}
name: Alice
age: 30

[Preferences]
color: Blue
food: Pizza
""")

    result = parse_copr(test_file)
    assert result["Section One"]["name"] == "Alice"
    assert result["Section One"]["Preferences"]["food"] == "Pizza"
