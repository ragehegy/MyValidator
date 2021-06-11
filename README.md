# **MyValidator library**

A library used to validate different data types against defined criteria *(i.e. format, value, datatype, schema, ..)*

## Sample code:

```
from MyValidator import jsonValidator

v = xmlValidator("trans/transaction.xml")
v.parse() # v is XML object now.
v.validate_schema("schema.xsd") # validates the XML object against target schema XSD file.
v.validate("amount", int) # validates that all amount nodes in the XML tree are of type int.
```

# Usage:

- Initialization:

    - First you'll need a data object from file or string to work with: (`transaction.xml` or `transaction.json`)
    
    - Supported data types:
        - XML
        - JSON

    - Create a validator instance for the proposed data type:
        - for XML format use `xmlValidator` class
        - for JSON format use `jsonValidator` class

            ```
            validator1 = xmlValidator(<XMLFilePath>)
            validator2 = jsonValidator(<JSONFilePath>)
            ```

- Parsing the files:

    - Convert the string data from the instance to the corresponding data type using `validatorClass.parse()`:
        - For XML files, it'll create an XML tree object from the xml string.
        - For JSON files, `parse()` will create a dictionary object.

            ```
            validator1.parse()
            validator2.parse()
            ```

    - The function will print error messages if the file is invalid format or if it doesn't exist.

- Validating the object agains a schema:

    - for XML validators, you can use `validate_schema()` method to validate the object against a target schema file of XSD format:

        ```
        validator1.validate_schema("schema.xsd")
        ```
    
    - The method will return `True` or `False` indicating whether the object's schema matches the target schema or not.

- Validating keys and values' data types:
    
    - Validator classes have the method `validate()` that enables you to validate a key and value pair, to ensure that the value is a specific data type:

        ```
        # validating that `amount` key/tag value is of type `int`
        validator.validate("amount", int) 
        ```
