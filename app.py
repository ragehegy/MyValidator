from MyValidator import jsonValidator, xmlValidator

if __name__ == "__main__":
    v = xmlValidator("trans/transaction.xml")
    v.parse()
    print(v.validate("amount", int))
    print(v.validate_schema("schema.xsd"))

    v2 = jsonValidator(path="trans/transaction.json")
    v2.parse()
    print(v2.validate("amount", int))
